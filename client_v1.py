#!/usr/bin/python3
# -*- coding: utf-8 -*

import time
import serial

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=None)

tmp=0
for i in range(6):
    #msg = b"0202000F5603"
    #data = bytes(msg,"utf-8")
    if(tmp==0):
        msg = b"\x02"
        tmp=1
    elif(tmp==1):
        msg = b"\x02"
        tmp=2
    elif(tmp==2):
        msg = b"\x00"
        tmp=3
    elif(tmp==3):
        msg = b"\x0F"
        tmp=4
    elif(tmp==4):
        msg = b"\x56"
        tmp=5
    elif(tmp==5):
        msg = b"\x03"
        tmp=0
    ser.write(msg)
    #print(msg)
    #time.sleep(0.01)

ser.close
