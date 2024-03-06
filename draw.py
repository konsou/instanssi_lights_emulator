import pygame
from typing import Tuple, Dict


def draw_light(screen: pygame.Surface, index: int, color: Tuple[int, int, int],
               position_map: Dict[int, Tuple[int, int]]) -> None:
    """Draws a light on the screen based on its index using a provided position map."""
    x, y = position_map.get(index, (0, 0))
    pygame.draw.circle(screen, color, (x, y), 25)  # Use a fixed radius or import from settings


def update_display(screen: pygame.Surface, lights_state: Dict[int, Tuple[int, int, int]],
                   position_map: Dict[int, Tuple[int, int]], background_image: pygame.Surface) -> None:
    """Updates the display with the current state of all lights."""
    screen.blit(background_image, (0, 0))  # Draw the background image
    for index, color in lights_state.items():
        draw_light(screen, index, color, position_map)
    pygame.display.flip()
