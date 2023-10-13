from sense_hat import SenseHat
import time
from datetime import datetime,date
from scapy.all import *


path="/home/pi/Desktop/IMUData"



dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

timestamp_fname=datetime.now().strftime("%H:%M:%S")
filename=path+timestamp_fname+".csv"

step_length= 0.415 * height # in meters
def captured_packet_callback(pkt): #x-axis  
    xpos = [0]
    ypos = [0]  
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:
        accel = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        mag = sense.get_compass_raw()
    
    
      
    for event in sense.stick.get_events():  
        if event.action == 'pressed' and event.direction == 'right': # x axis movement
            xpos.append(step_length[-1] + step_length)
        if event.action == 'pressed' and event.direction == 'right': # x axis movement
            xpos.append(step_length[-1] - step_length)
        if event.action == 'pressed' and event.direction == 'right': # x axis movement
            ypos.append(step_length[-1] + step_length)
        if event.action == 'pressed' and event.direction == 'right': # x axis movement
            ypos.append(step_length[-1] - step_length)
            
            
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


       


