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


def captured_packet_callback(pkt): #x-axis
    global x_pos 
    global y_pos
    
    
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()
    
        x_axis = True
        disabled = True
        initialized = False
        for event in sense.stick.get_events():
            if event.action == 'held' and event.direction == 'right': # x axis movement
                initialized = True
                x_axis = True
                disabled = False
                x_pos =  accel['x']
                break 
            if event.action == 'held' and event.direction == 'down': # y axis movement
                initialized = True
                x_axis = False
                disabled = False
                y_pos =  accel['y']
                break
            if event.action == 'pressed' and event.direction == 'left':#initialziation
                x_pos = 0.0
                y_pos = 0.0
                initialized = True
                break
            if event.action == 'release' and event.direction == 'down': # when you release it should save x
                initialized = True
                x_pos =  accel['x']
                print(str(x_pos))
                break
            if event.action == 'release' and event.direction == 'right':
                initialized = True
                y_pos =  accel['y']
                print(str(y_pos))
                break
            

        if initialized is True:
            if disabled is True:
                x = x_pos
                y = y_pos # consider making this an array so that if we want to run the analysis it can access the 0
                z = 0.0  
            else:
                if x_axis is True:
                    x = accel['x']
                    y = y_pos # consider making this an array so that if we want to run the analysis it can access the 0
                    z = 0.0  
                else:
                    x = x_pos 
                    y = accel['y'] # consider making this an array so that if we want to run the analysis it can access the 0
                    z = 0.0  

            timestamp = datetime.now().strftime("%H:%M:%S")
            #print("Value of x:" + x + " Value of Y:" + y)
            entry = str(time.time())+","+timestamp+","+str(x)+","+str(y)+","+str(z)+","+str(pkt.dBm_AntSignal)+"\n"

            with open(filename, "a") as f:
                f.write(entry)
            
            #time.sleep(1)

if __name__ == "__main__":
    
    sense=SenseHat()
    sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
    sniff(iface=iface_n, prn=captured_packet_callback)


       


