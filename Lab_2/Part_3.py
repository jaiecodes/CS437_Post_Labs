from scapy.all import *
import matplotlib.pyplot as plt

def read_pcap(file):
    timestamps = []

    packets = rdpcap(file)
    for packet in packets:
        timestamps.append(packet.time)

    return timestamps

def detect_traffic(timestamps, threshold=0.1):
    traffic_pattern = []

    for i in range(1, len(timestamps)):
        time_diff = timestamps[i] - timestamps[i - 1]

        if time_diff < threshold:
            traffic_pattern.append(1)  # Detected traffic burst
        else:
            traffic_pattern.append(0)  # No traffic burst

    return traffic_pattern

def plot_traffic_pattern(timestamps, traffic_pattern):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps[1:], traffic_pattern, 'r-', linewidth=1)
    plt.xlabel('Time')
    plt.ylabel('Traffic Burst Detected')
    plt.title('Traffic Burst Detection')
    plt.ylim([-0.1, 1.1])
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    file = '/home/pi/Desktop/Code/PostLabs/CS437_Post_Labs/Lab_2/packet_capture.pcap'
    timestamps = read_pcap(file)
    traffic_pattern = detect_traffic(timestamps, threshold=0.1)  # Adjust the threshold as needed
    plot_traffic_pattern(timestamps, traffic_pattern)
