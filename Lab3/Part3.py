from sense_hat import SenseHat
import time
from datetime import datetime, date
from scapy.all import *

path = "/home/pi/Desktop/IMUData"

dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

rssi_max = -100000
colours = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255]]

def captured_packet_callback(pkt):
    global rssi_max
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        print("RSSI: " + str(pkt.dBm_AntSignal) + "\n")
        print("MAXXX: " + str(rssi_max) + "\n")
        if pkt.dBm_AntSignal > rssi_max:  # Check if the new RSSI is greater than the current maximum
            rssi_max = pkt.dBm_AntSignal
            set_pixel_color(rssi_max)
        time.sleep(0.1)

def set_pixel_color(rssi_value):
    if rssi_value >= rssi_max:  # Set the pixel color based on the maximum RSSI value
        sense.set_pixel(7, 7, colours[1])
    elif rssi_max - 3 <= rssi_value < rssi_max:
        sense.set_pixel(7, 7, colours[5])
    elif rssi_max - 5 <= rssi_value < rssi_max - 3:
        sense.set_pixel(7, 7, colours[2])
    elif rssi_max - 10 <= rssi_value < rssi_max - 5:
        sense.set_pixel(7, 7, colours[0])

if __name__ == "__main":
    sense = SenseHat()
    sense.clear()
    while True:
        sniff(iface=iface_n, prn=captured_packet_callback)
