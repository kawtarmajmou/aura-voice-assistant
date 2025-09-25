# Aura Voice Assistant 🎤

A Python-based intelligent voice assistant with speech recognition and natural language processing.

## Features

- 🎤 **Speech Recognition** - Using Google Speech API for accurate voice input
- 🔊 **Text-to-Speech** - Dual engine support (pyttsx3 + Google TTS)
- ⏰ **Time & Date** - Real-time time and date information
- 🌤️ **Weather Updates** - Current weather forecasts with location support
- 🤖 **Natural Language Processing** - Intent recognition and entity extraction
- 🔌 **Modular Architecture** - Easy-to-extend skill-based system
- ⚡ **Wake Word Detection** - Activate with "Aura" wake word

## Installation

### Prerequisites
- Python 3.7 or higher
- Microphone
- Internet connection (for speech recognition)

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/kawtarmajmou/aura-voice-assistant.git
cd aura-voice-assistant

# Install dependencies
pip install -r requirements.txt

# Run the assistant
python main.py
```

### Detailed Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kawtarmajmou/aura-voice-assistant.git
   cd aura-voice-assistant
   ```

2. **Install required packages:**
   ```bash
   pip install speechrecognition pyttsx3 pyaudio gtts playsound requests pyyaml python-dotenv
   ```

3. **Optional: Configure API keys** for enhanced features:
   - Edit `config/config.yaml`
   - Add your OpenWeatherMap API key for weather functionality

## Usage

### Basic Usage
```bash
# Start with wake word detection (say "Aura" to activate)
python main.py

# Start in always-listening mode (no wake word needed)
python main.py --no-wake-word

# Enable debug mode for detailed logs
python main.py --debug
```

### Voice Commands Examples

#### 🕒 Time & Date
- _"What time is it?"_
- _"What's the date today?"_
- _"What day is it?"_

#### 🌤️ Weather
- _"What's the weather like?"_
- _"Weather in London"_
- _"Will it rain today?"_

#### 💬 Conversation
- _"Hello Aura"_
- _"What's your name?"_
- _"How are you?"_
- _"Tell me a joke"_

#### 🔧 System
- _"Who made you?"_
- _"What can you do?"_
- _"Stop listening"_

#### 🚪 Exit
- _"Goodbye"_
- _"Exit"_
- _"Quit"_
- _"Stop"_

## Project Structure

```
aura-voice-assistant/
├── src/                 # Source code
│   ├── core/           # Core functionality
│   │   ├── assistant.py    # Main assistant class
│   │   ├── speech_engine.py # Speech recognition & TTS
│   │   └── wake_word.py    # Wake word detection
│   ├── nlp/            # Natural Language Processing
│   │   └── intent_parser.py # Intent recognition
│   ├── skills/         # Voice command skills
│   │   ├── skill_manager.py # Skill management
│   │   ├── weather.py      # Weather skill
│   │   ├── time.py         # Time skill
│   │   └── system.py       # System info skill
│   └── utils/          # Utilities
│       ├── config.py       # Configuration loader
│       └── logger.py       # Logging setup
├── config/             # Configuration files
│   └── config.yaml        # Main configuration
├── main.py             # Entry point
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Configuration

Edit `config/config.yaml` to customize your assistant:

```yaml
assistant:
  name: "Aura"
  version: "1.0.0"

speech:
  use_google_tts: false
  speech_timeout: 10
  phrase_time_limit: 10

skills:
  enabled:
    - weather
    - time
    - date
    - system

apis:
  openweathermap: "YOUR_API_KEY_HERE"

logging:
  level: "INFO"
```

## Skills Development

### Adding New Skills

1. Create a new skill file in `src/skills/`:
```python
import logging
from typing import Dict, Any

class NewSkill:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)
    
    def execute(self, intent: Dict[str, Any], original_text: str) -> str:
        # Your skill logic here
        return "Response from your new skill"
```

2. Register the skill in `skill_manager.py`

## Troubleshooting

### Common Issues

**Audio not working:**
- Ensure microphone is connected and not muted
- Check audio permissions for your application

**Import errors:**
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (requires 3.7+)

**Speech recognition issues:**
- Ensure stable internet connection (Google Speech API requires internet)
- Speak clearly and avoid background noise

**Windows-specific issues:**
- Install Visual C++ Build Tools for PyAudio
- Use `pipwin install pyaudio` if PyAudio installation fails

### Debug Mode

Enable debug mode for detailed logging:
```bash
python main.py --debug
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a pull request

### Areas for Contribution
- New voice skills and features
- Improved natural language processing
- Better error handling
- Additional TTS engine support
- Documentation improvements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **SpeechRecognition** library for voice input processing
- **pyttsx3** for offline text-to-speech capabilities
- **Google Text-to-Speech** for high-quality online TTS
- **OpenWeatherMap** for weather data API

## Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [Issues](https://github.com/kawtarmajmou/aura-voice-assistant/issues)
3. Create a new issue with detailed description


---

**Made with ❤️ by kawtarmajmou**

*Python Voice Assistant Project - Making AI accessible through voice interfaces*
