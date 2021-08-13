# --- Hongtao Cai 8/12/2021 ---
# Columbia University

# --- serialread_blz.py ---
# This is a test file for testing Raspberry Pi getting serial input from ESP32 Using Bluetooth with Pi3D VR Environment Built
# Details about Bluetooth Connection can be found in rfcomm_client2.py 
# Use ESC to stop running

from __future__ import absolute_import, division, print_function, unicode_literals

""" Example showing what can be left out. ESC to quit"""
import demo
import pi3d
import serial
from bluetooth import *
import sys
from sys import getsizeof
import re
import socket
import time
import errno

# --- Pi3D DISPLAY SETUP ---
DISPLAY = pi3d.Display.create(w=800, h=500, frames_per_second=10, background=(0.1, 0.1, 0.0, 0.0),
                display_config=pi3d.DISPLAY_CONFIG_HIDE_CURSOR | pi3d.DISPLAY_CONFIG_MAXIMIZED, use_glx=True)
shader  = pi3d.Shader("uv_flat")
sprite  = pi3d.ImageSprite("textures/PATRN.PNG", shader, w=10.0, h=10.0)
mykeys  = pi3d.Keyboard()

ardStr  = 'x'

# --- SOCKET SETUP ---
addr = "9C:9C:1F:C5:DF:D2" # Bluetooth Address Change with Device 
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

service_match = find_service(address = addr)

buf_size = 40 #Buffer Size, Need to Change with Input Size

if len(service_match) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)
    
for s in range(len(service_match)):
    print("\nservice_matches: [" )
    print(service_match[s])

first_match = service_match[0]
port 		= first_match["port"]
name 		= first_match["name"]
host 		= first_match["host"]

port = 1

print("connecting to \"%s\" on %s, port %s" % (name, host, port))

sock = BluetoothSocket(RFCOMM)
sock.connect((host, port))
sock.setblocking(0) # Select Socket to be nonBlocking 

global dy
dy = 0


print("connected")

# --- FUNCTION ---
def digit_check(s):
	digits = set("0123456789")
	return bool(digits.intersection(s))

def rx_and_echo():
	while True:
		try:
			data = sock.recv(buf_size)
			if not data:
				print ("connection lost")
				sock.close()
				break
			else:
				#print (data)
				#print (getsizeof(data))
				Ddata = data.decode("utf-8")
				if Ddata.find(',') != -1:
					dy_string = Ddata[0: Ddata.find(',')]
					#print(dy_string)
					
					if digit_check(dy_string): # Statement to avoid string doesn't have digit  eg. {, dy
						dy_list = [int(d) for d in re.findall(r'-?\d+', dy_string)] 
						dy = dy_list[0]
						
						if (dy >1000) or (dy<-1000): # Statement to avoid rare case reading data incorrectly 
							dy = 0
							
						print("dy: ", dy)
					else:
						pass
		except socket.error as e: # When no data received, break While loop
			if e.args[0] == errno.EWOULDBLOCK:
				#prit ("EWOULDBLOCK")
				break
			else:
				print (e)
				break            
        #print(number_count)
            
#rx_and_echo()


while DISPLAY.loop_running():
  #print("in here")
  sprite.draw()
  k = mykeys.read()
  if k == 27:
    mykeys.close()
    DISPLAY.destroy()
    break
    
  rx_and_echo()
  
        
    
      
          
    

      
