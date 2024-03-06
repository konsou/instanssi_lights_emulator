import socket
import pygame
import sys
from typing import Tuple

import select

# Configuration
UDP_IP = "127.0.0.1"
UDP_PORT = 9909
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
LIGHT_RADIUS = 25
LIGHTS_PER_ROW = 7  # To fit 28 lights in a grid, 7x4
BACKGROUND_COLOR = (0, 0, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Instanssi Lights Emulator")

# Dictionary to store the state of each light
lights_state = {index: (0, 0, 0) for index in range(28)}


def draw_light(index: int, color: Tuple[int, int, int]) -> None:
    """Draws a light on the screen based on its index."""
    col = index % LIGHTS_PER_ROW
    row = index // LIGHTS_PER_ROW
    x = col * (2 * LIGHT_RADIUS + 10) + LIGHT_RADIUS + 10
    y = row * (2 * LIGHT_RADIUS + 10) + LIGHT_RADIUS + 10
    pygame.draw.circle(screen, color, (x, y), LIGHT_RADIUS)


def update_display() -> None:
    """Updates the display with the current state of all lights."""
    screen.fill(BACKGROUND_COLOR)
    for index, color in lights_state.items():
        draw_light(index, color)
    pygame.display.flip()


def parse_data(data: bytes) -> None:
    """Parses the received data and updates the lights' state."""
    # Skipping the protocol version and nickname for simplicity
    commands = data.split(b'\x00', 2)[-1]  # Remove nickname part
    for i in range(0, len(commands), 6):  # Each command is 6 bytes
        if len(commands[i:i + 6]) < 6:
            continue  # Incomplete command, ignore
        _, light_index, _, r, g, b = commands[i:i + 6]
        lights_state[light_index] = (r, g, b)


def udp_listener():
    """Listens for UDP packets and updates the lights' state."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Listening for data on UDP port {UDP_PORT}...")

    while True:
        data, _ = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Data received: {data}")
        parse_data(data)
        update_display()


def main():
    # Set up your socket here
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.setblocking(False)  # Make the socket non-blocking

    try:
        while True:
            # Use select with a timeout to wait for network activity
            readable, _, _ = select.select([sock], [], [], 0.1)  # 0.1-second timeout

            # Process network data if available
            if sock in readable:
                data, _ = sock.recvfrom(1024)
                parse_data(data)
                update_display()

            # Process pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
