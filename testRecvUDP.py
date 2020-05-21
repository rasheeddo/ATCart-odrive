#!/usr/bin/env python3
import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

import os
import struct
import socket
import numpy as np 
import pickle
import time
import select


# create an socket object
odrive_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# the address of this thread
MOAB = "192.168.0.200"
ODRIVE_WHEEL_PORT = 27116

odrive_sock.bind(('0.0.0.0', ODRIVE_WHEEL_PORT))
odrive_sock.setblocking(0)

## Note ##
data = None
parse_odrive_data = [None]
addr = None

while True:
	startTime = time.time()

	# we use non-blocking mode so when there is no data coming
	# it will be error, so just pass that socket.error and 
	# continue read incoming data for continuous data flow
	try:
		data, addr = odrive_sock.recvfrom(1024)
		parse_odrive_data = struct.unpack("iffffff",data)
		print("parse_odrive_data", parse_odrive_data)
	except socket.error:
		#print("socket error, don't care...")
		pass

	period = time.time() - startTime
	#print("period", period)
	