import socket
from sense_hat import SenseHat
import time

# Initialize the Sense HAT
sense = SenseHat()

def get_ip_address():
    sense.clear()
    try:
        # Create a socket to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.1)
        s.connect(("8.8.8.8", 80))  # Connect to a well-known external IP address
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        pass

def main():
    while True:
        ip_address = get_ip_address()
        if ip_address:
            # Display the IP address on the Sense HAT LED matrix
            sense.show_message("IP: " + ip_address, scroll_speed=0.05)
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
