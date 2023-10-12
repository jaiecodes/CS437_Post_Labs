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

def captured_x_packet_callback(pkt): #x-axis
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()

        x = accel['x']
        y = 0.0 # consider making this an array so that if we want to run the analysis it can access the 0
        z = 0.0  

        timestamp = datetime.now().strftime("%H:%M:%S")

        entry = str(time.time())+","+timestamp+","+str(x)+","+str(y)+","+str(z)+","+str(pkt.dBm_AntSignal)+"\n"

        with open(filename, "a") as f:
            f.write(entry)
        
        time.sleep(1)


def captured_y_packet_callback(pkt): #x-axis
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()

        x = 0.0 
        y = accel['y'] # consider making this an array so that if we want to run the analysis it can access the 0
        z = 0.0  

        timestamp = datetime.now().strftime("%H:%M:%S")

        entry = str(time.time())+","+timestamp+","+str(x)+","+str(y)+","+str(z)+","+str(pkt.dBm_AntSignal)+"\n"

        with open(filename, "a") as f:
            f.write(entry)
        
        time.sleep(1)




if __name__ == "__main__":
    sense=SenseHat()
    y_start = False
    x_start = False
    sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
    
    x = AsyncSniffer(iface=iface_n, prn=captured_x_packet_callback, store=0)
    y = AsyncSniffer(iface=iface_n, prn=captured_y_packet_callback, store=0)
    while True:
        for event in sense.stick.get_events():
            if event.action == 'pressed' and event.direction == 'right':
                x.daemon = True
                x.start()
                if y_start is True:
                    y.stop()
            if event.action == 'pressed' and event.direction == 'down':
                y_start = True
                y.daemon = True
                y.start()
                if x_start is True:
                    x.stop()
