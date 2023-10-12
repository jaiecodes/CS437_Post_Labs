from sense_hat import SenseHat
import numpy as np
import time
import scipy.signal as signal
from datetime import datetime,date
import matplotlib.pyplot as plt
import pandas as pd
import scipy
from scapy.all import *

import scipy.integrate as integrate
path="/home/pi/Desktop/Code/Lab3/Part2/IMUDataRSSI"



dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

timestamp_fname=datetime.now().strftime("%H:%M:%S")
filename=path+timestamp_fname+".csv"

def captured_packet_callback(pkt): #x-axis
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()

        x = accel['x']
        y = 0 # consider making this an array so that if we want to run the analysis it can access the 0
        z = 0  

        timestamp = datetime.now().strftime("%H:%M:%S")

        entry = str(time.time())+","+timestamp+","+str(x)+","+str(y)+","+str(z)+","+str(pkt.dBm_AntSignal)+"\n"

        with open(filename, "a") as f:
            f.write(entry)
        
        time.sleep(1)



if __name__ == "__main__":
    sense=SenseHat()
    sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
    sniff(iface=iface_n, prn=captured_packet_callback)