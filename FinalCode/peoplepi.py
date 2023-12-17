import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Dictionary mapping IP addresses to classrooms
Rooms = {'10.192.226.31': "Classroom 1", "10.192.226.32": "Main Lecture Hall"}
Occupancy = {"Classroom 1" : 1, "Main Lecture Hall" : 0}
while True:
    data, addr = sock.recvfrom(1024)
    decoded_data = data.decode('utf-8')
    #print(decoded_data) decoded data is the message itself
    # Assuming the received data is the IP address
    #received_ip = decoded_data.strip()
    #print(received_ip)
    # Print the corresponding classroom for the received IP
   
    
    # Removing parentheses and splitting the string
    ip_address, port_number = addr

    #print("IP Address:", ip_address)
    #print("Port Number:", port_number)
    
    if ip_address in Rooms:
        classroom = Rooms[ip_address]
        Occupancy[classroom] = Occupancy[classroom] + int(decoded_data)
        print(f"Received message from {ip_address}: IP {ip_address} corresponds to {classroom}")
        print(f"{classroom} occupancy is now:" + str({Occupancy[classroom]}))
        
    else:
        print(f"Received message from {ip_address}: IP {ip_address} is not in the dictionary")
