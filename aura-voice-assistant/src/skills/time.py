import datetime
import logging
from typing import Dict, Any

class TimeSkill:
    """Time information skill"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    def execute(self, intent: Dict[str, Any], original_text: str) -> str:
        """Get current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."