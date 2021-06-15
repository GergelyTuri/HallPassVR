#--- Gyroscope-convert ---
#Hongtao Cai Columbia University
#This is just to show how to process data

from __future__ import absolute_import, division, print_function, unicode_literals
import math
import random 
import demo
import pi3d
import numpy as np
import time

readfile = open("readresult.txt", "r")

#line_read = readfile.readline()

#print(line_read)


DISPLAY = pi3d.Display.create(x=150, y=150,
            background=(0.4, 0.8, 0.8, 1), frames_per_second=60)
shader = pi3d.Shader("uv_reflect")
flatsh = pi3d.Shader("uv_flat")

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

read_finish_signal = 0

while DISPLAY.loop_running():
	#print("running")
	
	print(read_finish_signal)

	if read_finish_signal == 0:
		line_read = readfile.readline()
		
		if not line_read:
			read_finish_signal = 1
			#print ("in here")		
		else:
			print("just for check: ", line_read)
			
			data_read = [float(x) for x in line_read.split('\t')]
			
			print(data_read)
		
			
			
			
			print(data_read[0])
				
			
	elif read_finish_signal == 1:
		DISPLAY.destroy()


