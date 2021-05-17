# Corridor_test 5/17/2021
#Hongtao Cai Columbia University 
#1) fix serial input issue
#2) delete mouse control viewing angle and keyboard control function 
#3) test out corridor length corrsponding to 2m path       2m = 4 wheel round      4x100 = 400
#4) fix GUI trash file issue
 
# --- NEED TO DO ---	
#1) Add different color corridor
#2) Input pattern array
#3) Add wall in the end 



from __future__ import absolute_import, division, print_function, unicode_literals

import math

import random 

import demo
import pi3d
import serial

import numpy as np

#the random made corridor gonna have different mark such as red, yellow, purple, blue, black)
#I will use randi function to make the length of the corridor 

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

# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(background=(0.4, 0.8, 0.8, 1), frames_per_second=120)
shader = pi3d.Shader("uv_reflect")
flatsh = pi3d.Shader("uv_flat")


# --- TEXTURE ----
blockimg = pi3d.Texture("textures/grey.jpg") #defined

blockimgR = pi3d.Texture("textures/red.jpg")
blockimgY = pi3d.Texture("textures/yellow.jpg")
blockimgP = pi3d.Texture("textures/purple.jpg")
blockimgB = pi3d.Texture("textures/blue.jpg")
blockimgBl = pi3d.Texture("textures/crop.jpg")
blockimgW = pi3d.Texture("textures/white.png")

roofedgeimg = pi3d.Texture("textures/crop.jpg") 
roofimg = pi3d.Texture("textures/crop.jpg")
greenimg = pi3d.Texture("textures/squareblocks4green.png")
ectex = [pi3d.Texture('textures/crop.jpg')]
myecube = pi3d.EnvironmentCube(size=900.0, maptype="HALFCROSS")
myecube.set_draw_details(flatsh, ectex)

#random create value
randR = random.randint(1,10) #red
randY = random.randint(1,10) #yellow
randP = random.randint(1,10) #purple
randB = random.randint(1,10) #blue
randBl = random.randint(1,10) #black

#calculated x position previous corridor center position + half previous corridor length + half corridor length 
xY = 150 + randR/2 + randY/2
xP = xY + randY/2 + randP/2

xend = xP + randP/2 
 



# Create elevation map
mapwidth=1000.0
mapdepth=1000.0
mapheight=0.0
floorimg = pi3d.Texture("textures/crop.jpg")
bumpimg = pi3d.Texture("textures/crop.jpg")
mymap = pi3d.ElevationMap(mapfile="textures/crop.jpg",
                     width=mapwidth, depth=mapdepth, height=mapheight,
                     divx=64, divy=64)
mymap.set_draw_details(shader,[floorimg, bumpimg],128.0, 0.0)
mymap.set_fog((0.3,0.25,0.1,0.8), 500.0)

#Create some random block models elsewhere on the map!
pi3d.corridor(
  200, 10, mymap, 30, 400, 20, 
  details=[shader, [blockimgB, blockimgB], 1.0, 0.0, 4.0, 4.0], walls="nso") #intial case 
  
oldxposition = 160


  

#CAM = pi3d.Camera(eye=(0.0,0.0,-5.0))

#this part for the movement of camera - avatar camera
rot = 0.0
tilt = 0.0
avhgt = 5
#x, y, z movementW
#xm = 0.0
#zm = 0.0
#ym = mymap.calcHeight(xm,zm)+avhgt

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
initialym = mymap.calcHeight(man.x(), man.z()) + avhgt/2
initialzm = 10

initialposition = pi3d.Position(initialxm, initialym, initialzm) #just in case

man.move(initialposition) 

ardStr = 'x'

global round_count

round_count = 0 

while DISPLAY.loop_running():
	print("xm value: ", man.x())
	CAMERA.reset()
	CAMERA.rotate(rot_fix, 0, 0)
	CAMERA.rotate(0, tilt_fix, 0)
  
	pos = 0
  #CAMERA.position((xm, ym, zm)) #position of the camera
	CAMERA.position((man.x(), man.y()+3, man.z()))
  
	mymap.draw()
	myecube.draw()
  
	pi3d.SolidObject.drawall() 
  
	#used to rotate the camera, data for camera rotating 
	mx, my = mymouse.position()
  
	rot -= (mx-omx)*0.4
	tilt += (my-omy)*0.4
	omx=mx
	omy=my #replace with new position data 
  
	while ardSer.in_waiting:
		ardStr = ardSer.readline()
		try:
			if ardStr.find(',')!=-1:
				print("ardStr: ", ardStr)
				#output_serial.write(str(ardStr))
        #outpit_serial.write("/n")
    #pos = int(ardStr)
				dy = ardStr[0:ardStr.find(',')]
				print("dy: ", dy)
				pos = int(dy)
			else:
				pos = 0
		except:
			print("reading problem")
			ardSer.flush()
      
	pos = pos/10
	#pos = pos+100
  
	xm = man.x()+pos
	zm = man.z() 
	ym = mymap.calcHeight(xm, zm) + avhgt/2
  
  #oldPos = pi3d.Position(oxm, oym, ozm)
  
      
      
	NewPos  = pi3d.Position(xm, ym, zm) #set the new position
	collisions = man.CollisionList(NewPos) #count for collisions it has 
  
  
	#if not, it will move to the new position
	if not collisions:
		man.move(NewPos) 
    
	elif ((collisions) and xm >= oldxposition + 15): #based on test, camera goes to xm=233 when it reaches the wall, don't know why yet, in here I used estimated length - 5 ( 150+ 75 + 10 -5) 
		man.move(initialposition)
	print("when collision. xm value is: ", xm)
    
    # --- TESTING ROUND ---
	new_postion = man.x() 
	#roundcount = new_postion - 138
	
	if (390 < new_postion < 410):
		round_count += 1
		print("rount number is: ", round_count)
		man.move(initialposition)
		output_serial.write(str(round_count).strip() + " @ " + str(new_postion).strip())
		output_serial.write('\n')
		
	else:
		round_count == round_count
		
	
    
    
#print("rount number is: ", round_count)
output_serial.close()
inputs.release()
DISPLAY.destroy()
