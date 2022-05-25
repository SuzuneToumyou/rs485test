#!/usr/bin/python3
# -*- coding: utf-8 -*


import serial
import struct


ser = serial.Serial(
      port = "/dev/ttyUSB0",
      baudrate = 19200,
      parity = serial.PARITY_NONE,
      bytesize = serial.EIGHTBITS,
      stopbits = serial.STOPBITS_ONE,
      #timeout = None,
      #xonxoff = 0,
      #rtscts = 0,
      )

tmp = 0
s_code = b'\x02'
s_ID = b'\x00'

while True:
      if ser.in_waiting > 0:
            recv_data = ser.read(1)
            if(tmp==0 and recv_data==b'\x02'):
                tmp=1
                print("packet start!")
            elif(tmp==1 and recv_data==s_code):
                tmp=2
                print("s_code OK:" + recv_data.hex())
            elif(tmp==2 and recv_data==s_ID):
                tmp=3
                print("s_ID OK:" + recv_data.hex())
            elif(tmp==3 and recv_data==b'\x0F'):
                tmp=4
                print("sent packet!:" + recv_data.hex())
            elif(tmp==4):
                tmp=5
            elif(tmp==5 and recv_data==b'\x03'):
                tmp=0
                print("packet end!")
