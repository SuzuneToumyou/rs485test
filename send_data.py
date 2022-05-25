#!/usr/bin/python3
# -*- coding: utf-8 -*

import pigpio
import time
import struct

import serial

import math
import csv

import numpy as np
import pathlib as pl

from bitarray import bitarray

s_code = b'\x02'
s_ID = b'\x00'

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=None)

def senser_get():
    pi = pigpio.pi()
    addr = 0x0a

    h = pi.i2c_open(1,addr)
    pi.i2c_write_device(h, [0x4d])
    time.sleep(2)
    count, result = pi.i2c_read_device(h,2051)
    #count, result = pi.i2c_read_device(h,1024)
    time.sleep(2)
    
    pi.i2c_close(h)
    
    tP = []
    if count <= 0: #device_error
        return (0)
    else:
        #file_name="./outputdata.dat"
        #fout= open(file_name,"wb")

        readbuff = bytes(result)
        #print(result)
        #fout.write(readbuff)

        #hedder
        #tPTAT = (256*readbuff[1] + readbuff[0]) #/10

        msg = b"\x02"
        ser.write(msg)
        ser.write(s_code)
        ser.write(s_ID)

        #time.sleep(5)
        tPTAT = (256*readbuff[1] + readbuff[0])
        msg = tPTAT.to_bytes(2,"little")
        ser.write(msg)

        for i in range(1024):
            #if i != 0:
            tmp = (256*readbuff[i*2+1] + readbuff[i*2]) #/10
            #print(tmp.to_bytes(2,"little"))
            msg = tmp.to_bytes(2,"little")
            ser.write(msg)
            #time.sleep(1)
        #print(readbuff[2050].to_bytes(1,"little"))
        msg = readbuff[2050].to_bytes(1,"little")
        ser.write(msg)
        time.sleep(5)
        msg = b"\x03"
        ser.write(msg)
        return(1)
    tP.clear()
    pi.i2c_close(h)

if __name__ == "__main__":

    return_data = senser_get()
    if return_data != 0:
        return_data = senser_get()
    time.sleep(10)
    return_data = senser_get()
