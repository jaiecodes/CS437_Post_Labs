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

x_accel = 0.0
y_accel = 0.0
is_intialized = False
direction = 0 ## 0 is forward, 1 is right, 2 is bottom, 3 is left
count = 0


def captured_packet_callback(pkt): #x-axis
    global x_accel 
    global y_accel
    global is_intialized
    global count
    global direction
    
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()
    
        
        for event in sense.stick.get_events():
           
            if event.action == 'pressed' and event.direction == 'right': # x axis movement
                direction = 0    
                count = count + 1         
                break 
            if event.action == 'pressed' and event.direction == 'down': # y axis movement
                direction = 1   
                count = count + 1        
                break
            if event.action == 'pressed' and event.direction == 'left':#initialziation
                direction = 2
                count = count + 1  
                break
            if event.action == 'pressed' and event.direction == 'up':#initialziation
                direction = 3
                count = count + 1  
                break
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        #print("Value of x:" + x + " Value of Y:" + y)
        
        entry = str(time.time())+","+timestamp+","+str(accel['x'])+","+str(accel['y'])+","+str(accel['z'])+","+str(count)+ ","+str(direction)+","+str(pkt.dBm_AntSignal)+"\n"

        with open(filename, "a") as f:
            f.write(entry)
    
        #time.sleep(1)

if __name__ == "__main__":
    
    sense=SenseHat()
    sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
    sniff(iface=iface_n, prn=captured_packet_callback)


       


