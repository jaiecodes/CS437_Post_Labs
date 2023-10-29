sudo wpa_cli -i wlan1 terminate
sudo ip link set wlan1 down
sudo iw dev wlan1 set type monitor
sudo iwconfig wlan1 channel 6
sudo iw wlan1 set freq 2437 20Mhz
sudo ip link set wlan1 up