import logging
from typing import Dict, Any

class SkillManager:
    """Manages and executes skills"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.skills = self._load_skills()
    
    def _load_skills(self) -> Dict[str, Any]:
        """Load skills"""
        skills = {}
        
        # Weather skill
        try:
            from src.skills.weather import WeatherSkill
            skills['weather'] = WeatherSkill(self.config)
        except ImportError as e:
            self.logger.warning(f"Weather skill not available: {e}")
        
        # Time skill
        try:
            from src.skills.time import TimeSkill
            skills['time'] = TimeSkill(self.config)
        except ImportError:
            pass
            
        # System skill
        try:
            from src.skills.system import SystemSkill
            skills['system'] = SystemSkill(self.config)
        except ImportError:
            pass
        
        return skills
    
    def execute(self, intent: Dict[str, Any], original_text: str) -> str:
        """Execute the appropriate skill based on intent"""
        intent_name = intent['intent']
        
        if intent_name in self.skills:
            try:
                skill = self.skills[intent_name]
                return skill.execute(intent, original_text)
            except Exception as e:
                self.logger.error(f"Error executing skill {intent_name}: {e}")
                return f"Sorry, I encountered an error while processing your request."
        
        elif intent_name == 'greeting':
            return "Hello! I'm Aura, your voice assistant. How can I help you today?"
        
        elif intent_name == 'unknown':
            return "I'm not sure how to help with that. Try asking about weather, time, or just say hello!"
        
        else:
            return "I don't know how to handle that request yet."