import socket
import time

# Configuration
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE_PATTERN = "101010"  # Example pattern, customize as needed


def send_udp_message(message: str) -> None:
    print(f"Sending message: {message}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    try:
        while True:
            # Sending a simple pattern
            send_udp_message(MESSAGE_PATTERN)
            # Wait for a bit before sending the next pattern
            time.sleep(1)

            # You can add more patterns or logic to change the MESSAGE_PATTERN dynamically
            # For example, to create a blinking effect
            MESSAGE_PATTERN = "".join(['0' if c == '1' else '1' for c in MESSAGE_PATTERN])

    except KeyboardInterrupt:
        print("Stopped sending data.")
