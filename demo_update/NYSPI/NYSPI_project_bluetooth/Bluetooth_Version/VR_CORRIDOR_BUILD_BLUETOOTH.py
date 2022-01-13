# --- Corridor Interface 8/12/2021 ---
#Hongtao Cai - Columbia University 
#1) Fix Bugs

from __future__ import absolute_import, division, print_function, unicode_literals
import math
import random 
#import demo
import pi3d
import serial

import numpy as np
import os 
from bluetooth import *
import sys
from sys import getsizeof
import re
import socket
import time
import errno

import json
from json.decoder import JSONDecodeError

import time

print("in here, function start, test 6/1")

# --- SET UP ---
addr = "9C:9C:1F:C5:DF:D2"
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

service_match = find_service(address = addr)

buf_size = 40

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

global dy
dy = 0





output_serial = open("serial_output.txt", "w")
rot_fix = -90
tilt_fix = -90
corridor_start = 16
corridor_length_default = 192


winw, winh, bord = 1200, 700, 0

#384 - 2m


#print("corridor length is: ", corridor_length)
#print("corridor length avg is: ", corridor_length_avg)
#print("corridor start at: ", corridor_start)

global ELEMENT_LIST 
ELEMENT_LIST = []

global ELEMENT_CONVERT_TABLE
ELEMENT_CONVERT_TABLE = {"NAME":[], "DECODE_NAME":[]}

global CODENAME_LIST
CODENAME_LIST = []

global FLOOR_IMG
global CEILING_IMG
global LEN_PATH

global GOLDEN_PATH_NAME_IMG
global REF_PATH_NUM_DIG
    
def DECODE_INITIAL():
    
    global ELEMENT_LIST
    global ELEMENT_CONVERT_TABLE
    
    extensions = [".jpg", ".png" ]
    ELEMENT_LIST = []
    ELEMENT_LIST = [f for f in os.listdir('image/ELEMENT') 
            if os.path.splitext(f)[1] in extensions]

    const = -1
    const_loop = -2
    #global CODENAME_LIST
    for element in ELEMENT_LIST:
        ELEMENT_CONVERT_TABLE["NAME"].append(element)
    
        element = element[:element.index('.')]
        CODE_NAME = element[0] + element[const]
    
        while CODE_NAME in CODENAME_LIST:
            CODE_NAME = element[0] + element[const_loop]
            const_loop = const_loop -1 
        #print(CODE_NAME)
        
        CODENAME_LIST.append(CODE_NAME)
        ELEMENT_CONVERT_TABLE["DECODE_NAME"].append(CODE_NAME)
        	
    #print(ELEMENT_LIST)
    
    #print(ELEMENT_CONVERT_TABLE['DECODE_NAME'])
    
