import speech_recognition as sr
import pyttsx3
import threading
import logging
from gtts import gTTS
import tempfile
import os
from playsound import playsound

class SpeechEngine:
    """Handles speech recognition and text-to-speech"""
    
    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Adjust for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
        
        # Initialize TTS engine
        self.tts_engine = pyttsx3.init()
        self._setup_tts()
        
        # Use Google TTS as fallback
        self.use_google_tts = config.get('speech', {}).get('use_google_tts', False)
    
    def _setup_tts(self):
        """Setup TTS engine properties"""
        voices = self.tts_engine.getProperty('voices')
        if voices and len(voices) > 1:
            self.tts_engine.setProperty('voice', voices[1].id)  # Female voice
        
        rate = self.tts_engine.getProperty('rate')
        self.tts_engine.setProperty('rate', rate - 50)
        
        volume = self.tts_engine.getProperty('volume')
        self.tts_engine.setProperty('volume', min(volume + 0.2, 1.0))
    
    def listen(self) -> str:
        """Listen for speech and return transcribed text"""
        try:
            self.logger.info("Listening...")
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=10)
            
            self.logger.info("Processing speech...")
            text = self.recognizer.recognize_google(audio)
            self.logger.info(f"Recognized: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            self.logger.info("Listening timeout")
            return ""
        except sr.UnknownValueError:
            self.logger.info("Could not understand audio")
            return ""
        except sr.RequestError as e:
            self.logger.error(f"Speech recognition error: {e}")
            return ""
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            return ""
    
    def speak(self, text: str):
        """Convert text to speech"""
        if not text:
            return
            
        self.logger.info(f"Speaking: {text}")
        
        if self.use_google_tts:
            self._speak_google(text)
        else:
            self._speak_pyttsx3(text)
    
    def _speak_pyttsx3(self, text: str):
        """Use pyttsx3 for speech"""
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            self.logger.error(f"TTS error: {e}")
    
    def _speak_google(self, text: str):
        """Use Google TTS for speech"""
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                tts.save(tmp_file.name)
                playsound(tmp_file.name)
                os.unlink(tmp_file.name)
        except Exception as e:
            self.logger.error(f"Google TTS error: {e}")
            # Fallback to pyttsx3
            self._speak_pyttsx3(text)