#use for partial GUI test

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

#from seperate_test import CODENAME_LIST, ELEMENT_CONVERT

string_dir = 'image/ELEMENT'
extensions = [".jpg", ".png", ]

ELEMENT_LIST = []
global CODENAME_LIST
global ELEMENT_CONVERT_TABLE
global ONCADD_ELEMENT_G
global ONCADD_ELEMENT_G_LIM

global SEF_CHECK_DECODE_G
global SEF_CHECK_NAME_G

CODENAME_LIST = []
ONCADD_ELEMENT_G= []

SEF_CHECK_DECODE_G = []
SEF_CHECK_NAME_G = []

ONCADD_ELEMENT_G_LIM = 4

ELEMENT_CONVERT_TABLE = {"NAME":[], "DECODE_NAME":[]}

ELEMENT_LIST = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]



def ELEMENT_DECODE():
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
    
    #print(CODE_NAME)
    print(ELEMENT_CONVERT_TABLE)    
    #print(CODENAME_LIST)


def CURRSEL_ELEMENT(self):
    #global CODENAME_LIST
    """ handle item selected event
    """
    # get selected indices
    selected_indices = LISTBOX_ELEMENT.curselection()[0]
    print (selected_indices)
    print(CODENAME_LIST[selected_indices])
    print(ELEMENT_CONVERT_TABLE["NAME"][selected_indices])
    
    
def ONCLICK_ADD():
    try:
        ADD_ELEMENT_NUM = LISTBOX_ELEMENT.curselection()[0] #store information about pic in number
        print(ADD_ELEMENT_NUM)
        
        if len(ONCADD_ELEMENT_G) < ONCADD_ELEMENT_G_LIM:
            ONCADD_ELEMENT_G.append(ADD_ELEMENT_NUM)
            
            SEF_CHECK_DECODE_G.append(ELEMENT_CONVERT_TABLE['DECODE_NAME'][ADD_ELEMENT_NUM])
            SEF_CHECK_NAME_G.append(ELEMENT_CONVERT_TABLE['NAME'][ADD_ELEMENT_NUM])
            
            
        else:
            print("Error", "Out of Limit") 
        
        
        
        
    except:
       print("Error exists in ONCLIKC_ADD") 
    
    

root = Tk()
root.geometry("500x600") # set size of window
root.title('Listbox')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


LISTBOX_ELEMENT = Listbox(root,  font = "Helvetica", height = 5, width = 30 )

LISTBOX_ELEMENT.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10, sticky = W)

ImageName = {'Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift'}

for PATTERN in ELEMENT_LIST:
    LISTBOX_ELEMENT.insert(END, PATTERN)
    
LISTBOX_ELEMENT.bind('<<ListboxSelect>>', CURRSEL_ELEMENT)


# --- MAIN ---
#comb_statue()
#history_comb_read()
ELEMENT_DECODE()
root.mainloop()

