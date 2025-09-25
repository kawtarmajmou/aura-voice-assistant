import speech_recognition as sr
import logging

class WakeWordDetector:
    """Simple wake word detection"""
    
    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.wake_word = "aura"
        
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
    
    def detect(self) -> bool:
        """Detect wake word"""
        try:
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=2)
            
            text = self.recognizer.recognize_google(audio).lower()
            return self.wake_word in text
            
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return False
        except Exception as e:
            self.logger.error(f"Wake word detection error: {e}")
            return False