def FINAL_SELF_CHECK():
    global GOLDEN_PATH_NAME_IMG
    global FLOOR_IMG
    global CEILING_IMG
    global LEN_PATH
    global REF_PATH_NUM_DIG
    
    PATH_DICT = {}
    
    PATH_VALUE_DICT = {}
    INPUT_DICT = {}
    PATTERN_1 = {}
    PATTERN_2 = {}
    PATTERN_3 = {}
    
    REF_PATH_DECODE_INDEX = []
    GOLDEN_PATH_DECODE_INDEX = []
    
    REF_PATH_NAME_IMG = []
    GOLDEN_PATH_NAME_IMG = []
    
    REF_PATH_NUM_DIG = []
    GOLDEN_PATH_NUM_DIG = []
    
    #global ELEMENT_CONVERT_TABLE
    #global CODENAME_LIST
    
    
     
    transpt = open('trash.txt', 'r')
    
    PATH_NAME = transpt.readline()
    
    print("path name is: ", PATH_NAME)
    
    NOTE = [0, 0, 0]
    transpt.close()
    
    with open('image/HIST_PATH/PATH.json', 'r') as f:
        try:
            PATH_DICT = json.loads(f.read())
            
            if PATH_DICT:
                #print (PATH_DICT)
                if (PATH_NAME in PATH_DICT):
                    PATH_VALUE_DICT = PATH_DICT[PATH_NAME]
                    NOTE = PATH_VALUE_DICT['Note']
                    INPUT_DICT = PATH_VALUE_DICT['INPUT']
                    
                    FLOOR_IMG = INPUT_DICT['Floor']
                    CEILING_IMG = INPUT_DICT['Ceiling']
                    LEN_PATH = INPUT_DICT['Path Length']
                    
                    print('floor img is :', FLOOR_IMG)
                    print('Ceiling img is :', CEILING_IMG)
                    print("path length is :", LEN_PATH)
                    #print(list(PATH_VALUE_DICT.values())[0]['ELEMENT_DECODE_INDEX'])
                    
                    
                else:
                   print("ERROR is either JSON file or PATH_NAME") 
        except JSONDecodeError:
            print("ERROR exists in PATH_PROCESS reading PATH JSON")
            
    #print(NOTE)  
      
    
    if (NOTE == [3,0,0]):
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = PATTERN_1
        PATTERN_3 = PATTERN_2
        #print("PATTERN for [3,0,0] is :", PATTERN_1) #read the only pattern
    elif (NOTE == [2, 0, 1]): #[2,0,1] = [0,2,1]
        #print(PATH_VALUE_DICT)
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = PATTERN_1
        PATTERN_3 = list(PATH_VALUE_DICT.values())[1]
        
    elif (NOTE == [1,2,0]): #[1,2,0] = [0,1,2]
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = list(PATH_VALUE_DICT.values())[1]
        PATTERN_3 = PATTERN_2
        
    elif (NOTE == [1,1,1]):
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = list(PATH_VALUE_DICT.values())[1]
        PATTERN_3 = list(PATH_VALUE_DICT.values())[2]
        
    elif (NOTE == [2,1,0]):
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = list(PATH_VALUE_DICT.values())[1]
        PATTERN_3 = PATTERN_1       
        
    REF_PATH_DECODE_INDEX[0:3] = PATTERN_1['ELEMENT_DECODE_INDEX']
    REF_PATH_DECODE_INDEX[4:7] = PATTERN_2['ELEMENT_DECODE_INDEX']
    REF_PATH_DECODE_INDEX[8:11] = PATTERN_3['ELEMENT_DECODE_INDEX']
    
    REF_PATH_NAME_IMG[0:3] = PATTERN_1['ELEMENT_NAME_IMG']
    REF_PATH_NAME_IMG[4:7] = PATTERN_2['ELEMENT_NAME_IMG']
    REF_PATH_NAME_IMG[8:11] = PATTERN_3['ELEMENT_NAME_IMG']
    
    REF_PATH_NUM_DIG[0:3] =  PATTERN_1['ELEMENT_NUM_DIG']
    REF_PATH_NUM_DIG[4:7] =  PATTERN_2['ELEMENT_NUM_DIG']
    REF_PATH_NUM_DIG[8:11] =  PATTERN_3['ELEMENT_NUM_DIG']
    
    
    
    
    print(REF_PATH_DECODE_INDEX)
    print(REF_PATH_NAME_IMG)
    print(REF_PATH_NUM_DIG)
    #print(ELEMENT_CONVERT_TABLE)
    
    for element in REF_PATH_NUM_DIG:
        GOLDEN_PATH_DECODE_INDEX.append(ELEMENT_CONVERT_TABLE['DECODE_NAME'][element])
        #print("index :", GOLDEN_PATH_DECODE_INDEX)
        GOLDEN_PATH_NAME_IMG.append(ELEMENT_CONVERT_TABLE['NAME'][element])
        #print(ELEMENT_CONVERT_TABLE['NAME'][element])
        
        
    print(GOLDEN_PATH_DECODE_INDEX)
    print(GOLDEN_PATH_NAME_IMG)
    

    if ((GOLDEN_PATH_DECODE_INDEX == REF_PATH_DECODE_INDEX) 
        and (GOLDEN_PATH_NAME_IMG == REF_PATH_NAME_IMG)):
        print('CORRIDOR SELF CHECK PASSED')
    else:
        print("ERROR EXIST in VR CORRIDOR INITIAL SELF CHECK")
	
	
	

