from sense_hat import SenseHat
import time
from datetime import datetime,date
from scapy.all import *


path="/home/pi/Desktop/IMUData"



dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

timestamp_fname=datetime.now().strftime("%H:%M:%S")
filename=path+timestamp_fname+".csv"
height=1.95 # in meters
step_length= 0.415 * height # in meters
xpos = 0.0
ypos = 0.0
init = False
rssi_max = -100000
colours = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]

def captured_packet_callback(pkt): #x-axis  
    global xpos
    global ypos
    global init
    global rssi_max
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac:      
      if pkt.dBm_AntSignal > rssi_max:
        rssi_max = pkt.dBm_AntSignal
        sense.set_pixel(8,8, colours[1])

      if abs(pkt.dBm_AntSignal) < abs(rssi_max - 5): 
      sense.set_pixel(8,8, colours[2])

      if abs(pkt.dBm_AntSignal) < abs(rssi_max - 10): 
      sense.set_pixel(8,8, colours[0])


if __name__ == "__main__":
    sense=SenseHat()
    sense.clear()
    sense.set_imu_config(True,True,True) ## Config the Gyroscope, Accelerometer, Magnetometer
    sniff(iface=iface_n, prn=captured_packet_callback)
    
    
    


       


