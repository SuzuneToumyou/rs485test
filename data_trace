#!/usr/bin/python3
# -*- coding: utf-8 -*

import pigpio
import time
import struct

import math
import csv

import numpy as np
import pathlib as pl

from bitarray import bitarray

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
        tPTAT = (256*readbuff[1] + readbuff[0]) #/10

        for i in range(1024):
            if i != 0:
                tmp = (256*readbuff[i*2+1] + readbuff[i*2]) #/10
                print(tmp.to_bytes(2,"little"))
        print(readbuff[2050].to_bytes(1,"little"))
        return(1)
    tP.clear()
    pi.i2c_close(h)

if __name__ == "__main__":

    return_data = senser_get()
    if return_data != 0:
        return_data = senser_get()
    time.sleep(10)
    return_data = senser_get()
