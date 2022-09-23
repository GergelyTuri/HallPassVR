'''"""The Head-Fixed Mice Virtual Reality System

This Python script used to reset ELEMENT folder back to default and clear all exist
history pattern & path

'''

from   tkinter   import *
from   PIL       import ImageTk, Image
from   tkinter   import filedialog
import os
import numpy     as np 
from   tkinter   import messagebox
import time
from   threading import Thread
import datetime
import linecache
import glob
import shutil
from os import path
import re
import json
from json.decoder import JSONDecodeError


'''NUKE_HIST functions aims to nuke all exist pattern and path data generated before '''
def NUKE_HIST():
    INDEX = 7
    
    #delete HIST PATTERN
    with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
        PATTERN_DICT = json.loads(f.read()) # read history pattern data from json
    
    for element in PATTERN_DICT.copy():
        #print (element)
        if element == 'format': # ignore the first key in JSON file which is format
            pass
        else:
            del PATTERN_DICT[element] #delete history pattern
            
    #print(PATTERN_DICT)
    json_string = json.dumps(PATTERN_DICT, indent=4)
    
    filelist = glob.glob('image/HIST_PATTERN/*.jpg')
    #print(filelist)
    
    for element in filelist:
        os.remove(element) #delete all img 
    #update JSON file
    with open('image/HIST_PATTERN/PATTERN.json', 'w') as f:
        f.write(json_string)
    



    #delete HIST_PATH
    with open('image/HIST_PATH/PATH.json', 'r') as f:
        PATH_DICT = json.loads(f.read())
    
    path_format = 'PATH ' + 'Tue Nov 23 13:30:13 2021'

    for element in PATH_DICT.copy():
        #print (element)
        if element == path_format:
            pass
        else:
            del PATH_DICT[element]
            
    #print(PATH_DICT)
    json_string = json.dumps(PATH_DICT, indent=4)
    
    filelist = glob.glob('image/HIST_PATH/*.jpg')
    #print(filelist)
    
    for element in filelist:
        os.remove(element)
    #update JSON file
    with open('image/HIST_PATH/PATH.json', 'w') as f:
        f.write(json_string) 


'''ELEMENT_DEFAULT functions aims to set the img in ELEMENT 
folder backs to default, default img saves under src_folder '''

def ELEMENT_DEFAULT():
    dst_folder = 'image/ELEMENT'
    src_folder = 'image/SOURCE/DEFAULT'

    filelist = glob.glob('image/ELEMENT/*.jpg')
    #print(filelist)
    
    for element in filelist:
        os.remove(element)

    for jpgfile in glob.iglob(os.path.join(src_folder, "*.jpg")):
        shutil.copy(jpgfile, dst_folder)


if __name__ == "__main__":
    NUKE_HIST()
    ELEMENT_DEFAULT()