from __future__ import absolute_import, division, print_function, unicode_literals

import math

import demo
import pi3d

import numpy as npwwwwwwwwwwwwwwwww

# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(x=150, y=150,
            background=(0.4, 0.8, 0.8, 1), frames_per_second=30)
shader = pi3d.Shader("uv_reflect")
flatsh = pi3d.Shader("uv_flat")
#############################

# Load textures
blockimg = pi3d.Texture("textures/squareblocks4.png")
roofedgeimg = pi3d.Texture("textures/roofedging.png")
roofimg = pi3d.Texture("textures/Roof.png")
greenimg = pi3d.Texture("textures/squareblocks4green.png")
ectex = pi3d.loadECfiles("textures/ecubes", "sbox", "jpg")
myecube = pi3d.EnvironmentCube(size=900.0, maptype="FACES")
myecube.set_draw_details(flatsh, ectex)

# Create elevation map
mapwidth=1000.0
mapdepth=1000.0
mapheight=0.0
floorimg = pi3d.Texture("textures/tree2.png")
bumpimg = pi3d.Texture("textures/tree1.png")
mymap = pi3d.ElevationMap(mapfile="textures/mountainsHgt2.png",
                     width=mapwidth, depth=mapdepth, height=mapheight,
                     divx=64, divy=64)
mymap.set_draw_details(shader,[floorimg, bumpimg],128.0, 0.0)
mymap.set_fog((0.3,0.25,0.1,0.8), 500.0)

#Create some random block models elsewhere on the map!
pi3d.corridor(
  150, 10, mymap, 10, 60,
  details=[shader, [blockimg, blockimg], 1.0, 0.0, 4.0, 4.0], walls="ns")

pi3d.corridor(
  150, -40, mymap,
  details=[shader, [blockimg, blockimg], 1.0, 0.0, 4.0, 4.0], walls="ew")

#CAM = pi3d.Camera(eye=(0.0,0.0,-5.0))

#this part for the movement of camera - avatar camera
rot = 0.0
tilt = 0.0
avhgt = 3.5
#x, y, z movement
xm = 0.0
zm = 0.0
ym = mymap.calcHeight(xm,zm)+avhgt

mymouse = pi3d.Mouse(restrict=False)
mymouse.start()

mykey = pi3d.Keyboard()

omx, omy = mymouse.position() #in order to get old position

CAMERA = pi3d.Camera.instance()

while DISPLAY.loop_running():
  CAMERA.reset()
  CAMERA.rotate(tilt, 0, 0)
  CAMERA.rotate(0, rot, 0)

  CAMERA.position((xm, ym, zm)) #position of the camera

  mymap.draw()
  myecube.draw()

  pi3d.SolidObject().drawall()

  #used to rotate the camera
  mx, my = mymouse.position()

  rot -= (mx-omx)*0.4
  tilt += (my-omy)*0.4
  omx=mx
  omy=my #replace with new position data

  k=mykey.read()
  if k> -1:
    if k==119: #key W
      xm -= math.sin(math.radians(rot))
      zm += math.cos(math.radians(rot))
      ym = mymap.calcHeight(xm, zm) + avhgt

    elif k==115: #key s
      xm += math.sin(math.radians(rot))
      zm -= math.cos(math.radians(rot))
      ym = mymap.calcHeight(xm, zm) + avhgt

    elif k==39: #key '
      tilt -= 2.0

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




inputs.release()
DISPLAY.destroy()
