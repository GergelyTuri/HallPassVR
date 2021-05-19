# Corridor_test 5/18&19/2021
#Hongtao Cai Columbia University
#1) Use array to read pattern
#2) prototype for corridor


# NEED TO DO 
#1) Fix the segment fault
#2) Combine with GUI interface
#3) Fix rot issue for pattern

from __future__ import absolute_import, division, print_function, unicode_literals

import math

import random 

import demo
import pi3d
import serial

import numpy as np
import os 

print("in here, function start")

# --- SET UP ---
ardSer = serial.Serial(
  port='/dev/ttyS0', 
  baudrate = 38400, #9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS, 
  timeout=1
)

output_serial = open("serial_output.txt", "w")
rot_fix = -100
tilt_fix = -100
corridor_start = 16

# --- test --- 
display_array = [1,1,1,3,1,1,1,3,1,1,1,3] 


# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(background=(0, 0, 0, 0), frames_per_second=120)
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

  file_list = os.listdir("textures/image/")
  #print("file_list: ", str(file_list[0]))
  
  string_add = 'textures/image/'
  
  pattern_list = [string_add + x for x in file_list]
  #print("pattern_list: ", str(pattern_list[0]))
  
  pattern_count = [num for num in range(0, len(file_list))]
  #print("pattern_count: ", str(pattern_count))
 
def corridor_build():
	global display_array
	global corridor_start
	
	#blockimg = pi3d.Texture("textures/crop.jpg")
		
	for i in display_array:
		print("i is: ", i)
		pattern_name = pattern_list[display_array[i]]
		print("pattern name is: ", pattern_name)
		blockimg = pi3d.Texture("textures/crop.jpg")
		pattern = pi3d.Texture(pattern_name)
		
		pi3d.corridor(
		corridor_start, 10, mymap, 50, 33, 30, 
		details=[flatsh, [pattern], 50, 0.0, 1.0, 1.0], walls="nso") #
		
		corridor_start += 33
		
		
		
	
  
  
  
  
# --- FUNCTION ---  
pattern_get()


#print("pattern_list: ", str(pattern_list))
#print("pattern_count: ", str(pattern_count))
#print("test pattern name: ", str(pattern_list[display_array[0]]))

# --- TEXTURE ----
blockimg = pi3d.Texture("textures/crop.jpg") #defined
#print(blockimg)
pattern1 = pi3d.Texture(pattern_list[display_array[0]])
pattern2 = pi3d.Texture(pattern_list[display_array[1]])
pattern3 = pi3d.Texture(pattern_list[display_array[2]])
pattern4 = pi3d.Texture(pattern_list[display_array[3]])

pattern5 = pi3d.Texture(pattern_list[display_array[4]])
pattern6 = pi3d.Texture(pattern_list[display_array[5]])
pattern7 = pi3d.Texture(pattern_list[display_array[6]])
pattern8 = pi3d.Texture(pattern_list[display_array[7]])

pattern9 = pi3d.Texture(pattern_list[display_array[8]])
pattern10 = pi3d.Texture(pattern_list[display_array[9]])
pattern11 = pi3d.Texture(pattern_list[display_array[10]])
pattern12 = pi3d.Texture(pattern_list[display_array[11]])



roofedgeimg = pi3d.Texture("textures/crop.jpg") 
roofimg = pi3d.Texture("textures/crop.jpg")
ectex = [pi3d.Texture('textures/crop.jpg')]
bumpimg = pi3d.Texture("textures/white.jpg")
endwall = pi3d.Texture("textures/hornbeam2.png")

myecube = pi3d.EnvironmentCube(size=1200.0, maptype="HALFCROSS")
myecube.set_draw_details(flatsh, ectex)

# Create elevation map
mapwidth=1000.0
mapdepth=1000.0
mapheight=0.0

mymap = pi3d.ElevationMap(mapfile="textures/white.jpg",
                     width=mapwidth, depth=mapdepth, height=mapheight,
                     divx=64, divy=64)
                     
