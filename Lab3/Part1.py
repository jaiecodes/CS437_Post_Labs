from sense_hat import SenseHat
import numpy as np
import time
from datetime import datetime,date
from scapy.all import *


path="/home/pi/Desktop/IMUData16:25:06.csv"



dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

timestamp_fname=datetime.now().strftime("%H:%M:%S")
filename=path+timestamp_fname+".csv"

x_accel = 0.0
y_accel = 0.0
is_intialized = False

def captured_packet_callback(pkt): #x-axis
    global x_accel 
    global y_accel
    global is_intialized
    
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()
    
        enabled = False

        x_accel = 0.0
        y_accel = 0.0
        z_accel = accel['z']

        for event in sense.stick.get_events():
            if event.action == 'held' and event.direction == 'right': # x axis movement
                enabled = True
                x_accel = np.absolute(accel['x'])
                break 
            if event.action == 'held' and event.direction == 'down': # y axis movement
                enabled = True
                y_accel = np.absolute(accel['y'])
                break
            if event.action == 'held' and event.direction == 'left':#initialziation
                enabled = True
                x_accel = -1.0 * np.absolute(accel['x'])
                break
            if event.action == 'held' and event.direction == 'up':#initialziation
                enabled = True
                y_accel = -1.0 * np.absolute(accel['y'])
                break

        if is_intialized is False: 
            is_intialized = True
            timestamp = datetime.now().strftime("%H:%M:%S")
            #print("Value of x:" + x + " Value of Y:" + y)
            entry = str(time.time())+","+timestamp+","+str(0.0)+","+str(0.0)+","+str(0.0)+","+str(pkt.dBm_AntSignal)+"\n"

            with open(filename, "a") as f:
                f.write(entry)

        if enabled is True:
        
            timestamp = datetime.now().strftime("%H:%M:%S")
            #print("Value of x:" + x + " Value of Y:" + y)
            entry = str(time.time())+","+timestamp+","+str(x_accel)+","+str(y_accel)+","+str(z_accel)+","+str(pkt.dBm_AntSignal)+"\n"

            with open(filename, "a") as f:
                f.write(entry)
        
        #time.sleep(1)

if __name__ == "__main__":
    
    sense=SenseHat()
    sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
    sniff(iface=iface_n, prn=captured_packet_callback)


       


