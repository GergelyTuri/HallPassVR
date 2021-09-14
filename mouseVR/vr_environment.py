# --- Corridor Interface 8/12/2021 ---
# Hongtao Cai - Columbia University
# 1) Fix Bugs

from __future__ import absolute_import, division, print_function, unicode_literals
import math
import random
# import demo
import pi3d
import serial

import numpy as np
import os
import re

print("in here, function start, test 6/1")

# --- SET UP ---
try:
    ardSer = serial.Serial(
        port='/dev/ttyS0',
        baudrate=115200,  # 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
except OSError as err:
    print(err)
    ardSer = None

output_serial = open("tmp/serial_output.txt", "w")
rot_fix = -90
tilt_fix = -90
corridor_start = 16
corridor_length_default = 192

winw, winh, bord = 1200, 700, 0

# 384 - 2m

# --- test ---
share = open("tmp/path.txt", "r")

display_array = share.readline()
display_array_length = share.readline()
display_list = []

share.close()

corridor_length = corridor_length_default * int(display_array_length)
corridor_length_avg = corridor_length / 12
corridor_start = corridor_length_avg / 2


# print("corridor length is: ", corridor_length)
# print("corridor length avg is: ", corridor_length_avg)
# print("corridor start at: ", corridor_start)

def read_data():
    global display_array
    global display_list
    global display_array_length

    display_list = [int(x) for x in display_array.split()]
    # print("the display list is: ", display_list)
    # print("the display length is: ", display_array_length)


# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(w=winw, h=winh - bord, far=4000.0, background=(0, 0, 0, 0), frames_per_second=120)
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

    # print("file_list: ", str(file_list[0]))
    string_dir = 'images/patterns/'
    extensions = [".jpg"]
    file_list = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]

    pattern_list = [string_dir + x for x in file_list]
    # print("pattern_list: ", str(pattern_list[0]))

    pattern_count = [num for num in range(0, len(file_list))]
    # print("pattern_count: ", str(pattern_count))


def corridor_build():
    global display_array
    global corridor_start

    # blockimg = pi3d.Texture("textures/crop.jpg")

    for i in display_array:
        # print("i is: ", i)
        pattern_name = pattern_list[display_array[i]]
        # print("pattern name is: ", pattern_name)
        blockimg = pi3d.Texture("../textures/crop.jpg")
        pattern = pi3d.Texture(pattern_name)

        pi3d.corridor(
            corridor_start, 10, mymap, 50, 33, 30,
            details=[flatsh, [pattern], 50, 0.0, 1.0, 1.0], walls="nso")  #

        corridor_start += 33


# --- FUNCTION ---
pattern_get()
read_data()

# print("the second list element is: ", display_list)


# print("display array ", display_array)
# print("pattern_count: ", str(pattern_count))
# print("test pattern name: ", str(pattern_list[display_array[0]]))

# --- TEXTURE ----
blockimg = pi3d.Texture("images/textures/crop.jpg")  # defined
# print(blockimg)
pattern1 = pi3d.Texture(pattern_list[int(display_list[0])])
pattern2 = pi3d.Texture(pattern_list[int(display_list[1])])
pattern3 = pi3d.Texture(pattern_list[int(display_list[2])])
pattern4 = pi3d.Texture(pattern_list[int(display_list[3])])

pattern5 = pi3d.Texture(pattern_list[int(display_list[4])])
pattern6 = pi3d.Texture(pattern_list[int(display_list[5])])
pattern7 = pi3d.Texture(pattern_list[int(display_list[6])])
pattern8 = pi3d.Texture(pattern_list[int(display_list[7])])

pattern9 = pi3d.Texture(pattern_list[int(display_list[8])])
pattern10 = pi3d.Texture(pattern_list[int(display_list[9])])
pattern11 = pi3d.Texture(pattern_list[int(display_list[10])])
pattern12 = pi3d.Texture(pattern_list[int(display_list[11])])

roofedgeimg = pi3d.Texture("images/textures/crop.jpg")
roofimg = pi3d.Texture("images/textures/crop.jpg")
ectex = [pi3d.Texture('images/textures/crop.jpg')]
bumpimg = pi3d.Texture("images/textures/grey.jpg")
endwall = pi3d.Texture("images/textures/hornbeam2.png")

myecube = pi3d.EnvironmentCube(size=20000.0, maptype="HALFCROSS")
myecube.set_draw_details(flatsh, ectex)

# Create elevation map
mapwidth = 10000.0
mapdepth = 10000.0
mapheight = 0.0

mymap = pi3d.ElevationMap(mapfile="images/textures/white.png",
                          width=mapwidth, depth=mapdepth, height=mapheight,
                          divx=64, divy=64)

mymap.set_draw_details(flatsh, [bumpimg], 0, 0.0)
# mymap.set_fog((0.3,0.25,0.1,0.8), 500.0)

# Create some random block models elsewhere on the map!