mymap.set_draw_details(flatsh,[bumpimg], 0, 0.0)
#mymap.set_fog((0.3,0.25,0.1,0.8), 500.0)

#Create some random block models elsewhere on the map!


print("in here, check seg fault")
pi3d.corridor(
  16, 10, mymap, 50, 32,  20, 
  details=[flatsh, [pattern1], 1, 1, 1, 1], walls="nso") #intial case
  
pi3d.corridor(
  48, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern2], 1, 0.0, 1.0, 1.0], walls="nso") # 
  
pi3d.corridor(
  80, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern3], 1, 0.0, 1.0, 1.0], walls="nso") #
  
pi3d.corridor(
  112, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern4], 50, 0.0, 1.0, 1.0], walls="nso") #intial case
  
  
  
  
  
  
  
pi3d.corridor(
  144, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern5], 50, 0.0, 1.0, 1.0], walls="nso") # 
  
pi3d.corridor(
  176, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern6], 50, 0.0, 1.0, 1.0], walls="nso") #
  
  
pi3d.corridor(
  208, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern7], 50, 0.0, 1.0, 1.0], walls="nso") # 
  
pi3d.corridor(
  240, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern8], 50, 0.0, 1.0, 1.0], walls="nso") #






pi3d.corridor(
  272, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern9], 50, 0.0, 1.0, 1.0], walls="nso") # 
  
pi3d.corridor(
  304, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern10], 50, 0.0, 1.0, 1.0], walls="nso") #
  
  
pi3d.corridor(
  336, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern11], 50, 0.0, 1.0, 1.0], walls="nso") # 
  
pi3d.corridor(
  368, 10, mymap, 50, 32, 20, 
  details=[flatsh, [pattern12], 50, 0.0, 1.0, 1.0], walls="nso")
  
  
  
pi3d.corridor(
  385, 10, mymap, 50, 1, 20, 
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

mykey = pi3d.Keyboard()

omx, omy = mymouse.position() #in order to get old position

CAMERA = pi3d.Camera.instance()

#create the soliod object
man = pi3d.SolidObject("man", pi3d.Size(0.5,avhgt,0.5), pi3d.Position(0, (mymap.calcHeight(5,5)+ avhgt/2),0),1)

#just for verify 


#this is object inital position 
initialxm = 0 #center x position - half of the length +1 this case: 150 - 150/2 +1, when changing to serial input position, data should be changed to (pos+138)
initialym = avhgt/2
initialzm = 10

initialposition = pi3d.Position(initialxm, initialym, initialzm) #just in case

man.move(initialposition) 

ardStr = 'x'

global round_count

round_count = 0 

pi3d.SolidObject.drawall()

while DISPLAY.loop_running():
	print("xm value: ", man.x())
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
  
	while ardSer.in_waiting:
		ardStr = ardSer.readline()
		try:
			if ardStr.find(',')!=-1:
				#print("ardStr: ", ardStr)
				#output_serial.write(str(ardStr))
				#outpit_serial.write("/n")
				#pos = int(ardStr)
				dy = ardStr[0:ardStr.find(',')]
				#print("dy: ", dy)
				pos = int(dy)
			else:
				pos = 0
		except:
			print("reading problem")
			ardSer.flush()
      
	pos = pos/10
      
	# --- position update ---
	xm = man.x()+pos
	zm = man.z() 
	ym = mymap.calcHeight(xm, zm) + avhgt/2

	NewPos  = pi3d.Position(xm, ym, zm) #set the new position
	collisions = man.CollisionList(NewPos) #count for collisions it has 
  
  
	#if not, it will move to the new position
	if not collisions:
		man.move(NewPos) 
        
	# --- TESTING ROUND ---
	new_postion = man.x() 
	#roundcount = new_postion - 138
	
	if (355 < new_postion < 380):
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
inputs.release()
DISPLAY.destroy()
