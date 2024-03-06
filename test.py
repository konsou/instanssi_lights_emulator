import socket
import time
from typing import Tuple

# Configuration
UDP_IP = "127.0.0.1"
UDP_PORT = 9909


def create_light_command(index: int, color: Tuple[int, int, int]) -> bytearray:
    """Creates a single light command for a given light index and RGB color."""
    effect_type = 1  # Light effect
    extension_byte = 0  # Currently unused, must be 0
    r, g, b = color
    return bytearray([effect_type, index, extension_byte, r, g, b])


def create_packet(nickname: str, commands: bytearray) -> bytearray:
    """Creates a complete UDP packet with the specified nickname and light commands."""
    packet = bytearray([1])  # Protocol version
    packet.extend(bytearray([0]))  # Nickname start
    packet.extend(nickname.encode('utf-8'))
    packet.extend(bytearray([0]))  # Nickname end
    packet.extend(commands)
    return packet


def send_udp_message(packet: bytearray) -> None:
    """Sends the given packet to the specified UDP address and port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(packet, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    nickname = "test_cycle"
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

    for color in colors:
        for index in range(28):  # Assuming 28 lights
            commands = create_light_command(index, color)
            packet = create_packet(nickname, commands)
            send_udp_message(packet)
            time.sleep(0.1)  # Wait a bit before sending the next command
