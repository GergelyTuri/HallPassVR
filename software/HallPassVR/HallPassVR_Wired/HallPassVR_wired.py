# --- HallPassVR Corridor Interface 9/12/2022 ---
# by Hongtao Cai
# edited/modified by Clay Lacefield
#  - Columbia University
#
# Called by VR_OPEN.py, via HallPassVR_GUI.py
# Reads in virtual linear track/hallway components from GUI,
# draws hallway, then moves through hallway based upon rotary encoder ESP32
# serial input.

from __future__ import absolute_import, division, print_function, unicode_literals
import math
import random
import pi3d
import serial

import numpy as np
import os
import re

import json
from json.decoder import JSONDecodeError

import time

# --- SET UP ---

# adjust these vars to scale VR to rotary/wheel position
corridor_length_default = 192  # cm ticks per 1m
posScaleFactor = 2  # scale factor for position readings (ticks/mm)

winw, winh, bord = 1200, 700, 0
corridor_start = 16

# set up serial connection to rotary ESP32
ardSer = serial.Serial(
    port="/dev/ttyS0",  # set to /dev/ttyS0 for GPIO serial, /dev/ttyUSB0 for USB serial
    baudrate=115200,  # must equal serial baud rate of rotary ESP32 .ino script
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
)

output_serial = open("serial_output.txt", "w")
rot_fix = -90
tilt_fix = -90

# hallway vars to load from GUI json output
global ELEMENT_LIST
ELEMENT_LIST = []

global ELEMENT_CONVERT_TABLE
ELEMENT_CONVERT_TABLE = {"NAME": [], "DECODE_NAME": []}

global CODENAME_LIST
CODENAME_LIST = []

global FLOOR_IMG
global CEILING_IMG
global LEN_PATH

global GOLDEN_PATH_NAME_IMG
global REF_PATH_NUM_DIG

# load hall elements
def DECODE_INITIAL():

    global ELEMENT_LIST
    global ELEMENT_CONVERT_TABLE

    extensions = [".jpg", ".png"]
    ELEMENT_LIST = []
    ELEMENT_LIST = [
        f for f in os.listdir("image/ELEMENT") if os.path.splitext(f)[1] in extensions
    ]

    const = -1
    const_loop = -2

    for element in ELEMENT_LIST:
        ELEMENT_CONVERT_TABLE["NAME"].append(element)

        element = element[: element.index(".")]
        CODE_NAME = element[0] + element[const]

        while CODE_NAME in CODENAME_LIST:
            CODE_NAME = element[0] + element[const_loop]
            const_loop = const_loop - 1

        CODENAME_LIST.append(CODE_NAME)
        ELEMENT_CONVERT_TABLE["DECODE_NAME"].append(CODE_NAME)


