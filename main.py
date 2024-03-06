import socket
import pygame
import sys
from typing import Tuple

# Configuration
UDP_IP = "127.0.0.1"  # Listen on all interfaces
UDP_PORT = 5005
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
LIGHT_RADIUS = 50
LIGHTS_PER_ROW = SCREEN_WIDTH // (2 * LIGHT_RADIUS)
BACKGROUND_COLOR = (0, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Instanssi Lights Emulator")


def draw_light(x: int, y: int, color: Tuple[int, int, int]) -> None:
    """Draws a light on the screen."""
    pygame.draw.circle(screen, color, (x, y), LIGHT_RADIUS)


def parse_data(data: str) -> None:
    """Parses the received data and updates the display accordingly."""
    screen.fill(BACKGROUND_COLOR)
    for i, char in enumerate(data.strip()):
        row = i // LIGHTS_PER_ROW
        col = i % LIGHTS_PER_ROW
        x = col * 2 * LIGHT_RADIUS + LIGHT_RADIUS
        y = row * 2 * LIGHT_RADIUS + LIGHT_RADIUS

        if char == '1':
            draw_light(x, y, (0, 255, 0))  # Green for "on"
        elif char == '0':
            draw_light(x, y, (75, 75, 75))  # Dim gray for "off"

    pygame.display.flip()


def main():
    # Setup UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Listening for data on UDP port {UDP_PORT}...")

    try:
        while True:
            data, _ = sock.recvfrom(1024)  # buffer size is 1024 bytes
            parse_data(data.decode('utf-8'))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