def read_data():
  global display_array
  global display_list
  global display_array_length
  
  display_list = [int(x) for x in display_array.split()]
  #print("the display list is: ", display_list)
  #print("the display length is: ", display_array_length)


# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(w=winw, h=winh - bord, far=4000.0,background=(0, 0, 0, 0), frames_per_second=120)
shader = pi3d.Shader("uv_reflect")
flatsh = pi3d.Shader("uv_flat")
bumpsh = pi3d.Shader("uv_bump")

global file_list
global pattern_list
global pattern_count


def pattern_get():
  
  global file_list
  global pattern_list
  global pattern_count


  #print("file_list: ", str(file_list[0]))
  string_dir = 'image/ELEMENT/'
  extensions = [".jpg"]
  file_list  = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]
  
  
  pattern_list = [string_dir + x for x in file_list]
  #print("pattern_list: ", str(pattern_list[0]))
  
  pattern_count = [num for num in range(0, len(file_list))]
  #print("pattern_count: ", str(pattern_count))
  
def digit_check(s):
	digits = set("0123456789")
	return bool(digits.intersection(s))

def rx_and_echo():
	global dy
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
					
					if digit_check(dy_string):
						dy_list = [int(d) for d in re.findall(r'-?\d+', dy_string)]
						dy = dy_list[0]
						
						if (dy >1000) or (dy<-1000):
							dy = 0
							
						print("dy: ", dy)
					else:
						pass
		except socket.error as e:
			if e.args[0] == errno.EWOULDBLOCK:
				#prit ("EWOULDBLOCK")
				#dy = 0
				break
			else:
				print (e)
				break            
        #print(number_count)
 
			      
# --- FUNCTION ---  
pattern_get()
#read_data()
DECODE_INITIAL()
FINAL_SELF_CHECK()

corridor_length     = corridor_length_default * int(LEN_PATH)
corridor_length_avg = corridor_length/12
corridor_start      = corridor_length_avg/2

cubesize = 400 * int(LEN_PATH)
mapwidth=500 * int(LEN_PATH)
mapdepth=500 * int(LEN_PATH)

# --- TEXTURE ----
blockimg = pi3d.Texture("../textures/crop.jpg") #defined
#print(blockimg)

VR_PATTERN = []

for element in REF_PATH_NUM_DIG:
	VR_PATTERN.append(pi3d.Texture(pattern_list[element]))


#roofedgeimg = pi3d.Texture("../textures/crop.jpg")
ceiling_tex_path = "image/ELEMENT/"+ CEILING_IMG 
ceiling_tex     = pi3d.Texture(ceiling_tex_path)
#ectex       = [pi3d.Texture('../textures/crop.jpg')]
floor_tex_path = "image/ELEMENT/"+ FLOOR_IMG 
floor_tex     = pi3d.Texture(floor_tex_path)
endwall     = pi3d.Texture("../textures/stop.jpeg")

myecube     = pi3d.EnvironmentCube(size=cubesize, maptype="HALFCROSS")
myecube.set_draw_details(flatsh, [ceiling_tex], 1, 0.0, 1.0, 1.0) #ceiling 

# Create elevation map

mapheight=0.0

mymap = pi3d.ElevationMap(mapfile="../textures/white.png",
                     width=mapwidth, depth=mapdepth, height=mapheight,
                     divx=64, divy=64)
                     
mymap.set_draw_details(flatsh, [floor_tex], 50, 50) 
#mymap.set_fog((0.3,0.25,0.1,0.8), 500.0)

