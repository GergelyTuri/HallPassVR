#!/usr/bin/python

# --- Hongtao Cai 8/12/2021 ---
# Columbia University

# --- serialread.py ---
# This is a test file for testing Raspberry Pi getting serial input from ESP32 Using Software TX/RX 
 

from __future__ import absolute_import, division, print_function, unicode_literals

""" Example showing what can be left out. ESC to quit"""
import demo
import pi3d
import serial
import ast
import re

# --- GPIO SETUP --- 
ardSer = serial.Serial(
  port     = '/dev/ttyS0', 
  baudrate = 115200, #baudrate needs to match with baudrate in ino code
  parity   = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS, 
  timeout  = 1
)




# --- Pi3D Environment SETUP ---
DISPLAY = pi3d.Display.create(w=800, h=500, frames_per_second=10, background=(0.1, 0.1, 0.0, 0.0),
                display_config=pi3d.DISPLAY_CONFIG_HIDE_CURSOR | pi3d.DISPLAY_CONFIG_MAXIMIZED, use_glx=True)
shader = pi3d.Shader("uv_flat")
sprite = pi3d.ImageSprite("textures/PATRN.PNG", shader, w=10.0, h=10.0)
mykeys = pi3d.Keyboard()


ardStr = 'x'



while DISPLAY.loop_running():
  sprite.draw()
  k = mykeys.read()
  if k == 27:
    mykeys.close()
    DISPLAY.destroy()
    break

  # --- Reading Serial Input data ---
  # Typical Jason input: b'{"position": {"dy": -1}, "millis": 3797000}
    
  #print(ardSer.inWaiting())
  while ardSer.in_waiting:
    #print(ardSer.inWaiting())
    ardStr = ardSer.readline()
    DardStr = ardStr.decode("utf-8") #Decode data to String 
    try:
      if DardStr.find(',')!= -1: 
        dy_string = DardStr[0:DardStr.find(',')]
        dy_list = [int(d) for d in re.findall(r'-?\d+', dy_string)] #Detect all Positive/Negative data 
        #print(dy_string)
        dy = dy_list[0]
        print("dy: ",dy)
      else:
        pos = 0
    
    except:
      print("reading problem")
      ardSer.flush()

