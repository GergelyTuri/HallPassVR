'''   The Head-Fixed Mice Virtual Reality System
 
Bluetooth Version VR_OPEN.py 
This python script aims to open VR_CORRIDOR_BUILD_BLUETOOTH.py on second monitor by using a tkinter window, 
in order to pypass the difficult operation of running cmd on second monitor under Rasp pi4+ 

root.geometry("1x1+2500+200") can set the tkinter window opens at position 2500 (horizontal) 200 (vertical)
this set is decided specific for Rasp pi4+, change is necessary under different resolution 
Under Rasp pi4+ first monitor is 1920X1080
'''
from re import L
from tkinter import *
import os
import time
import json
from json.decoder import JSONDecodeError



root = Tk()

root.geometry("1x1+2500+200")

# 2022-01-05-13_06_50 test0105 [1,1,1]
# 2022-01-05-12_20_27 ssssddd [3,0,0]
# 2022-01-05-18_24_36 TEST021 120

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

geometry = "10X10+" + str(int(screen_width*0.75)) + "+200"

#root.geometry(geometry)
#print(geometry)



def CORRIDOR_OPEN():
	os.system('python3 VR_CORRIDOR_BUILD_WIRED.py')
	time.sleep(0.001)
	root.destroy()
	
	#pass


root.wait_visibility()

CORRIDOR_OPEN()
root.mainloop()


