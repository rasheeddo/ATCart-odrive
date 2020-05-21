#!/usr/bin/env python3

import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

import socket
import struct
import time
import math as m
import numpy as np
#import matplotlib.pyplot as plt


MOAB_COMPUTER = "192.168.8.20"
MOAB_PORT = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 0))



def testSendInt(int1, int2):
    udpPacket = struct.pack('HH', int1, int2)
    s.sendto(udpPacket, (MOAB_COMPUTER, MOAB_PORT))

def testSendFloat(float1, float2):
    udpPacket = struct.pack('ff', float1, float2)
    s.sendto(udpPacket, (MOAB_COMPUTER, MOAB_PORT))

def sendRPMOdrivePacket(rpmR,rpmL):
	udpPacket = struct.pack('fff',2,rpmR,rpmL)
	s.sendto(udpPacket,(MOAB_COMPUTER,MOAB_PORT))

def sendDEGOdrivePacket(degR,degL):
	udpPacket = struct.pack('fff',3,degR,degL)
	s.sendto(udpPacket,(MOAB_COMPUTER,MOAB_PORT))

#print(sendOut)
while True:
	
	#testSendFloat(40.5,80.5)
	sendRPMOdrivePacket(100.0,30.0)
	#sendDEGOdrivePacket(90.0,180.0)
	time.sleep(0.1)
