import pygame
from typing import List, Tuple, Dict

import settings

def draw_lights(screen: pygame.Surface, lights_state: Dict[int, Tuple[int, int, int]],
                position_map: List[Tuple[int, int, str]]) -> None:
    """Draws lights on the screen based on their states and positions.

    Args:
        screen: The pygame surface to draw on.
        lights_state: A dictionary mapping light indices to (R, G, B) color tuples.
        position_map: A list of tuples, each representing (x, y, type) for each light.
    """
    for index, (x, y, light_type) in enumerate(position_map):
        # Fetch the light color from lights_state, defaulting to white if not found
        color = lights_state.get(index, (255, 255, 255))  # Default color
        pygame.draw.circle(screen, color, (x, y), 25)  # Assuming a fixed radius for simplicity


def update_display(screen: pygame.Surface, lights_state: Dict[int, Tuple[int, int, int]],
                   position_map: List[Tuple[int, int, str]], background_image: pygame.Surface) -> None:
    """Updates the display with the current state of all lights.

    Args:
        screen: The pygame surface for the display.
        lights_state: Current colors of the lights.
        position_map: Positions and types of the lights.
        background_image: The background image to blit onto the screen.
    """
    screen.fill(settings.BACKGROUND_COLOR)
    screen.blit(background_image, (0, 0))  # Draw the background image
    draw_lights(screen, lights_state, position_map)
    pygame.display.flip()
