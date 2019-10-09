#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = '127.0.0.1'
port = 200

def portscanning(port):
        if sock.connect_ex((host,port)):
                print ("port %d is open"  % (port))
        else:
                print ("port %d is closed" % (port))

portscanning(port)

