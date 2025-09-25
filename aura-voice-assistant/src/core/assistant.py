import threading
import queue
import time
import logging
from typing import Dict, Any

from src.core.speech_engine import SpeechEngine
from src.core.wake_word import WakeWordDetector
from src.nlp.intent_parser import IntentParser
from src.skills.skill_manager import SkillManager

class AuraAssistant:
    """Main voice assistant class"""
    
    def __init__(self, config: Dict[str, Any], use_wake_word: bool = True):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        self.speech_engine = SpeechEngine(config)
        self.intent_parser = IntentParser(config)
        self.skill_manager = SkillManager(config)
        
        # Wake word detection
        self.use_wake_word = use_wake_word
        if use_wake_word:
            self.wake_detector = WakeWordDetector(config)
        
        # Threading and queues
        self.command_queue = queue.Queue()
        self.is_running = False
        
    def run(self):
        """Main run loop"""
        self.is_running = True
        
        if self.use_wake_word:
            print("Say 'Aura' to wake me up!")
            # Simple wake word detection without threading for now
            self._simple_wake_word_mode()
        else:
            print("I'm always listening...")
            self._always_listening_mode()
    
    def _simple_wake_word_mode(self):
        """Simple mode with wake word detection"""
        while self.is_running:
            try:
                if self.wake_detector.detect():
                    self.speech_engine.speak("Yes, I'm listening")
                    self._listen_and_process()
                time.sleep(0.5)
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Error: {e}")
    
    def _always_listening_mode(self):
        """Always listening mode"""
        while self.is_running:
            try:
                self._listen_and_process()
            except KeyboardInterrupt:
                break
            except Exception as e:
                self.logger.error(f"Error: {e}")
    
    def _listen_and_process(self):
        """Listen for command and process it"""
        command = self.speech_engine.listen()
        if command:
            if command.lower() in ['quit', 'exit', 'stop', 'goodbye']:
                self.speech_engine.speak("Goodbye!")
                self.is_running = False
                return
            
            # Process the command
            self._process_command(command)
    
    def _process_command(self, command: str):
        """Process a single command"""
        self.logger.info(f"Processing command: {command}")
        
        # Parse intent
        intent = self.intent_parser.parse(command)
        self.logger.info(f"Detected intent: {intent['intent']}")
        
        # Execute skill
        response = self.skill_manager.execute(intent, command)
        
        # Speak response
        if response:
            self.speech_engine.speak(response)
    
    def stop(self):
        """Stop the assistant"""
        self.is_running = False
        self.logger.info("Assistant stopped")