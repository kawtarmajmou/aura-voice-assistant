import yaml
import os

def load_config():
    """Load configuration from YAML file"""
    try:
        config_path = os.path.join('config', 'config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config or {}
    except FileNotFoundError:
        print("Config file not found. Using default configuration.")
        return {}
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}