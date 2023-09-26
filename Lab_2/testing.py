import matplotlib.pyplot as plt
import numpy as np
from scapy.all import *

def analyze_pcap(pcap_file):
    # Initialize variables to store motion event data
    timestamps = []
    motion_events = []

    # Open the pcap file and analyze packets
    packets = rdpcap(pcap_file)
    for packet in packets:
        # Implement your logic here to detect motion events.
        # You might look for specific patterns or protocols related to motion detection.

        # Example logic: Detect packets with a specific port number (adjust as needed)
        if packet.haslayer(UDP) and packet[UDP].dport == 5000:
            timestamps.append(packet.time)
            motion_events.append(1)
        else:
            timestamps.append(packet.time)
            motion_events.append(0)

    return timestamps, motion_events

def plot_timeline(timestamps, motion_events):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, motion_events, 'r-', linewidth=1)
    plt.xlabel('Time')
    plt.ylabel('Motion Detection')
    plt.title('Motion Detection Timeline')
    plt.ylim([-0.1, 1.1])  # Set y-axis limits
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    pcap_file = '/home/pi/Desktop/Code/PostLabs/CS437_Post_Labs/Lab_2/packet_capture.pcap'  # Replace with your pcap file path
    timestamps, motion_events = analyze_pcap(pcap_file)
    plot_timeline(timestamps, motion_events)
