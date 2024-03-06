import json
from typing import List, Tuple


def load_position_map(filename: str) -> List[Tuple[int, int, str]]:
    """Load the position map from a JSON file."""
    try:
        with open(filename, 'r') as f:
            position_map_data = json.load(f)
        # Convert each list to a tuple
        position_map = [tuple(item) for item in position_map_data]
        return position_map
    except FileNotFoundError:
        print(f"Position map file not found: {filename}")
        raise
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the position map file: {filename}")
        raise
