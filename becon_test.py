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
            print(tmp, ": ", recv_data.hex())
            tmp=tmp+1
