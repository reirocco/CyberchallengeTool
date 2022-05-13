#!/usr/bin/python
from email import parser
import socket
import sys
import os
from time import sleep
from piecewiseParser import Parser


def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    while True:
        data = None
        data = s.recv(1024)
        if len(data) != 0:
            print("Received:", repr(data.decode()))
            parser = Parser()
            print("sended --> " + str(parser.parse(data.decode())))
            s.send(parser.parse(data.decode()))
        #input("Press Enter to continue...")   
        data = s.recv(1024)
        if(len(data) != 0):
            print(data.decode())

if(len(sys.argv) == 3):

    hostname = str(sys.argv[1])
    port = int(sys.argv[2])
    netcat(hostname,port)

else:
    print("Program for connecting to TCP Stream")
    print("You can use : ")
    print("./"+os.path.basename(__file__)+" <hostname> <port>")




