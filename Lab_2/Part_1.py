import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import scapy

capture = sniff()
wrpcap("Part1.pcap", capture)
