import os
import logging
from typing import Optional
import json

def setup_logging(log_file: str = 'agent_activity.log') -> logging.Logger:
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('AgentManager')

def save_locally(content: str, filename: str, directory: str = 'outputs') -> Optional[str]:
    """Save content to a local file"""
    try:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filepath
    except Exception as e:
        print(f"Error saving to file: {str(e)}")
        return None

def format_output(output) -> str:
    """Format output to string"""
    if isinstance(output, dict):
        return json.dumps(output, ensure_ascii=False, indent=2)
    return str(output)