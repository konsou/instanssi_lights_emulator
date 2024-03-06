# position_map.py
import json
from typing import Dict, Tuple


def load_position_map(filename: str) -> Dict[int, Tuple[int, int]]:
    """Load the position map from a JSON file."""
    try:
        with open(filename, 'r') as f:
            position_map_data = json.load(f)
        # Convert keys from string to integer, and values to tuple
        position_map = {int(k): tuple(v) for k, v in position_map_data.items()}
        return position_map
    except FileNotFoundError:
        print(f"Position map file not found: {filename}")
        raise
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the position map file: {filename}")
        raise
