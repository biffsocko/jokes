#!/usr/bin/env python3

import socket

#HOST = "10.32.67.14"   # Replace with the hostname or IP address of the server
HOST = "research-jump-001.fcstone.com"   # Replace with the hostname or IP address of the server
#PORT = 65433  # Replace with the port number used by the server
PORT = 10000  # Replace with the port number used by the server

# Create a socket object and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Send a message to the server
#message = 'Hello, server!'
#sock.send(message.encode())

# Receive a response from the server
response = sock.recv(1024)
print("Received response from server:", response.decode())

# Close the socket connection
sock.close()
