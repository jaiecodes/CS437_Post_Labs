import matplotlib.pyplot as plt
import numpy as np
from scapy.all import *

def read_pcap(file):
    time = []
    motion = []

    packets = rdpcap(file)
    for packet in packets:
        if packet.haslayer(UDP) and packet[UDP].dport == 5000:
            time.append(packet.time)
            motion.append(1)
        else:
            time.append(packet.time)
            motion.append(0)

    return time, motion

def plot(time, motion):
    plt.figure(figsize=(12, 6))
    plt.plot(time, motion, 'r-', linewidth=1)
    plt.xlabel('Time')
    plt.ylabel('Is Motion Dectected?')
    plt.title('Motion Detection Timeline')
    plt.ylim([-0.1, 1.1])
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    file = '/home/pi/Desktop/Code/PostLabs/CS437_Post_Labs/Lab_2/packet_capture.pcap'
    time, motion = read_pcap(file)
    plot(time, motion)
