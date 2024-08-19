import json

def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config
