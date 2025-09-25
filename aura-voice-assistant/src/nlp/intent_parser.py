import re
import logging
from typing import Dict, Any

class IntentParser:
    """Natural Language Processing for intent recognition"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)
        
        # Define intent patterns
        self.intent_patterns = {
            'weather': [
                r'.*(weather|temperature|forecast).*',
                r'.*(how).*(outside).*',
                r'.*(will it).*(rain|snow).*'
            ],
            'time': [
                r'.*(time).*',
                r'.*(what).*(time).*'
            ],
            'date': [
                r'.*(date|today).*',
                r'.*(what).*(date).*'
            ],
            'greeting': [
                r'.*(hello|hi|hey).*',
                r'.*(good morning|good afternoon).*'
            ],
            'joke': [
                r'.*(joke|funny).*'
            ],
            'calculation': [
                r'.*(calculate|what is).*(\d+).*',
                r'.*(math|equation).*'
            ]
        }
    
    def parse(self, text: str) -> Dict[str, Any]:
        """Parse text and return intent with entities"""
        text = text.lower().strip()
        
        # Check for each intent
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.match(pattern, text):
                    entities = self._extract_entities(intent, text)
                    return {
                        'intent': intent,
                        'confidence': 0.9,
                        'entities': entities,
                        'original_text': text
                    }
        
        # Default fallback intent
        return {
            'intent': 'unknown',
            'confidence': 0.0,
            'entities': {},
            'original_text': text
        }
    
    def _extract_entities(self, intent: str, text: str) -> Dict[str, Any]:
        """Extract entities based on intent"""
        entities = {}
        
        if intent == 'weather':
            # Extract location
            location_match = re.search(r'in\s+(\w+)', text)
            if location_match:
                entities['location'] = location_match.group(1)
        
        return entities