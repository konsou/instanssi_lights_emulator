import pygame
import sys
import select
import socket
from draw import update_display
import settings
from position_map import load_position_map

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Instanssi Lights Emulator")

# Load the background image
background_image = pygame.image.load(settings.BACKGROUND_IMAGE_PATH)

# Load the position map
position_map = load_position_map(settings.POSITION_MAP_FILE)

# Dictionary to store the state of each light
lights_state = {index: (0, 0, 0) for index in range(28)}


def parse_data(data: bytes) -> None:
    """Parses the received data and updates the lights' state."""
    # Skipping the protocol version and nickname for simplicity
    commands = data.split(b'\x00', 2)[-1]  # Remove nickname part
    for i in range(0, len(commands), 6):  # Each command is 6 bytes
        if len(commands[i:i + 6]) < 6:
            continue  # Incomplete command, ignore
        _, light_index, _, r, g, b = commands[i:i + 6]
        lights_state[light_index] = (r, g, b)


def main():
    # Update the display to show the background image from the beginning
    update_display(screen=screen,
                   lights_state=lights_state,
                   position_map=position_map,
                   background_image=background_image)

    # Set up your socket here
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((settings.UDP_IP, settings.UDP_PORT))
    sock.setblocking(False)  # Make the socket non-blocking

    try:
        while True:
            # Use select with a timeout to wait for network activity
            readable, _, _ = select.select([sock], [], [], 0.1)  # 0.1-second timeout

            # Process network data if available
            if sock in readable:
                data, _ = sock.recvfrom(1024)
                parse_data(data)
                update_display(screen=screen,
                               lights_state=lights_state,
                               position_map=position_map,
                               background_image=background_image)

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
