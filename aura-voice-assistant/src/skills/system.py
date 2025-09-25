import logging
from typing import Dict, Any

class SystemSkill:
    """System information skill"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    def execute(self, intent: Dict[str, Any], original_text: str) -> str:
        """Handle system commands"""
        text = intent.get('original_text', '').lower()
        
        if 'your name' in text:
            return "My name is Aura, your voice assistant."
        elif 'who are you' in text:
            return "I'm Aura, a voice assistant created to help you with various tasks."
        elif 'how are you' in text:
            return "I'm functioning well, thank you for asking!"
        else:
            return "I'm here to help! You can ask me about time, weather, or just chat."