# load and check/print hall elements
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

    transpt = open("trash.txt", "r")

    PATH_NAME = transpt.readline()

    print("path name is: ", PATH_NAME)

    NOTE = [0, 0, 0]
    transpt.close()

    with open("image/HIST_PATH/PATH.json", "r") as f:
        try:
            PATH_DICT = json.loads(f.read())

            if PATH_DICT:
                if PATH_NAME in PATH_DICT:
                    PATH_VALUE_DICT = PATH_DICT[PATH_NAME]
                    NOTE = PATH_VALUE_DICT["Note"]
                    INPUT_DICT = PATH_VALUE_DICT["INPUT"]

                    FLOOR_IMG = INPUT_DICT["Floor"]
                    CEILING_IMG = INPUT_DICT["Ceiling"]
                    LEN_PATH = INPUT_DICT["Path Length"]

                    print("floor img is :", FLOOR_IMG)
                    print("Ceiling img is :", CEILING_IMG)
                    print("path length is :", LEN_PATH)
                else:
                    print("ERROR is either JSON file or PATH_NAME")
        except JSONDecodeError:
            print("ERROR exists in PATH_PROCESS reading PATH JSON")

    if NOTE == [3, 0, 0]:
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = PATTERN_1
        PATTERN_3 = PATTERN_2
    elif NOTE == [2, 0, 1]:
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = PATTERN_1
        PATTERN_3 = list(PATH_VALUE_DICT.values())[1]
    elif NOTE == [1, 2, 0]:
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = list(PATH_VALUE_DICT.values())[1]
        PATTERN_3 = PATTERN_2
    elif NOTE == [1, 1, 1]:
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = list(PATH_VALUE_DICT.values())[1]
        PATTERN_3 = list(PATH_VALUE_DICT.values())[2]
    elif NOTE == [2, 1, 0]:
        PATTERN_1 = list(PATH_VALUE_DICT.values())[0]
        PATTERN_2 = list(PATH_VALUE_DICT.values())[1]
        PATTERN_3 = PATTERN_1

    REF_PATH_DECODE_INDEX[0:3] = PATTERN_1["ELEMENT_DECODE_INDEX"]
    REF_PATH_DECODE_INDEX[4:7] = PATTERN_2["ELEMENT_DECODE_INDEX"]
    REF_PATH_DECODE_INDEX[8:11] = PATTERN_3["ELEMENT_DECODE_INDEX"]

    REF_PATH_NAME_IMG[0:3] = PATTERN_1["ELEMENT_NAME_IMG"]
    REF_PATH_NAME_IMG[4:7] = PATTERN_2["ELEMENT_NAME_IMG"]
    REF_PATH_NAME_IMG[8:11] = PATTERN_3["ELEMENT_NAME_IMG"]

    REF_PATH_NUM_DIG[0:3] = PATTERN_1["ELEMENT_NUM_DIG"]
    REF_PATH_NUM_DIG[4:7] = PATTERN_2["ELEMENT_NUM_DIG"]
    REF_PATH_NUM_DIG[8:11] = PATTERN_3["ELEMENT_NUM_DIG"]

    for element in REF_PATH_NUM_DIG:
        GOLDEN_PATH_DECODE_INDEX.append(ELEMENT_CONVERT_TABLE["DECODE_NAME"][element])
        GOLDEN_PATH_NAME_IMG.append(ELEMENT_CONVERT_TABLE["NAME"][element])

    print(GOLDEN_PATH_DECODE_INDEX)
    print(GOLDEN_PATH_NAME_IMG)

    if (GOLDEN_PATH_DECODE_INDEX == REF_PATH_DECODE_INDEX) and (
        GOLDEN_PATH_NAME_IMG == REF_PATH_NAME_IMG
    ):
        print("CORRIDOR SELF CHECK PASSED")
    else:
        print("ERROR EXIST in VR CORRIDOR INITIAL SELF CHECK")


def read_data():
    global display_array
    global display_list
    global display_array_length

    display_list = [int(x) for x in display_array.split()]


# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(
    w=winw, h=winh - bord, far=4000.0, background=(0, 0, 0, 0), frames_per_second=120
)  # (far=4000.0,background=(0, 0, 0, 0), frames_per_second=120) # remove w,h for fullscreen
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

    string_dir = "image/ELEMENT/"
    extensions = [".jpg"]
    file_list = [
        f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions
    ]

    pattern_list = [string_dir + x for x in file_list]

    pattern_count = [num for num in range(0, len(file_list))]


# --- FUNCTION ---
pattern_get()
DECODE_INITIAL()
FINAL_SELF_CHECK()

corridor_length = corridor_length_default * int(LEN_PATH)
corridor_length_avg = corridor_length / 12
corridor_start = corridor_length_avg / 2

# --- TEXTURE ----
blockimg = pi3d.Texture("../textures/crop.jpg")  #
VR_PATTERN = []

for element in REF_PATH_NUM_DIG:
    VR_PATTERN.append(pi3d.Texture(pattern_list[element]))
ceiling_tex_path = "image/ELEMENT/" + CEILING_IMG
ceiling_tex = pi3d.Texture(ceiling_tex_path)
floor_tex_path = "image/ELEMENT/" + FLOOR_IMG
floor_tex = pi3d.Texture(floor_tex_path)
endwall = pi3d.Texture("image/ELEMENT/black.jpg")  # end wall image
myecube = pi3d.EnvironmentCube(size=5000.0, maptype="HALFCROSS")
myecube.set_draw_details(flatsh, [ceiling_tex], 1, 0.0, 1.0, 1.0)  # ceiling

