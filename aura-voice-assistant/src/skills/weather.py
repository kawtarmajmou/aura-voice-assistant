import requests
import logging
from typing import Dict, Any

class WeatherSkill:
    """Weather information skill"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.api_key = config.get('apis', {}).get('openweathermap')
    
    def execute(self, intent: Dict[str, Any], original_text: str) -> str:
        """Get weather information"""
        if not self.api_key or self.api_key == "YOUR_API_KEY_HERE":
            return "Weather service is not configured. Please add your OpenWeatherMap API key to the config file."
        
        entities = intent.get('entities', {})
        location = entities.get('location', 'London')  # Default location
        
        try:
            params = {
                'q': location,
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
            data = response.json()
            
            if response.status_code == 200:
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                return f"The weather in {location} is {desc} with a temperature of {temp} degrees Celsius."
            else:
                return f"Sorry, I couldn't get the weather for {location}."
                
        except Exception as e:
            self.logger.error(f"Weather API error: {e}")
            return "Sorry, I'm having trouble accessing weather information right now."