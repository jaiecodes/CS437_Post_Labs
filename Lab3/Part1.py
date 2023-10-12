from sense_hat import SenseHat
import numpy as np
import time
from datetime import datetime,date
from scapy.all import *


path="/home/pi/Desktop/IMUData"



dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

timestamp_fname=datetime.now().strftime("%H:%M:%S")
filename=path+timestamp_fname+".csv"

def captured_packet_callback(pkt, x_axis): #x-axis
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()

        if x_axis is True:
            x = accel['x']
            y = 0.0 # consider making this an array so that if we want to run the analysis it can access the 0
            z = 0.0  
        else:
            x = 0.0 
            y = accel['y'] # consider making this an array so that if we want to run the analysis it can access the 0
            z = 0.0  

        timestamp = datetime.now().strftime("%H:%M:%S")
        print("Value of x:" + x + " Value of Y:" + y)
        entry = str(time.time())+","+timestamp+","+str(x)+","+str(y)+","+str(z)+","+str(pkt.dBm_AntSignal)+"\n"

        with open(filename, "a") as f:
            f.write(entry)
        
        time.sleep(1)




if __name__ == "__main__":
    sense=SenseHat()
    sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
    x_enabled = True
    sniff(iface=iface_n, prn=captured_packet_callback(packet, x_enabled))
    #sniff(iface=iface_n, prn=captured_packet_callback, packet=captured_packet_callback(packet, x_enabled), store=0)
    while True:
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'right':
                x_enabled = True
            if event.action == 'pressed' and event.direction == 'down':
                x_enabled = False


