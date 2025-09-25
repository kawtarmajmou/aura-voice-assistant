#!/usr/bin/env python3
"""
Aura Voice Assistant - Main Entry Point
"""
import argparse
import logging
from src.core.assistant import AuraAssistant
from src.utils.logger import setup_logging
from src.utils.config import load_config

def main():
    """Main function to start the voice assistant"""
    parser = argparse.ArgumentParser(description='Aura Voice Assistant')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--no-wake-word', action='store_true', help='Disable wake word detection')
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(debug=args.debug)
    logger = logging.getLogger(__name__)
    
    # Load configuration
    config = load_config()
    
    try:
        # Initialize assistant
        assistant = AuraAssistant(config, use_wake_word=not args.no_wake_word)
        
        logger.info("Aura Voice Assistant started successfully!")
        print("Aura is listening... Say 'Hello Aura' to start or 'quit' to exit.")
        
        # Start the assistant
        assistant.run()
        
    except KeyboardInterrupt:
        logger.info("Assistant stopped by user")
    except Exception as e:
        logger.error(f"Error starting assistant: {e}")
        raise

if __name__ == "__main__":
    main()