print("in here, check seg fault")
pi3d.corridor(
    corridor_start, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern1], 1, 1, 1, 1], walls="nso")  # intial case

pi3d.corridor(
    corridor_start + corridor_length_avg * 1, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern2], 1, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 2, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern3], 1, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 3, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern4], 50, 0.0, 1.0, 1.0], walls="nso")  # intial case

pi3d.corridor(
    corridor_start + corridor_length_avg * 4, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern5], 50, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 5, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern6], 50, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 6, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern7], 50, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 7, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern8], 50, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 8, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern9], 50, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 9, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern10], 50, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 10, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern11], 50, 0.0, 1.0, 1.0], walls="nso")  #

pi3d.corridor(
    corridor_start + corridor_length_avg * 11, 10, mymap, 50, corridor_length_avg, 30,
    details=[flatsh, [pattern12], 50, 0.0, 1.0, 1.0], walls="nso")

pi3d.corridor(
    corridor_length + 1, 10, mymap, 50, 1, 30,
    details=[flatsh, [endwall], 50, 0.0, 1.0, 1.0], walls="w")

# corridor_build()

oldxposition = 160

print("in here, check seg fault2")

# CAM = pi3d.Camera(eye=(0.0,0.0,-5.0))

# this part for the movement of camera - avatar camera
rot = 0.0
tilt = 0.0
avhgt = 20

mymouse = pi3d.Mouse(restrict=True)
mymouse.start()
mykeys = pi3d.Keyboard()

mykey = pi3d.Keyboard()

omx, omy = mymouse.position()  # in order to get old position

CAMERA = pi3d.Camera.instance()

# create the soliod object
man = pi3d.SolidObject("man", pi3d.Size(0.5, avhgt, 0.5), pi3d.Position(0, (mymap.calcHeight(5, 5) + avhgt / 2), 0), 1)

# just for verify


# this is object inital position
initialxm = -15  # center x position - half of the length +1 this case: 150 - 150/2 +1, when changing to serial input position, data should be changed to (pos+138)
initialym = avhgt / 2
initialzm = 9

initialposition = pi3d.Position(initialxm, initialym, initialzm)  # just in case

man.move(initialposition)

ardStr = 'x'

global round_count

round_count = 0

pi3d.SolidObject.drawall()

prev_y = 0
while DISPLAY.loop_running():
    # print("xm value: ", man.x())
    CAMERA.reset()
    CAMERA.rotate(rot_fix, 0, 0)
    CAMERA.rotate(0, tilt_fix, 0)
    # CAMERA.position((xm, ym, zm))

    pos = 0

    CAMERA.position((man.x(), man.y() + 3, man.z()))

    # print("in here, check seg fault3")
    myecube.draw()
    mymap.draw()
    # print("in here, check seg fault4")
    pi3d.SolidObject.drawall()

    # print("in here, check seg fault5")

    # used to rotate the camera, data for camera rotating
    mx, my = mymouse.position()
    print(my)
    # print(ardSer.in_waiting)
    if ardSer is not None:
        while ardSer.in_waiting:
            # print(ardSer.inWaiting())
            ardStr = ardSer.readline()
            print(ardStr)
            DardStr = ardStr.decode("utf-8")
            try:
                if DardStr.find(',') != -1:
                    dy_string = DardStr[0:DardStr.find(',')]
                    dy_list = [int(d) for d in re.findall(r'-?\d+', dy_string)]
                    # print(dy_string)
                    dy = dy_list[0]
                    print("dy: ", dy)
                    pos = int(dy)
                else:
                    pos = 0

            except:
                print("reading problem")
                ardSer.flush()

    pos = my - prev_y
    prev_y = my

    # pos = pos / 10

    # pos = 4

    # --- position update ---

    xm = man.x() + pos
    if xm < -15:
        xm = -15

    zm = man.z()
    ym = mymap.calcHeight(xm, zm) + avhgt / 2

    NewPos = pi3d.Position(xm, ym, zm)  # set the new position
    collisions = man.CollisionList(NewPos)  # count for collisions it has

    k = mykeys.read()
    if k > -1:
        if k == 10:  # key RETURN
            mc = 0
        elif k == 27:  # Escape key
            mykeys.close()
            mymouse.stop()
            DISPLAY.stop()
            if ardSer is not None:
                ardSer.close()
            break
    else:
        pass

    # if not, it will move to the new position
    if not collisions:
        man.move(NewPos)

    # --- TESTING ROUND ---
    new_postion = man.x()
    # roundcount = new_postion - 138

    if (corridor_length - 20 < new_postion < corridor_length + 10):
        round_count += 1
        # print("rount number is: ", round_count)
        man.move(initialposition)
        # CAMERA.position((xm, ym, zm))
        output_serial.write(str(round_count).strip() + " @ " + str(new_postion).strip())
        output_serial.write('\n')

    else:
        round_count == round_count

# print("rount number is: ", round_count)
output_serial.close()
inputs.release()
DISPLAY.destroy()
