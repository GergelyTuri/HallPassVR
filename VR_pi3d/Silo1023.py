from __future__ import absolute_import, division, print_function, unicode_literals

import math

import random 

import demo
import pi3d
import serial

import numpy as np

#the random made corridor gonna have different mark such as red, yellow, purple, blue, black)
#I will use randi function to make the length of the corridor 

ardSer = serial.Serial('/dev/ttyUSB0', 9600, timeout=None) #get input from Arduino nano

# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(x=150, y=150,
            background=(0.4, 0.8, 0.8, 1), frames_per_second=60)
shader = pi3d.Shader("uv_reflect")
flatsh = pi3d.Shader("uv_flat")
#############################

# Load textures
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
  150, 10, mymap, 30, 20, 20, 
  details=[shader, [blockimgB, blockimgB], 1.0, 0.0, 4.0, 4.0], walls="nso") #intial case 
  
oldxposition = 160
  
'''pi3d.corridor(
  xY, 10, mymap, 30, randY, 20, 
  details=[shader, [blockimgBl, blockimgBl], 1.0, 0.0, 4.0, 4.0], walls="nso") #this is for yellow 
  
pi3d.corridor(
  xP, 10, mymap, 30, randY, 20, 
  details=[shader, [blockimgP, blockimgP], 1.0, 0.0, 4.0, 4.0], walls="nso") #this is for purple
  
pi3d.corridor(
  xend+10, 10, mymap, 30, 20, 20, 
  details=[shader, [blockimg, blockimg], 1.0, 0.0, 4.0, 4.0], walls="seo") #
  
pi3d.corridor(
  xend+10, 10, mymap, 30, 20, 20, 
  details=[shader, [blockimg, blockimg], 1.0, 0.0, 4.0, 4.0], walls="no")'''
  
for n in range (50): 
  rand = random.randint(0,1) #decide blue or black 
  lrand = random.randint(0,10) #decide the length of corridor
    
  while (lrand % 2 != 0):
    lrand = random.randint(0,10) #need to make sure distance always even 
      
  if (rand % 2 != 0):
    pi3d.corridor(
      oldxposition + lrand/2 , 10, mymap, 30, lrand, 20, 
      details=[shader, [blockimgB, blockimgB], 1.0, 0.0, 4.0, 4.0], walls="nso") #
    
  elif (rand % 2 == 0):
    pi3d.corridor(
      oldxposition + lrand/2 , 10, mymap, 30, lrand, 20, 
      details=[shader, [blockimgR, blockimgR], 1.0, 0.0, 4.0, 4.0], walls="nso") #
    
  oldxposition = oldxposition + lrand 
  
pi3d.corridor(
  oldxposition+10, 10, mymap, 30, 20, 20, 
  details=[shader, [blockimgB, blockimgB], 1.0, 0.0, 4.0, 4.0], walls="so") #
  
pi3d.corridor(
  oldxposition+10, 10, mymap, 30, 20, 20, 
  details=[shader, [blockimgB, blockimgB], 1.0, 0.0, 4.0, 4.0], walls="no")
  

  

#CAM = pi3d.Camera(eye=(0.0,0.0,-5.0))

#this part for the movement of camera - avatar camera
rot = 0.0
tilt = 0.0
avhgt = 5
#x, y, z movementW
#xm = 0.0
#zm = 0.0
#ym = mymap.calcHeight(xm,zm)+avhgt

mymouse = pi3d.Mouse(restrict=False)
mymouse.start()

mykey = pi3d.Keyboard()

omx, omy = mymouse.position() #in order to get old position

CAMERA = pi3d.Camera.instance()

#create the soliod object
man = pi3d.SolidObject("man", pi3d.Size(0.5,avhgt,0.5), pi3d.Position(0, (mymap.calcHeight(5,5)+ avhgt/2),0),1)

#just for verify
ardStr = ardSer.readline()
pos = int(ardStr) #pos = pos 


#this is object inital position 
initialxm = 138 #center x position - half of the length +1 this case: 150 - 150/2 +1, when changing to serial input position, data should be changed to (pos+138)
initialym = mymap.calcHeight(man.x(), man.z()) + avhgt/2
initialzm = 10

initialposition = pi3d.Position(initialxm, initialym, initialzm) #just in case

man.move(initialposition) 

while DISPLAY.loop_running():
  CAMERA.reset()
  CAMERA.rotate(tilt, 0, 0)
  CAMERA.rotate(0, rot, 0)
  
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
  
  #store the old position data 
  #oxm = man.x()
  #oym = man.y()
  #ozm = man.z()
  
  #xm=man.x() #update new xm position 
  #ym=man.y() 
  #zm=man.z()
  
  #get position
  ardStr = ardSer.readline()
  pos = int(ardStr) #pos = pos 
  
  xm = pos+138
  zm = man.z()
  ym = mymap.calcHeight(xm, zm) + avhgt/2
  
  #oldPos = pi3d.Position(oxm, oym, ozm)
  
  k=mykey.read()
  if k> -1:
    '''if k==119: #key w
      xm -= math.sin(math.radians(rot)) #first xm value comes out of the loop 
      zm += math.cos(math.radians(rot))
      ym = mymap.calcHeight(xm, zm) + avhgt/2
    
    elif k==115: #key s
      xm += math.sin(math.radians(rot))
      zm -= math.cos(math.radians(rot))
      ym = mymap.calcHeight(xm, zm) + avhgt/2'''
    
    if k==39: #key '
      tilt -= 2.0
      #print "in here" 
    
    elif k==47: #key /
      tilt += 2.0
    
    elif k==97: #key A
      rot -= 2
    
    elif k==100:
      rot +=12
    
    elif k==27:
      mykey.close()
      mymouse.stop()
      DISPLAY.stop()
      break
      
  NewPos  = pi3d.Position(xm, ym, zm) #set the new position
  collisions = man.CollisionList(NewPos) #count for collisions it has 
  
  
  #if not, it will move to the new position
  if not collisions:
    man.move(NewPos) 
    
  elif ((collisions) and xm >= oldxposition + 15): #based on test, camera goes to xm=233 when it reaches the wall, don't know why yet, in here I used estimated length - 5 ( 150+ 75 + 10 -5) 
    man.move(initialposition)
    
    
        
inputs.release()
DISPLAY.destroy()