#Create some random block models elsewhere on the map!



  
# Create an infinity corridor.
for i, pattern in enumerate(VR_PATTERN):
	pi3d.corridor(
		corridor_start + corridor_length_avg * i,
		10, mymap, 50, corridor_length_avg, 30,
		details=[flatsh, [pattern], 1, 0.0, 1.0, 1.0], walls="nso"
            )
  
#draw a wall
pi3d.corridor(
  corridor_length+1, 10, mymap, 50, 1, 30, 
  details=[flatsh, [endwall], 50, 0.0, 1.0, 1.0], walls="w")  


#corridor_build()

oldxposition = 160

print("in here, check seg fault2")
  

#CAM = pi3d.Camera(eye=(0.0,0.0,-5.0))

#this part for the movement of camera - avatar camera
rot = 0.0
tilt = 0.0
avhgt = 20

mymouse = pi3d.Mouse(restrict=True)
mymouse.start()
mykeys = pi3d.Keyboard()

mykey = pi3d.Keyboard()

omx, omy = mymouse.position() #in order to get old position

CAMERA = pi3d.Camera.instance()

#create the soliod object
man = pi3d.SolidObject("man", pi3d.Size(0.5,avhgt,0.5), pi3d.Position(0, (mymap.calcHeight(5,5)+ avhgt/2),0),1)

#just for verify 


#this is object inital position 
initialxm = -15 #center x position - half of the length +1 this case: 150 - 150/2 +1, when changing to serial input position, data should be changed to (pos+138)
initialym = avhgt/2
initialzm = 9

initialposition = pi3d.Position(initialxm, initialym, initialzm) #just in case

man.move(initialposition) 

ardStr = 'x'

global round_count

round_count = 0 

pi3d.SolidObject.drawall()

while DISPLAY.loop_running():
	#print("xm value: ", man.x())
	CAMERA.reset()
	CAMERA.rotate(rot_fix, 0, 0)
	CAMERA.rotate(0, tilt_fix, 0)
	#CAMERA.position((xm, ym, zm))
  
	pos = 0

	CAMERA.position((man.x(), man.y()+3, man.z()))
	
	#print("in here, check seg fault3")
	myecube.draw()
	mymap.draw()
	#print("in here, check seg fault4")
	pi3d.SolidObject.drawall()
	 
	#print("in here, check seg fault5")
	
	#used to rotate the camera, data for camera rotating 
	mx, my = mymouse.position()
	#print(ardSer.in_waiting)
	
	rx_and_echo()
      
	pos = dy/10
	
	#pos = 1
      
	# --- position update ---
	
	xm = man.x()+pos
	if xm < -15:
	  xm = -15
	  
	zm = man.z() 
	ym = mymap.calcHeight(xm, zm) + avhgt/2

	NewPos  = pi3d.Position(xm, ym, zm) #set the new position
	collisions = man.CollisionList(NewPos) #count for collisions it has 
	
	
	k = mykeys.read()
	if k >-1:
	  if k==10:   #key RETURN
	    mc = 0
	  elif k==27:  #Escape key
	    mykeys.close()
	    mymouse.stop()
	    DISPLAY.stop()
	    ardSer.close()
	    break
	else:
	    pass
  
  
	#if not, it will move to the new position
	if not collisions:
		man.move(NewPos) 
        
	# --- TESTING ROUND ---
	new_postion = man.x() 
	#roundcount = new_postion - 138
	
	if (corridor_length-20 < new_postion < corridor_length+10):
		round_count += 1
		#print("rount number is: ", round_count)
		man.move(initialposition)
		#CAMERA.position((xm, ym, zm))
		output_serial.write(str(round_count).strip() + " @ " + str(new_postion).strip())
		output_serial.write('\n')
		
	else:
		round_count == round_count
		
	
    
    
#print("rount number is: ", round_count)
output_serial.close()
#inputs.release()
DISPLAY.destroy()

