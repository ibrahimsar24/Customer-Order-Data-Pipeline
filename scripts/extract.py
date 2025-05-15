import json
import os
from typing import List, Dict, Any

def extract_json(filepath: str) -> List[Dict[Any, Any]]:
    """
    Load JSON data from a file or directory.
    If filepath is a directory, it will load all .json files in that directory.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Path does not exist: {filepath}")
    
    all_data = []
    
    if os.path.isdir(filepath):
        # Process all JSON files in the directory
        for filename in os.listdir(filepath):
            if filename.endswith('.json'):
                file_path = os.path.join(filepath, filename)
                try:
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        if isinstance(data, list):
                            all_data.extend(data)
                        else:
                            all_data.append(data)
                except Exception as e:
                    print(f"Error reading {file_path}: {str(e)}")
    else:
        # Process single JSON file
        with open(filepath, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                all_data.extend(data)
            else:
                all_data.append(data)
    
    return all_data