# Create elevation map
mapwidth = 7000.0
mapdepth = 7000.0
mapheight = 0.0

mymap = pi3d.ElevationMap(
    mapfile="../textures/white.png",  # flat elevation map
    width=mapwidth,
    depth=mapdepth,
    height=mapheight,
    divx=64,
    divy=64,
)

mymap.set_draw_details(flatsh, [floor_tex], 50, 50)

# Create an infinity corridor.
for i, pattern in enumerate(VR_PATTERN):
    pi3d.corridor(
        corridor_start + corridor_length_avg * i,
        10,
        mymap,
        50,
        corridor_length_avg,
        30,
        details=[flatsh, [pattern], 1, 0.0, 1.0, 1.0],
        walls="nso",
    )

# draw a wall
pi3d.corridor(
    corridor_length + 1,
    10,
    mymap,
    50,
    1,
    30,
    details=[flatsh, [endwall], 50, 0.0, 1.0, 1.0],
    walls="w",
)

# corridor_build()

oldxposition = 160

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
man = pi3d.SolidObject(
    "man",
    pi3d.Size(0.5, avhgt, 0.5),
    pi3d.Position(0, (mymap.calcHeight(5, 5) + avhgt / 2), 0),
    1,
)

# this is object inital position
initialxm = (
    -15
)  # center x position - half of the length +1 this case: 150 - 150/2 +1, when changing to serial input position, data should be changed to (pos+138)
initialym = avhgt / 2
initialzm = 9

initialposition = pi3d.Position(initialxm, initialym, initialzm)  # just in case

man.move(initialposition)

ardStr = "x"

global round_count

round_count = 0

lastPos = 0

pi3d.SolidObject.drawall()

# -------MAIN RUN LOOP (draw hall, read rotary serial data, move position)
while DISPLAY.loop_running():
    CAMERA.reset()
    CAMERA.rotate(rot_fix, 0, 0)
    CAMERA.rotate(0, tilt_fix, 0)

    pos = 0

    CAMERA.position((man.x(), man.y() + 3, man.z()))

    myecube.draw()
    mymap.draw()
    pi3d.SolidObject.drawall()

    # used to rotate the camera, data for camera rotating
    mx, my = mymouse.position()

    # read ESP32 rotary serial data
    while ardSer.in_waiting:
        ardStr = ardSer.readline()
        # print(ardStr)
        DardStr = ardStr.decode("utf-8")
        try:
            if DardStr.find(",") != -1:
                dy_string = DardStr[0 : DardStr.find(",")]
                dy_list = [int(d) for d in re.findall(r"-?\d+", dy_string)]
                dy = dy_list[0]
                pos = int(dy)
            else:
                pos = 0

        except:
            ardSer.flush()

    pos = pos / 10  # position is in cm not mm
    pos = pos * posScaleFactor

    # --- position update ---

    xm = man.x() + pos  # current/updated absolute position

    if xm < -15:
        xm = 350  # maxPos
    # print(xm)

    # send serial output to reset behavior arduino/esp32 from VR at rollover
    if lastPos - xm >= 100:
        ardSer.write("0\n".encode())
    lastPos = xm

    zm = man.z()
    ym = mymap.calcHeight(xm, zm) + avhgt / 2

    NewPos = pi3d.Position(xm, ym, zm)  # set the new position
    collisions = man.CollisionList(NewPos)  # count for collisions it has

    # press ESCAPE key to end VR
    k = mykeys.read()
    if k > -1:
        if k == 10:  # key RETURN
            mc = 0
        elif k == 27:
            os.remove("trash.txt")  # Escape key
            mykeys.close()
            mymouse.stop()
            DISPLAY.stop()
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

    if corridor_length - 20 < new_postion < corridor_length + 10:
        round_count += 1
        man.move(initialposition)
        output_serial.write(str(round_count).strip() + " @ " + str(new_postion).strip())
        output_serial.write("\n")

    else:
        round_count == round_count


output_serial.close()
# inputs.release()
DISPLAY.destroy()
