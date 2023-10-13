from sense_hat import SenseHat
import time
import threading
from datetime import datetime, date
from scapy.all import *

path = "/home/pi/Desktop/IMUData"

dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

rssi_max = -34
colours = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255]]

def captured_packet_callback(pkt):
    global rssi_max
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        if pkt.dBm_AntSignal > rssi_max:
            rssi_max = pkt.dBm_AntSignal
            sense.set_pixel(7, 7, colours[1])
        elif pkt.dBm_AntSignal > rssi_max - 15 and pkt.dBm_AntSignal < rssi_max - 10:
            sense.set_pixel(7, 7, colours[5])
        elif pkt.dBm_AntSignal > rssi_max - 25 and pkt.dBm_AntSignal < rssi_max - 15:
            sense.set_pixel(7, 7, colours[2])
        elif pkt.dBm_AntSignal < rssi_max - 25:
            sense.set_pixel(7, 7, colours[0])

def packet_sniffer():
    sniff(iface=iface_n, prn=captured_packet_callback)

if __name__ == "__main__":
    sense = SenseHat()
    sense.clear()

    sniffer_thread = threading.Thread(target=packet_sniffer)
    sniffer_thread.daemon = True
    sniffer_thread.start()

    while True:
        # Your main program logic can go here
        time.sleep(1)
