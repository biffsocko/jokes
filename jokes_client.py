#!/usr/bin/env python3
#############################################
# TR Murphy
# Jokes_client.py
#############################################

import socket

#HOST = "10.32.67.14"   
HOST = "someserver.goes_here.com"   # Replace with the hostname or IP address of the server
#PORT = 65433  

# Create a socket object and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

###########################################################
# don't need this - but kept it commented for notes later
###########################################################
# Send a message to the server
#message = 'Hello, server!'
#sock.send(message.encode())

# Receive a response from the server
response = sock.recv(1024)
print("Received response from server:", response.decode())

# Close the socket connection
sock.close()
exit(0)
