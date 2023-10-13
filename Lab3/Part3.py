from sense_hat import SenseHat
import time
from datetime import datetime,date
from scapy.all import *


path="/home/pi/Desktop/IMUData"



dev_mac = "e4:5f:01:d4:9d:ce"  # Assigned transmitter MAC
iface_n = "wlan1"  # Interface for network adapter

rssi_max = -100000
colours = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255]]

def captured_packet_callback(pkt): #x-axis  
    global rssi_max
    if pkt.haslayer(Dot11) and pkt.addr2 == dev_mac: 
      print("RSSI: "+str(pkt.dBm_AntSignal)+"\n")     
      print("MAXXX: "+str(rssi_max)+"\n")    
      if abs(pkt.dBm_AntSignal) > abs(rssi_max):
        print("GREEEN \n")    
        rssi_max = pkt.dBm_AntSignal
        sense.set_pixel(7,7, colours[1])
      elif abs(pkt.dBm_AntSignal) > abs(rssi_max) + 3: 
        print("TEAL "+str(abs(rssi_max) - 3)+"\n")  
        sense.set_pixel(7,7, colours[5])
      elif abs(pkt.dBm_AntSignal) > abs(rssi_max) + 5: 
        print("BLUE "+str(abs(rssi_max) - 5)+"\n")  
        sense.set_pixel(7,7, colours[2])
      elif abs(pkt.dBm_AntSignal) > abs(rssi_max) + 10: 
        print("RED "+str(abs(rssi_max) - 10)+"\n")  
        sense.set_pixel(7,7, colours[0])
      time.sleep(0.1)


if __name__ == "__main__":
    sense=SenseHat()
    sense.clear()
    sniff(iface=iface_n, prn=captured_packet_callback)
