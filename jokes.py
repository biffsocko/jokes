#!/usr/bin/env python3
#####################################################################################
# TRMurphy
# jokes.py
#
# joke list comes from 
# https://www.kaggle.com/datasets/abhinavmoudgil95/short-jokes?resource=download
#####################################################################################

import socket
import random

DEBUG=0
jokes=[]
HOST = "0.0.0.0" # use this IP to listen on all interfaces
PORT = 65433  

with open('shortjokes.txt', 'r', newline='') as jokefile:

    for row in jokefile:
        jokes.append(row)
        

bignum=len(jokes)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while(True):
        conn, addr = s.accept()
        with conn:
            if(DEBUG > 0 ):
                print(f"Connected by {addr}")
                
            # randiomize jokes haha  funny
            # you never know what you get
            rand = random.randint(0, bignum - 1)
            conn.send(jokes[rand].encode())
            conn.close()

exit(0)
