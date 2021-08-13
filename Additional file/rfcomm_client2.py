# --- 8/13/2021 Hongtao Cai ---
# Columbia University

# --- rfcomm_client2.py ---
# This file is an exmaple for bluetooth communication between Rasp Pi4 and ESP32.
# rx_and_echo() is function for receving data from ESP32. 
# digit_check() used for detecing digit at input string. 
# Use nonblocking socket in order to exit while loop when input buffer empty.
# -------------------------

from bluetooth import *
import socket
import time
import errno
import sys
from sys import getsizeof
import re

def digit_check(s):
	digits = set("0123456789")
	return bool(digits.intersection(s))

def rx_and_echo():
	while True:
		try:
			data = sock.recv(buf_size) # buf_size need to be defined based on input size
			if not data:
				print ("connection lost")
				sock.close()
				break
			else: # getting data, Typical Jason input: b'{"position": {"dy": -1}, "millis": 3797000}
				print (data)
				print (getsizeof(data))
				Ddata = data.decode("utf-8")
				if Ddata.find(',') != -1:
					dy_string = Ddata[0: Ddata.find(',')]
					print(dy_string)
					
					if digit_check(dy_string): # # Statement to avoid string doesn't have digit  eg. {, dy
						dy_list = [int(d) for d in re.findall(r'-?\d+', dy_string)] # 
						dy = dy_list[0]
						
						if (dy >1000) or (dy<-1000): # # Statement to avoid rare case reading data incorrectly 
							dy = 0
							
						print("dy: ", dy)
					else:
						pass
		except socket.error as e: # When buffer empty, break from the while loop
			if e.args[0] == errno.EWOULDBLOCK:
				#prit ("EWOULDBLOCK")
				break
			else:
				print (e)
				break            
        #print(number_count)

addr = "9C:9C:1F:C5:DF:D2"
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

service_match = find_service(address = addr)

buf_size = 41

if len(service_match) == 0:
    print("couldn't find the SampleServer service =(")
    sys.exit(0)
    
for s in range(len(service_match)):
    print("\nservice_matches: [" )
    print(service_match[s])

first_match = service_match[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

port = 1

print("connecting to \"%s\" on %s, port %s" % (name, host, port))

sock = BluetoothSocket(RFCOMM)
sock.connect((host, port))
sock.setblocking(0)
#sock.settimeout(1)

print("connected")

#input_and_send()
while True:
	#print ("outer loop")
	rx_and_echo()
	time.sleep(0.01)
	#print ("outer loop")

print("the shit finally over")

sock.close()
print("bye")
