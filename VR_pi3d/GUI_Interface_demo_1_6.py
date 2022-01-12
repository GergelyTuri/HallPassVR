#Note: the structure will be based on processing JSON file 
#A SELF_CHECK function is added in order to try to cover and detect all bug suitation 
#SO FAR SO GOOD but extra testbench will be needed in the end 
#Pic name is decoded (might cause error)

#have done: 1)Output JSON  2)Optimize speed  3)Self check 

#TobeDone:  1)More self check case to add e.g.
# after delete pic in folder, during INIT, should detect which history pattern can't be used(and delete)
#2) output Path JSON need to generate, extra note in the file might be need 
#3) A new nuke.py file will be needed, when nuke, should let the element file to default
#4) Need to write generate case for PNG etc 


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

#from GUI_Interface_demo_11_9 import ADDS_PATH


#from partial_test import LISTBOX_ELEMENT

# --- DEFINE ---
root = Tk()
root.geometry("1450x600") # set size of window


Path              = ["Combination1.jpg", "Combination2.jpg", "Combination3.jpg"]


ListFrame         = Frame(root, bg = '#10ccef')
CombinationFrame  = Frame(root, bg = '#c9b5fa')
HistoryComb       = Frame(root, bg = '#0a5cf5')
Input             = Frame(root, bg = '#9714eb')


string_dir = 'image/ELEMENT'

extensions = [".jpg", ".png" ]

ELEMENT_LIST = []
ELEMENT_LIST = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]


# --- FUNCTIONS ---
def INIT(): 
    INDEX = 0
    #global
    global CODENAME_LIST
    global ELEMENT_CONVERT_TABLE
    global ADDS_ELEMENT
    global ADDS_PATTERN
    global AADS_PATH
    global ADDS_PATH
    global ELEMENT_LIST
    global HIST_PATH_LIST
    
    global SEF_ELEMENT_G
    global ONCADD_ELEMENT_G_LIM
    global SEF_CHECK_DECODE_G # store the current pic decode name , eg. br 
    global SEF_CHECK_NAME_G # store the current pic name in jpg
    
    global SEF_CHECK_HIST_PATTERN_NAME_G #store information about history pattern, in jpg
    
    
    global selected_indices_ELEMENT_LIST
    selected_indices_ELEMENT_LIST = 0
    
    global CURR_STA_CURR_SEL # store the current curr list , size up to 4
    
    CODENAME_LIST = [] # list store the name after decode
    
    global PROGRAM_RUN_TIME
    global PATTERN_DICT
    global PATH_DICT
    global DROPBOX_PATTERN
    global DROPBOX_PATTERN_OLD
    
    global FLAG_subthread1
    global FLAG_subthread2
    global FLAG_CANVAS_REFRESH
    global SIZE_PATTERN
    global CANVAS_PATH_ENABLE_CHECK
    global PATH_GEN_PATTERN_LOC
    global JSON_GEN_PATTERN_LOC 
    
    global HIST_PATT_NAME_AB
    
    
    global preStr_ceiling
    global preStr_floor
    global INPUT_READY
    global PATH_READY
    global CANVAS_READY
    
    global INPUT_EXPT_NAME
    global INPUT_EXPT_LEN
    
    global INPUT_FLOOR_ELEMENT
    global INPUT_CEILING_ELEMENT
    
    ELEMENT_CONVERT_TABLE = {"NAME":[], "DECODE_NAME":[]} #directory store iofrmation about inital name and name after decode 
    PATTERN_DICT = {}
    PATH_DICT = {}
    
    SEF_ELEMENT_G= []
    SEF_CHECK_DECODE_G = []
    SEF_CHECK_NAME_G = []
    
    SEF_CHECK_HIST_PATTERN_NAME_G = [] #store information
    
    DROPBOX_PATTERN = [0, 0 ,0]
    DROPBOX_PATTERN_OLD = [1,0,0]
    CANVAS_PATH_ENABLE_CHECK = [0,0,0]
    PATH_GEN_PATTERN_LOC = [None, None, None]
    JSON_GEN_PATTERN_LOC = [None, None, None]
    
    FLAG_subthread1 = 0
    FLAG_subthread2 = 0
    
    FLAG_CANVAS_REFRESH = 0

    ONCADD_ELEMENT_G_LIM = 4
    PROGRAM_RUN_TIME = 0
    
    ELEMENT_LIST = []  # list store the picture name , eg. black.jpg 
    ELEMENT_LIST = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]
    
    HIST_PATH_LIST = []
    #file_list  = os.listdir(string_dir)
    SIZE_ELEMENT = (40,40)
    SIZE_PATTERN   = (300,30)
    SIZE_PATH    = (480,30)
    
    preStr_floor = ''
    preStr_ceiling = ''
    INPUT_READY = 0
    PATH_READY = 0
    CANVAS_READY = 0
    
    INPUT_FLOOR_ELEMENT = ''
    INPUT_CEILING_ELEMENT = ''
    INPUT_EXPT_NAME = ''
    INPUT_EXPT_LEN = 0
    
    
    #address
    ADDS_ELEMENT = 'image/ELEMENT/'
    ADDS_PATTERN = 'image/HIST_PATTERN/'
    ADDS_PATH    = 'image/HIST_PATH/'
    
    PROGRAM_RUN_TIME = time.process_time()   
    
    #function
    DROPBOX_PATTERN_STATE()
    ELEMENT_DECODE()
    JSON_INIT()
    
    SELF_CHECK(INDEX)
    
    LISTBOX_HIST_PATT_SEFRE()
    

    
def JSON_INIT():
    PATTERN_DICT['format'] = {
    'element_decode': ['index1', 'index2', 'index3', 'index4'],
    'element_name': ['IMG1', 'IMG2', 'IMG3', 'IMG4'],
    'element_num': ['NUM1', 'NUM2', 'NUM3', 'NUM4'], 
    'GENE_TIME':   'Wed Jan 31 09:49:09 2018'
    }
    
    json_string = json.dumps(PATTERN_DICT, indent=4) #PATTERN_DICT can only be used when process data

    with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
        try:
            data = json.loads(f.read())

            if data:
                #print("data exist")
                pass
        except JSONDecodeError:
            with open('image/HIST_PATTERN/PATTERN.json', 'w+') as f:
                f.write(json_string)
                f.write(' \n')
            
            
            
    path_format = 'PATH ' + 'Tue Nov 23 13:30:13 2021'
    PATH_DICT[path_format] = {
                'PATTERN1' : {
                'element_decode': ['index1', 'index2', 'index3', 'index4'],
                'element_name': ['IMG1', 'IMG2', 'IMG3', 'IMG4'],
                        'element_num': ['NUM1', 'NUM2', 'NUM3', 'NUM4'],  
                }, 
                
                'PATTERN2':{
                        'element_decode': ['index1', 'index2', 'index3', 'index4'],
                        'element_name': ['IMG1', 'IMG2', 'IMG3', 'IMG4'],
                        'element_num': ['NUM1', 'NUM2', 'NUM3', 'NUM4'],       
                },
                
                'PATTERN3':{
                        'element_decode': ['index1', 'index2', 'index3', 'index4'],
                        'element_name': ['IMG1', 'IMG2', 'IMG3', 'IMG4'],
                        'element_num': ['NUM1', 'NUM2', 'NUM3', 'NUM4'], 
                },
                
                'Note' : {},
                
               'INPUT':{
                    'Floor': "IMG",
                    'Ceiling': 'IMG',
                    'Path Length': 'digit',
                }
                
                #top/bottom need to add               
        }
    
    json_string2 = json.dumps(PATH_DICT, indent= 4)         
    with open('image/HIST_PATH/PATH.json', 'r') as f:
        try:
            data = json.loads(f.read())

            if data:
                #print("data exist")
                pass
        except JSONDecodeError:
            with open('image/HIST_PATH/PATH.json', 'w+') as f:
                f.write(json_string2)
                f.write(' \n')                      


def DROPBOX_PATTERN_STATE():
    global DROPBOX_PATTERN
    
    #state = Label(root, text = DROPBOX_CLICKED.get())
    string = DROPBOX_CLICKED.get()
    #print("DROPBOX_PATTERN_STATE: ", string)
    
    if   (string == "Pattern I"):
        DROPBOX_PATTERN = [1,0,0]
    elif (string == "Pattern II"):
        DROPBOX_PATTERN = [0,1,0]
    elif (string == "Pattern III"):
        DROPBOX_PATTERN = [0,0,1]
    
    root.after(50, DROPBOX_PATTERN_STATE)
    
    
def DROPBOX_PATTERN_LIST_CHECK():
    global FLAG_CANVAS_REFRESH
    global DROPBOX_PATTERN_OLD 
    
    #while True:
        #if FLAG_subthread1 == 0:
            #print(DROPBOX_PATTERN_OLD)
    if DROPBOX_PATTERN != DROPBOX_PATTERN_OLD:
        DROPBOX_PATTERN_OLD = DROPBOX_PATTERN
        FLAG_CANVAS_REFRESH = 1 #means clean
    else:
                #FLAG_CANVAS_REFRESH = 0
        #trash.seek(0)
        #trash.write("trash")
        #FLAG_CANVAS_REFRESH = 0
        pass
        #else:
            #break
    root.after(50, DROPBOX_PATTERN_LIST_CHECK)
    
        
def CANVAS():
    global FLAG_CANVAS_REFRESH
    global FLAG_CANVAS_PATH_ENABLE 
    global CANVAS_PATH_ENABLE_CHECK #sotr canvas flag eg [1,0,0]
    global JSON_GEN_PATTERN_LOC #store pattern eg. ['c5c5c5c5', None, None]
    global PATH_READY
    global PATH_GEN_PATTERN_LOC
    
    FLAG_CANVAS_PATH_ENABLE = 0
    
    #while True:
        #print(FLAG_CANVAS_REFRESH)
        #if FLAG_subthread2 == 0:

    for element in DROPBOX_PATTERN:
        if element == 1:
            pos = DROPBOX_PATTERN.index(element)
            #print(pos)
            pos += 1

                    #print("postion is: ", pos)
                
    if FLAG_CANVAS_REFRESH == 1: #clean the canvas
        #print("clean canvas")
        FLAG_CANVAS_PATH_ENABLE = 0
        PATH_READY = 0 # when clean the canvas, PATH_READY has to be 0
        CANVAS_PATH.delete(ALL)
        if pos == 1:
            CANVAS_PATTERN1.delete("all")
                    #print ("CANVAS 1 need to be clean")
            FLAG_CANVAS_REFRESH = 0
            CANVAS_PATH_ENABLE_CHECK[0] = 0
            
            PATH_GEN_PATTERN_LOC[0] = None
            JSON_GEN_PATTERN_LOC[0] = None

            #print(PATH_GEN_PATTERN_LOC) #store img pass eg. ['image/HIST_PATTERN/c5c5c5c5.jpg', None, None]
            #print(CANVAS_PATH_ENABLE_CHECK)
            #print(JSON_GEN_PATTERN_LOC)

        if pos == 2:
            CANVAS_PATTERN2.delete("all")
            #print ("CANVAS 2 need to be clean")
            FLAG_CANVAS_REFRESH = 0
            CANVAS_PATH_ENABLE_CHECK[1] = 0
            
            PATH_GEN_PATTERN_LOC[1] = None
            JSON_GEN_PATTERN_LOC[1] = None
            
            #print(PATH_GEN_PATTERN_LOC)
            #print(CANVAS_PATH_ENABLE_CHECK)
            #print(JSON_GEN_PATTERN_LOC)

        if pos == 3:
            CANVAS_PATTERN3.delete("all")
            #print ("CANVAS 3 need to be clean")
            FLAG_CANVAS_REFRESH = 0
            CANVAS_PATH_ENABLE_CHECK[2] = 0
            
            PATH_GEN_PATTERN_LOC[2] = None
            JSON_GEN_PATTERN_LOC[2] = None
            
            #print(PATH_GEN_PATTERN_LOC)
            #print(CANVAS_PATH_ENABLE_CHECK)
            #print(JSON_GEN_PATTERN_LOC)
            
        #print(CANVAS_PATH_ENABLE_CHECK)
        
        #function used for self check
        if CANVAS_PATH_ENABLE_CHECK == [1,1,1]:
            print("ERROR EXIST IN CANVAS")
            quit()
        else:
            pass 
                            
    elif FLAG_CANVAS_REFRESH == 2: #
        PATH_READY = 0
        CANVAS_PATH.delete(ALL)
        if pos == 1:
            #print ("CANVAS 1 need to be clean")
            img_path = ADDS_PATTERN + GEN_PATTERN_NAME +'.jpg'
            #print(img_path)
            IMG_RESIZE_CANVAS(img_path, SIZE_PATTERN, CANVAS_PATTERN1)

            FLAG_CANVAS_REFRESH = 0
            CANVAS_PATH_ENABLE_CHECK[0] = 1
            
            PATH_GEN_PATTERN_LOC[0] = img_path
            JSON_GEN_PATTERN_LOC[0] = GEN_PATTERN_NAME
            
            #print(PATH_GEN_PATTERN_LOC)
            #print(JSON_GEN_PATTERN_LOC)
            #print(CANVAS_PATH_ENABLE_CHECK)
            
        if pos == 2:
            img_path = ADDS_PATTERN + GEN_PATTERN_NAME +'.jpg'
            #print(img_path)
            IMG_RESIZE_CANVAS(img_path, SIZE_PATTERN, CANVAS_PATTERN2)
                  
            #print ("CANVAS 2 need to be clean")
            FLAG_CANVAS_REFRESH = 0
            CANVAS_PATH_ENABLE_CHECK[1] = 1
            
            PATH_GEN_PATTERN_LOC[1] = img_path
            JSON_GEN_PATTERN_LOC[1] = GEN_PATTERN_NAME
            
            #print(PATH_GEN_PATTERN_LOC)
            #print(JSON_GEN_PATTERN_LOC)
            #print(CANVAS_PATH_ENABLE_CHECK)
            
        if pos == 3:
            #print ("CANVAS 3 need to be clean")
            img_path = ADDS_PATTERN + GEN_PATTERN_NAME +'.jpg'
            IMG_RESIZE_CANVAS(img_path, SIZE_PATTERN, CANVAS_PATTERN3)
                  
            FLAG_CANVAS_REFRESH = 0
            CANVAS_PATH_ENABLE_CHECK[2] = 1
            
            PATH_GEN_PATTERN_LOC[2] = img_path
            JSON_GEN_PATTERN_LOC[2] = GEN_PATTERN_NAME
            
            #print(PATH_GEN_PATTERN_LOC)
            #print(JSON_GEN_PATTERN_LOC)
            #print(CANVAS_PATH_ENABLE_CHECK)
                         
        #print(CANVAS_PATH_ENABLE_CHECK)
        if CANVAS_PATH_ENABLE_CHECK == [1,1,1]:
            try:
        #img_list = [ADDS_ELEMENT+ ELEMENT_CONVERT_TABLE["NAME"][x] for x in CURRSEL_ELEMENT_GEN]
        ##print(img_list)
                COMB_PATTERN_NAME_LIST = [Image.open(y) for y in PATH_GEN_PATTERN_LOC]
            except:
                print("ERROR: PATTERN NOT FOUND")

            WIDTHS, HEIGHTS = zip(*(i.size for i in COMB_PATTERN_NAME_LIST))

            total_width = sum(WIDTHS)

            max_height = max(HEIGHTS)

            new_im = Image.new('RGB', (total_width, max_height))

            x_offset = 0

            for im in COMB_PATTERN_NAME_LIST:
                new_im.paste(im, (x_offset,0))
                x_offset += im.size[0]
    

            new_im.save('pathdraft.jpg')

            IMG_RESIZE_CANVAS('pathdraft.jpg', (480,30), CANVAS_PATH)
            #print("CANVAS for PATH should generate here")
            #print(PATH_GEN_PATTERN_LOC)
            #print(JSON_GEN_PATTERN_LOC)
            PATH_READY = 1
            FLAG_CANVAS_REFRESH = 0
            #IMG_RESIZE_CANVAS(img_path, SIZE_PATTERN, CANVAS_PATTERN3)
        else:
            pass 
        
    elif FLAG_CANVAS_REFRESH == 3: #case for history delete all
        
        CANVAS_PATH_ENABLE_CHECK = [0,0,0]
        PATH_GEN_PATTERN_LOC = [None, None, None]
        JSON_GEN_PATTERN_LOC = [None, None, None]
        
        CANVAS_PATTERN1.delete(ALL)
        CANVAS_PATTERN2.delete(ALL)
        CANVAS_PATTERN3.delete(ALL)
        CANVAS_HIST_PATTERN.delete(ALL)
        CANVAS_PATH.delete(ALL)
        
        FLAG_CANVAS_REFRESH = 0
                                 
    else:
        pass
    
    root.after(50, CANVAS)
            
     
    
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
    #print(ELEMENT_CONVERT)    
    #print(CODENAME_LIST)
    

    
def PATTERN_GEN(CURRSEL_ELEMENT_GEN):
    global GEN_PATTERN_NAME
    
    COMB_IMAGE_DECODE_NAME_LIST = [ELEMENT_CONVERT_TABLE["DECODE_NAME"][x] for x in CURRSEL_ELEMENT_GEN]
    #print(COMB_IMAGE_DECODE_NAME_LIST)

    #print(CURRSEL_ELEMENT_GEN[1])
    try:
        img_list = [ADDS_ELEMENT+ ELEMENT_CONVERT_TABLE["NAME"][x] for x in CURRSEL_ELEMENT_GEN]
        #print(img_list)
        COMB_IMAGE_NAME_LIST = [Image.open(y) for y in [ADDS_ELEMENT+ ELEMENT_CONVERT_TABLE["NAME"][x] for x in CURRSEL_ELEMENT_GEN]]
    except:
        print("ERROR: IMAGE NOT FOUND")

    WIDTHS, HEIGHTS = zip(*(i.size for i in COMB_IMAGE_NAME_LIST))

    total_width = sum(WIDTHS)

    max_height = max(HEIGHTS)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0

    for im in COMB_IMAGE_NAME_LIST:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    
    GEN_PATTERN_NAME = ''.join(COMB_IMAGE_DECODE_NAME_LIST)  
    
    #print(GEN_PATTERN_NAME)

    new_im.save(ADDS_PATTERN + GEN_PATTERN_NAME +'.jpg')
    

def CURRSEL_ELEMENT(self):
    #global CODENAME_LIST
    """ handle item selected event
    """
    INDEX = 0
    SELF_CHECK(INDEX)
    
    # get selected indices
    index1 = LISTBOX_ELEMENT.curselection()
    index2 = LISTBOX_PATTERN.curselection()
    index3 = LISTBOX_HIST_PATTERN.curselection()
  
    if index1:
        selected_indices1 = index1[0]
        #print ("selected_indices1: ", selected_indices1)
        selected_indices1_path = ADDS_ELEMENT + ELEMENT_CONVERT_TABLE['NAME'][selected_indices1]
        IMG_RESIZE_CANVAS(selected_indices1_path, (40,40), CANVAS_ELEMENT)
        #print(selected_indices1_path)
    
    elif index2:
        selected_indices2 = index2[0]
        #print ("selected_indices2: ", selected_indices2)
    elif index3:
        selected_indices3 = index3[0]
        
        HIST_PATT_NAME_SEL_AB = LISTBOX_HIST_PATTERN.get(LISTBOX_HIST_PATTERN.curselection())
        HIST_PATT_NAME_SEL = ADDS_PATTERN + HIST_PATT_NAME_SEL_AB
        IMG_RESIZE_CANVAS(HIST_PATT_NAME_SEL, SIZE_PATTERN, CANVAS_HIST_PATTERN)
        
        
    else:
        pass
    
#might use a class 

def ONCLICK_ADD(): # Edit Need
    INDEX = 1
    try:
        ADD_ELEMENT_NUM = LISTBOX_ELEMENT.curselection()[0] #store information about pic in number
        #print(ADD_ELEMENT_NUM)
        
        if len(SEF_ELEMENT_G) < ONCADD_ELEMENT_G_LIM: # ONCADD_ELEMENT_G_LIM = 4
            SEF_ELEMENT_G.append(ADD_ELEMENT_NUM) 
            
            SEF_CHECK_DECODE_G.append(ELEMENT_CONVERT_TABLE['DECODE_NAME'][ADD_ELEMENT_NUM])
            SEF_CHECK_NAME_G.append(ELEMENT_CONVERT_TABLE['NAME'][ADD_ELEMENT_NUM])
            

        else:
            print("Error: Out of Limit")     
    except IndexError:
        print("Error Click the correct box")
        
       
    SELF_CHECK(INDEX)
    LISTBOX_PATTERN_SEFRE()
    
    
    
def ONCLICK_DELETE():
    INDEX = 2 
    #SELF_CHECK(SEF_ELEMENT_G)
    global FLAG_CANVAS_REFRESH
    
    if LISTBOX_PATTERN.curselection():
        try:
            DELETE_ELEMENT_NUM = LISTBOX_PATTERN.curselection()[0]
            #print(DELETE_ELEMENT_NUM)
        except:
            print("ERROR: No Element Select")
    
        if len(SEF_ELEMENT_G) > 0:
            FLAG_CANVAS_REFRESH = 1            
            SEF_ELEMENT_G.remove(SEF_ELEMENT_G[DELETE_ELEMENT_NUM])
        
            SEF_CHECK_DECODE_G.remove(SEF_CHECK_DECODE_G[DELETE_ELEMENT_NUM])
            SEF_CHECK_NAME_G.remove(SEF_CHECK_NAME_G[DELETE_ELEMENT_NUM])
        else:
            print("Error: there is nothing to delete")
    
    else:
        pass
        
    SELF_CHECK(INDEX)
    LISTBOX_PATTERN_SEFRE()
    


def ONCLICK_DELETE_ALL():
    global FLAG_CANVAS_REFRESH
    
    INDEX = 3
    SEF_ELEMENT_G.clear()
    SEF_CHECK_DECODE_G.clear()
    SEF_CHECK_NAME_G.clear()
    
    SELF_CHECK(INDEX)
    LISTBOX_PATTERN_SEFRE()
    FLAG_CANVAS_REFRESH = 1
        

def ONCLICK_GENERATE():
    global FLAG_CANVAS_REFRESH 
    INDEX = 4
    print("self check decode name group: ", SEF_CHECK_DECODE_G)
    print("self check name group: ", SEF_CHECK_NAME_G)
    print("self check element number group: " , SEF_ELEMENT_G)
    
    if len(SEF_ELEMENT_G) < ONCADD_ELEMENT_G_LIM:
        print("ERROR: ", "Need "+str(ONCADD_ELEMENT_G_LIM - len(SEF_ELEMENT_G))+" ELEMENTS")
    
    elif len(SEF_ELEMENT_G) == 0:
        messagebox.showwarning("ERROR", "Empty Element list")
        
    else:
        PATTERN_GEN(SEF_ELEMENT_G)
        
        FLAG_CANVAS_REFRESH = 2 
        
        JSON_PROCESS(GEN_PATTERN_NAME, 
                     SEF_CHECK_DECODE_G, 
                     SEF_CHECK_NAME_G, 
                     SEF_ELEMENT_G)

        SELF_CHECK(INDEX)
        
        LISTBOX_HIST_PATT_SEFRE()
        #just for test
        #img_path = ADDS_PATTERN + GEN_PATTERN_NAME +'.jpg'
        #IMG_RESIZE_CANVAS(img_path, (300,30), CANVAS_PATTERN1)
        
def ONCLICK_UPLOAD():
    INDEX = 5
    
    global SEF_CHECK_DECODE_G
    global SEF_CHECK_NAME_G
    global SEF_ELEMENT_G
    global HIST_PATT_NAME_AB
    try:
        HIST_PATT_SEL = LISTBOX_HIST_PATTERN.curselection()[0]
        #print("HIST_PATT_SEL", HIST_PATT_SEL)
        #print(LISTBOX_HIST_PATTERN.get(LISTBOX_HIST_PATTERN.curselection()))
        HIST_PATT_NAME_SEL = LISTBOX_HIST_PATTERN.get(LISTBOX_HIST_PATTERN.curselection())
        
        HIST_PATT_NAME_AB = HIST_PATT_NAME_SEL[:HIST_PATT_NAME_SEL.index('.')]
        #print(HIST_PATT_NAME_AB)
        try:
            with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
                PATTERN_DICT_HIST = json.loads(f.read())
                if HIST_PATT_NAME_AB in PATTERN_DICT_HIST:
                    
                    SEF_CHECK_DECODE_G = PATTERN_DICT_HIST[HIST_PATT_NAME_AB]['ELEMENT_DECODE_INDEX']
                    SEF_CHECK_NAME_G = PATTERN_DICT_HIST[HIST_PATT_NAME_AB]['ELEMENT_NAME_IMG']
                    SEF_ELEMENT_G = PATTERN_DICT_HIST[HIST_PATT_NAME_AB]['ELEMENT_NUM_DIG']
                    
                else:
                    print("ERROR HIST PATTERN not in JSON file")
                    quit()
                           
        except JSONDecodeError:
            print("ERROR exists in ONCLICK_UPLOAD")

        SELF_CHECK(INDEX)
        LISTBOX_PATTERN_SEFRE()

    except IndexError:
        print("ERROR: Click the correct box")
        
     

def ONCLICK_HIS_PATTERN_DELETE():
    global PATH_GEN_PATTERN_LOC
    CANVAS_CLEAN = [0,0,0]
    INDEX = 6
    try:
        HIST_PATT_SEL = LISTBOX_HIST_PATTERN.curselection()[0]
        HIST_PATT_NAME_SEL = LISTBOX_HIST_PATTERN.get(LISTBOX_HIST_PATTERN.curselection())

        HIST_PATT_NAME_AB = HIST_PATT_NAME_SEL[:HIST_PATT_NAME_SEL.index('.')]

        with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
            PATTERN_DICT = json.loads(f.read())
        
        del PATTERN_DICT[HIST_PATT_NAME_AB]

        json_string = json.dumps(PATTERN_DICT, indent=4)

        #update JSON file
        with open('image/HIST_PATTERN/PATTERN.json', 'w') as f:
            f.write(json_string)

        #upload pattern
        PATH_HIST_PATT_NAME_SEL = ADDS_PATTERN + HIST_PATT_NAME_SEL
        #print(PATH_HIST_PATT_NAME_SEL) 
        os.remove(PATH_HIST_PATT_NAME_SEL)
        #SELF_CHECK(INDEX)
        
        CANVAS_HIST_PATTERN.delete("all")
        
        print(PATH_GEN_PATTERN_LOC)
        
        for i in range(len(PATH_GEN_PATTERN_LOC)):
            if (PATH_HIST_PATT_NAME_SEL == PATH_GEN_PATTERN_LOC[i]):
                if (i == 0):
                    CANVAS_PATTERN1.delete(ALL)
                elif (i == 1):
                    CANVAS_PATTERN2.delete(ALL)
                elif (i == 2):
                    CANVAS_PATTERN3.delete(ALL)
            else:
                pass
            
        SELF_CHECK(INDEX)
        LISTBOX_HIST_PATT_SEFRE()
    except IndexError:
        print ("please click the right box")
    except JSONDecodeError:
        print("ERROR EXISTS in ONCLICK_HIS_PATTERN_DELETE")
        print("ERROR EXIST, PROGRAM CLOSE in 5S")
        time.sleep(5)
        quit() 
    #print(PATTERN_DICT)
    
    

def ONCLICK_HIS_PATTERN_DELETEALL():
    global FLAG_CANVAS_REFRESH
    INDEX = 7
    #result=messagebox.askquestion('Delete All','This will remove all historys, do you want to do that')
    with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
        PATTERN_DICT = json.loads(f.read())
    
    for element in PATTERN_DICT.copy():
        #print (element)
        if element == 'format':
            pass
        else:
            del PATTERN_DICT[element]
            
    print(PATTERN_DICT)
    json_string = json.dumps(PATTERN_DICT, indent=4)
    
    filelist = glob.glob('image/HIST_PATTERN/*.jpg')
    print(filelist)
    
    for element in filelist:
        os.remove(element)
    #update JSON file
    with open('image/HIST_PATTERN/PATTERN.json', 'w') as f:
        f.write(json_string)
        
    SELF_CHECK(INDEX)
    LISTBOX_HIST_PATT_SEFRE()
    
    
    FLAG_CANVAS_REFRESH = 3
    
    CANVAS()
    
    
    
    
    
    
    
           
def ONCLICK_START():
    global INPUT_READY
    global PATH_READY

    print("INPUT_FLOOR_ELEMENT is ", INPUT_FLOOR_ELEMENT)
    print("INPUT_CEILING_ELEMENT is ", INPUT_CEILING_ELEMENT)
    print("INPUT_EXPT_NAME is ", INPUT_EXPT_NAME)
    print("INPUT_EXPT_LEN is ", INPUT_EXPT_LEN)

    #print()
    
    print("Input signal: ", INPUT_READY)
    #print("PATH signal: ", PATH_READY ) 
    #PATH_PROCESS()
    
    if ((INPUT_READY) and (PATH_READY)):
        print("CANVAS for PATH should generate here")
        PATH_PROCESS()

        os.system('python3 VR_open.py')

    else:
        #CANVAS_PATH.delete(ALL)
        print("INPUT INFORMATION MISSING, VR CAN'T BE GENERATE")    
               
    
def ONCLICK_EXIT():
    starttime = time.time()
    #print(starttime)
    INDEX = 5
    global FLAG_subthread1
    global FLAG_subthread2
    
    root.destroy()


def INPUT():
    #initial 
    
    global preStr_floor
    global preStr_ceiling 
    
    global INPUT_FLOOR_ELEMENT
    global INPUT_CEILING_ELEMENT
    
    global INPUT_EXPT_NAME
    global INPUT_EXPT_LEN
    
    
    global INPUT_READY
    
    currStr_floor = DROPBOX_CLICKED_FLOOR.get()
    currStr_ceiling = DROPBOX_CLICKED_CEILING.get()
    
    try:
        if ((preStr_floor != currStr_floor) or (preStr_ceiling != currStr_ceiling)):
            #print("floor is ", currStr_floor)
            #print("ceiling is ",currStr_ceiling )
            
            if (preStr_floor != currStr_floor):
                img_path_floor = ADDS_ELEMENT + currStr_floor
                #print("floor is ", img_path_floor) 
                IMG_RESIZE_CANVAS(img_path_floor, (40,40), CANVAS_INPUT_FLOOR)
                
            elif (preStr_ceiling != currStr_ceiling):
                img_path_ceiling = ADDS_ELEMENT + currStr_ceiling
                #print("ceiling is ", img_path_ceiling)
                IMG_RESIZE_CANVAS(img_path_ceiling, (40,40), CANVAS_INPUT_CEILING)

            
            preStr_floor = currStr_floor
            preStr_ceiling = currStr_ceiling
        else:
            pass
                
    except: 
        print("Error exists in Input fuction")
        time.sleep(3)
        quit()        

    #print("floor is ", currStr_floor)
    #print("ceiling is ",currStr_ceiling )
    
    INPUT_FLOOR_ELEMENT = currStr_floor
    INPUT_CEILING_ELEMENT = currStr_ceiling
    
    
    
    #print("floor is ", INPUT_FLOOR_ELEMENT)
    #print("ceiling is ",INPUT_CEILING_ELEMENT )
    
    #read length and  name
    result_length = Input_Length.get()
    result_name=Input_Name.get()

    #print(result_length)

    INPUT_EXPT_NAME = result_name
    INPUT_EXPT_LEN = result_length 

    #print(INPUT_EXPT_LEN)

    if ((INPUT_FLOOR_ELEMENT != '') and (INPUT_CEILING_ELEMENT != '')
        and (INPUT_EXPT_NAME != '') and (int(INPUT_EXPT_LEN) > 0)):
        
        INPUT_READY = 1
            
    else:
        INPUT_READY = 0
        #print("INPUT INFORMATION MISSING")
    
    

    #INPUT_READY 
        
    root.after(50, INPUT)



def JSON_PROCESS(IMG_NAME, ELEMENT_DECODE, ELEMENT_NAME, ELEMENT_NUM):
    localtime  = time.ctime()
    
    mydict = {
        'ELEMENT_DECODE_INDEX': ELEMENT_DECODE,
        'ELEMENT_NAME_IMG':     ELEMENT_NAME,
        'ELEMENT_NUM_DIG':      ELEMENT_NUM,
        'GENE_TIME':            localtime
    }
    
    
    with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
        PATTERN_DICT = json.loads(f.read())
        
    PATTERN_DICT[IMG_NAME] = mydict
    
    json_string = json.dumps(PATTERN_DICT, indent=4)
    
    with open('image/HIST_PATTERN/PATTERN.json', 'w') as f:
        f.write(json_string)
            

        #print("ERROR exist when reading JSON file")
    
def PATH_PROCESS():
    global JSON_GEN_PATTERN_LOC
    global PATH_GEN_PATTERN_LOC
    
    my_dict = {}
    INDEX = 8
    input_dict = {}
    
    #self check
    #SELF_CHECK(INDEX)
    
    with open('image/HIST_PATH/PATH.json', 'r') as f:
        PATH_DICT = json.loads(f.read())
        
    #print("format: ", format)
    #try:
    with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
        try:
            input_data = json.loads(f.read())

            if input_data:
            #print("data exist")
                pass
        except JSONDecodeError:
            print("ERROR exists in PATH_PROCESS reading JSON")

    with open('image/HIST_PATH/PATH.json', 'w') as f:
        error_count = 0
        occurence = [0, 0, 0]
        #format = INPUT_EXPT_NAME +" "+ time.ctime()
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 

        format = now + " "+ INPUT_EXPT_NAME
        ADDS_PATH_CANVAS = ADDS_PATH + format + '.jpg'
        
        transpt = open('trash.txt', 'w')
        transpt.write(format)
        transpt.close()


        for element in JSON_GEN_PATTERN_LOC:
            if element not in input_data:
                print("ERROR exists in PATH_PROCESS reading JSON")
                        #error_count +=1
                quit()

            else:
                times = JSON_GEN_PATTERN_LOC.count(element)
                occurence[JSON_GEN_PATTERN_LOC.index(element)] = times
                        #print(PATTERN_DICT['format']['element_decode'])
                        #pass
                        #print(PATTERN_DICT[element])
                my_dict[element] = input_data[element]
        #print(occurence)                
        #print(my_dict)
        
        PATH_DICT[format] = my_dict
        PATH_DICT[format]['Note'] = occurence
        
        input_dict['Floor'] = INPUT_FLOOR_ELEMENT
        input_dict['Ceiling'] = INPUT_CEILING_ELEMENT
        input_dict['Path Length'] = INPUT_EXPT_LEN

        PATH_DICT[format]['INPUT'] = input_dict


        json_string = json.dumps(PATH_DICT, indent=4)
        
        f.write(json_string)
        
        #path canvas update
        #PATH_GEN_PATTERN_LOC
    try:
        #img_list = [ADDS_ELEMENT+ ELEMENT_CONVERT_TABLE["NAME"][x] for x in CURRSEL_ELEMENT_GEN]
        ##print(img_list)
        COMB_PATTERN_NAME_LIST = [Image.open(y) for y in PATH_GEN_PATTERN_LOC]
    except:
        print("ERROR: PATTERN NOT FOUND")

    WIDTHS, HEIGHTS = zip(*(i.size for i in COMB_PATTERN_NAME_LIST))

    total_width = sum(WIDTHS)

    max_height = max(HEIGHTS)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0

    for im in COMB_PATTERN_NAME_LIST:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    

        #GEN_PATTERN_NAME = 
    
        #print(GEN_PATTERN_NAME)
    #now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 

    #ADDS_PATH_CANVAS = ADDS_PATH + now + " "+ INPUT_EXPT_NAME + '.jpg'

    new_im.save(ADDS_PATH_CANVAS)
       
     #time.sleep(5)
    SELF_CHECK(INDEX)
    
    
    
def LISTBOX_PATTERN_SEFRE():
    LISTBOX_PATTERN.delete(0, END)
    
    for element in SEF_CHECK_NAME_G:
        LISTBOX_PATTERN.insert(END, element)    
    
    
def LISTBOX_PATTERN_SEFRE():
    LISTBOX_PATTERN.delete(0, END)
    
    for element in SEF_CHECK_NAME_G:
        LISTBOX_PATTERN.insert(END, element)
        
#def LISTBOX_ELEMENT_SEFRE():

def LISTBOX_HIST_PATT_SEFRE():
    filelist = glob.glob('image/HIST_PATTERN/*.jpg')
    len_img = len(filelist)
    
    SEF_CHECK_PATTERN_NAME_G = [os.path.basename(s) for s in filelist]
    #img_absolute_list = [element[:element.index('.')] for element in fileName_absolute_list]
    LISTBOX_HIST_PATTERN.delete(0, END)
    
    for element in SEF_CHECK_PATTERN_NAME_G:
        LISTBOX_HIST_PATTERN.insert(END, element)

    
    
def IMG_RESIZE_CANVAS(img, size, canvas):
    global CANVAS_READY

    CANVAS_READY = 0
    canvas.delete(ALL)
    
    IMG_PATH = Image.open(img)
    IMG_PATH_RESIZE = IMG_PATH.resize(size, Image.ANTIALIAS)

    IMG_PATH_NEW = ImageTk.PhotoImage(IMG_PATH_RESIZE)
    IMG_VIEW_PATTERN   = canvas.create_image(0, 0, 
                    image = IMG_PATH_NEW, 
                    anchor = "nw")
    canvas.img = IMG_PATH_NEW

    CANVAS_READY = 1

    #print('canvas_ready :', CANVAS_READY)
    

    
    
    
def SELF_CHECK(INDEX): #Edit Need
    #SEF_ELEMENT_G = ELEMENT_G
    #print(INDEX)
    global case
    case = ''
    
    #print(DROPBOX_PATTERN)
    
    for element in DROPBOX_PATTERN:
        if element == 1:
            pos = DROPBOX_PATTERN.index(element)
            #print(pos)
            pos += 1
            
    if INDEX == 0:
        case = "INIT"
    if INDEX == 1:
        case = "ONCLICK_ADD"
    elif INDEX == 2:
        case = "ONCLICK_DELETE"
    elif INDEX == 3:
        case = "ONCLICK_DELETE_ALL"
    elif INDEX == 4:
        case = 'ONCLICK_GENERATE'
    elif INDEX == 5:
        case = "ONCLICK_UPLOAD"
    elif INDEX == 6:
        case = "ONCLICK_HIS_PATTERN_DELETE"
    elif INDEX == 7:
        case = "ONCLICK_HIS_PATTERN_DELETEALL"
    elif INDEX == 8:
        case = "PATH_GENERATE"
        
    
    BOOL_SEF_CHECK_CORR = 0
    CHECK_ELEMENT_G = []
    key_list = list(ELEMENT_CONVERT_TABLE['NAME'])
    
    print("                                                            ")
    print("-------------------------SELF CHECK-------------------------")
    print("self check state: ", case)
    print("self check decode name group: ", SEF_CHECK_DECODE_G)
    print("self check name group: ", SEF_CHECK_NAME_G)
    print("self check element number group: " , SEF_ELEMENT_G)
    print("self check pattern state: ", pos)

    
    #self check
    
    #small case for cursor select
    if (INDEX == 0):
        filelist = glob.glob('image/ELEMENT/*.jpg')
        len_img = len(filelist)
        
        if (len_img == LISTBOX_ELEMENT.size()):
            pass 
        else:
            print("ERROR EXIST, PROGRAM CLOSE in 3S, small case i cursor select fail")
            time.sleep(3)
            quit()  
        
    if (len(SEF_ELEMENT_G) == 0):
        if (len(SEF_CHECK_DECODE_G) == 0  and len(SEF_CHECK_NAME_G) == 0):
            BOOL_SEF_CHECK_CORR = 1
            pass
        
        else:
            print("ERROR EXIST, PROGRAM CLOSE in 3S")
            time.sleep(3)
            quit()  
    else:
        for element in range(len(SEF_ELEMENT_G)):
            if ELEMENT_CONVERT_TABLE["DECODE_NAME"][SEF_ELEMENT_G[element]] == SEF_CHECK_DECODE_G[element]:
            
                CHECK_ELEMENT_G.append(key_list.index(SEF_CHECK_NAME_G[element]))
            #print("CHECK_ELEMENT_G:", CHECK_ELEMENT_G)
            
            else:
                print("ERROR EXIST, PROGRAM CLOSE in 3S")
                time.sleep(3)
                quit()
            
        if CHECK_ELEMENT_G == SEF_ELEMENT_G:
            BOOL_SEF_CHECK_CORR = 1
            pass
        else:
            print("ERROR EXIST, PROGRAM CLOSE in 3S")
            time.sleep(3)
            quit()
            
    
            
    #self check for gen function
    if ((INDEX == 4) or (INDEX == 6) or (INDEX == 0) or (INDEX == 7)):
        try:
            with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
                HIST_PATT = json.loads(f.read())
            
            if HIST_PATT:
                len_json = len(HIST_PATT)
                if len_json == 1:
                    if 'format' not in HIST_PATT:
                        print("ERROR exits when reading JSON file")
                        time.sleep(3)
                        quit()
                    else:
                        filelist = glob.glob('image/HIST_PATTERN/*.jpg')
                        len_img = len(filelist)

                        if (len_img == len_json -1):
                            pass
                        else:
                            print("ERROR: SIZE of the IMG folder not match with JSON, PROGRAM CLOSE in 3S")
                            time.sleep(3)
                            quit()
                else:
                    filelist = glob.glob('image/HIST_PATTERN/*.jpg')
                    len_img = len(filelist)
                    #print(len_img)
                    #print("json:", len_json)
                
                    if (len_img == len_json-1):
                        fileName_absolute_list = [os.path.basename(s) for s in filelist]
                        img_absolute_list = [element[:element.index('.')] for element in fileName_absolute_list]

                        #print(img_absolute_list)
                        #print
                        error_count = 0
                        for element in img_absolute_list:
                            if element not in HIST_PATT:
                                print("error")
                                error_count +=1
                                
                            else:
                                #print(PATTERN_DICT['format']['element_decode'])
                                pass
                        
                        if (error_count != 0):    
                            print("Special case: self check JSON vs .jpg File Error Count: ", error_count)
                            time.sleep(3)
                            quit()
                                                
                        if error_count:
                            print("ERROR exists when reading JSON or .jpg file, PROGRAM CLOSE in 3S")
                            time.sleep(3)
                            quit()                           
                    else:
                        print("ERROR exists when reading JSON or .jpg file, PROGRAM CLOSE in 3S")
                        time.sleep(3)
                        quit()            
            else: #means empty, should at least have format after JSON init 
                print("ERROR exits when reading JSON file, PROGRAM CLOSE in 3S")
                time.sleep(3)
                quit()
                
        except JSONDecodeError:
            print("ERROR exits when reading JSON file, PROGRAM CLOSE in 3S")
            time.sleep(3)
            quit()
            
    if INDEX == 5:
        SEP_PATTERN_NAME = re.findall('..',HIST_PATT_NAME_AB)
        #print(SEP_PATTERN_NAME)
        if SEP_PATTERN_NAME == SEF_CHECK_DECODE_G:
            print("Special case: self check on UPLOAD success")
           
        else:
           print("ERROR exits when decoding JSON file, PROGRAM CLOSE in 3S")
           time.sleep(3)
           quit() 
           
    if ((INDEX == 8) or (INDEX == 0)):
        #pass
        with open('image/HIST_PATH/PATH.json', 'r') as f:
            HIST_PATH = json.loads(f.read())
            len_json = len(HIST_PATH)
               
        if len_json == 1:
            if 'PATH Tue Nov 23 13:30:13 2021' not in HIST_PATH:
                print("ERROR exits when reading JSON file, PROGRAM CLOSE in 3S")
                time.sleep(3)
                quit()
            else:
                pass
            
        else:
            filelist = glob.glob('image/HIST_PATH/*.jpg')
            len_img = len(filelist) 
            
            if (len_img == len_json -1):
                fileName_absolute_list = [os.path.basename(s) for s in filelist]
                img_absolute_list = [element[:element.index('.')] for 
                                     element in fileName_absolute_list]   

                #print("case under 0 or 8, fileName_absolute_list ", fileName_absolute_list)
                #print("case under 0 or 8, fileName_absolute_list ", img_absolute_list)

                error_count = 0
                for element in img_absolute_list:
                    if element not in HIST_PATH:
                        print("error")
                        error_count +=1
                                
                    else:
                        #print(PATTERN_DICT['format']['element_decode'])
                        pass

            else:
                print ("ERROR exist in PATH folder, PROGRAM CLOSE in 3S") 
                time.sleep(3)         
                quit()
           
    print("                                                            ")
    print("               SELF CHECK SUCCESSFUL                        ")
    print("------------------------------------------------------------")    
           
            
   
# --- DEFAULT ---
canvas = Canvas(ListFrame, width = 50, height = 40)
canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)
DEFAULTPIC = 'Default.jpg'
IMG_RESIZE_CANVAS(DEFAULTPIC, (65, 40), canvas)

CANVAS_ELEMENT = Canvas(ListFrame, width = 35, height = 35) # element
CANVAS_ELEMENT.grid(row = 5, column = 1, columnspan = 1, sticky = W)

#img_resize_canvas("default.jpg", (65,40), canvas)

#stop_timer_threads = False
stop_clean_threads = False



# --- LISTBOX GENERATE ---
LISTBOX_ELEMENT      = Listbox(ListFrame,  font = "Helvetica", height = 5, width = 30, background= 'grey')
LISTBOX_PATTERN      = Listbox(ListFrame,   font = "Helvetica", height = 5, width = 30, background= '#1ecbe1')
LISTBOX_HIST_PATTERN = Listbox(HistoryComb, font = "Helvetica", height = 5, width = 35 )

LISTBOX_PATTERN.grid     (row = 0, column = 8, columnspan = 5, padx=10, pady=10, sticky = W)
LISTBOX_ELEMENT.grid     (row = 0, column = 0, columnspan = 5, padx=10, pady=10, sticky = W)
LISTBOX_HIST_PATTERN.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10, sticky = W)

for PATTERN in ELEMENT_LIST:
    LISTBOX_ELEMENT.insert(END, PATTERN)


LISTBOX_ELEMENT.bind     ('<<ListboxSelect>>', CURRSEL_ELEMENT)
LISTBOX_PATTERN.bind     ('<<ListboxSelect>>', CURRSEL_ELEMENT)
LISTBOX_HIST_PATTERN.bind('<<ListboxSelect>>', CURRSEL_ELEMENT)

# --- Button ---
Button_ADD        = Button(ListFrame,   text = "Add",        width = 5,  height = 2, command= ONCLICK_ADD)
Button_Delete     = Button(ListFrame,   text = "Delete",     width = 5,  height = 2, command= ONCLICK_DELETE)
Button_Delete_All = Button(ListFrame,   text = "Delete All", width = 7,  height = 2, command= ONCLICK_DELETE_ALL)
Button_Generate   = Button(ListFrame,   text = "Generate",   width = 8,  height = 2, command= ONCLICK_GENERATE )
Button_Exit       = Button(root,        text = "Exit",       width = 10, height = 2, command= ONCLICK_EXIT)
Button_Upload     = Button(HistoryComb, text = "Upload",     width = 7,  height = 2, command= ONCLICK_UPLOAD)
Button_Delete_hi  = Button(HistoryComb, text = "Delete",     width = 7,  height = 2, command= ONCLICK_HIS_PATTERN_DELETE)
Button_Del_hi_all = Button(HistoryComb, text = "Delete All", width = 10, height = 2, command= ONCLICK_HIS_PATTERN_DELETEALL)
#Button_Input      = Button(Input,       text = "Read",       width = 7,  height = 2, command= ONCLICK_INPUT_READ)
Button_Start      = Button(root,        text = "Start",      width = 10, height = 2, command= ONCLICK_START)
#lambda: [onClick_Start(),os.system('python Corridor_test_5_20.py')]

Button_ADD.grid       (row = 5,  column = 2,   sticky = N)
Button_Delete.grid    (row = 5,  column = 3,   sticky = N)
Button_Delete_All.grid(row = 5,  column = 4,   sticky = N)
Button_Generate.grid  (row = 5,  column = 10,  sticky = N)
Button_Exit.grid      (row = 10, column = 12,  sticky = N)
Button_Start.grid     (row = 10, column = 11,  sticky = N)
Button_Upload.grid    (row = 1,  column = 0,   sticky = W, padx = 10, pady = 10)
Button_Delete_hi.grid (row = 1,  column = 1,   sticky = W, padx = 10, pady = 10)
Button_Del_hi_all.grid(row = 1,  column = 2,   sticky = W, padx = 10, pady = 10)
#Button_Input.grid     (row = 4,  column = 7,   sticky = W, padx = 10)

# --- EntryBox ---
Input_Name   = Entry(Input, width = 20, font = ("Arial", 12))
Input_Length = Entry(Input, width = 10 ,font = ("Arial", 12))
Input_Length.insert(0, "2")

Input_Name.grid  (row = 2, column = 1, padx = 5, pady = 5, ipady = 5, sticky = W)
Input_Length.grid(row = 3, column = 1, padx = 5, pady = 5, ipady = 5, sticky = W) 

# --- SCROLLBAR ---
scrobar  = Scrollbar(ListFrame)
scrobar1 = Scrollbar(HistoryComb)


scrobar.grid (row = 0, column = 5, sticky= "ns")
scrobar1.grid(row = 0, column = 5, sticky= "ns")

scrobar.config (command = LISTBOX_ELEMENT.yview)
scrobar1.config(command = LISTBOX_HIST_PATTERN.yview)

LISTBOX_ELEMENT.config(yscrollcommand = scrobar.set)
LISTBOX_HIST_PATTERN.config(yscrollcommand = scrobar1.set)


# --- Frame GRID ---
ListFrame.grid       (row = 0, column = 0,  columnspan = 10, sticky = W)
CombinationFrame.grid(row = 0, column = 10, padx = 20,       pady= 20, sticky = W)
HistoryComb.grid     (row = 8, column = 0,  rowspan = 5, columnspan= 8,  sticky = W)
Input.grid           (row = 8, column = 7, columnspan = 5,  sticky = W)

# --- LABEL ---
Label1 = Label(CombinationFrame,  text =" Pattern I",             font = ("Arial", 12))
Label2 = Label(CombinationFrame,  text =" Pattern II",            font = ("Arial", 12))
Label3 = Label(CombinationFrame,  text =" Pattern III",           font = ("Arial", 12))
Label4 = Label(CombinationFrame,  text =" Path",                  font = ("Arial", 12))
Label5 = Label(HistoryComb,       text =" Combination",           font = ("Arial", 12))
Label6 = Label(Input,             text =" Path Name",             font = ("Arial", 12))
Label7 = Label(Input,             text =" Path Length(m)",        font = ("Arial", 12))
Label8 = Label(Input,             text =" Floor",                 font = ("Arial", 12))
Label9 = Label(Input,             text =" Ceiling",               font = ("Arial", 12))

Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)
Label2.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = N)
Label3.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = N)
Label4.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = W)
Label5.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = W)
Label6.grid(row = 2, column = 0, padx = 15, pady = 15, sticky = W)
Label7.grid(row = 3, column = 0, padx = 15, pady = 15, sticky = W)
Label8.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = W)
Label9.grid(row = 1, column = 0, padx = 15, pady = 15, sticky = W)



# --- CANVAS ---
CANVAS_PATTERN1        = Canvas(CombinationFrame, width = 300, height = 30)
CANVAS_PATTERN2        = Canvas(CombinationFrame, width = 300, height = 30)
CANVAS_PATTERN3        = Canvas(CombinationFrame, width = 300, height = 30)
CANVAS_PATH            = Canvas(CombinationFrame, width = 480, height = 30)
CANVAS_HIST_PATTERN    = Canvas(HistoryComb,      width = 300, height = 30)
CANVAS_INPUT_FLOOR     = Canvas(Input,            width = 35,  height = 35)
CANVAS_INPUT_CEILING   = Canvas(Input,            width = 35,  height = 35)

CANVAS_PATTERN1.grid     (row = 0, column = 1, columnspan = 6,  sticky = W)
CANVAS_PATTERN2.grid     (row = 1, column = 1, columnspan = 6,  sticky = W)
CANVAS_PATTERN3.grid     (row = 2, column = 1, columnspan = 6,  sticky = W)
CANVAS_PATH.grid         (row = 7, column = 5, columnspan = 15, sticky = W)
CANVAS_HIST_PATTERN.grid (row = 4, column = 0, columnspan = 6,  sticky = W, padx = 10, ipady = 5)
CANVAS_INPUT_FLOOR.grid  (row = 0, column = 15)
CANVAS_INPUT_CEILING.grid(row = 1, column = 15)

#canvas_path = Canvas(root, )

# --- OPTION MEUN ---
DROPBOX_CLICKED = StringVar()
DROPBOX_CLICKED.set("Pattern I")
drop   = OptionMenu(ListFrame, DROPBOX_CLICKED, "Pattern I", "Pattern II", "Pattern III")
drop.grid(row = 5, column = 9)



DROPBOX_CLICKED_FLOOR = StringVar()
DROPBOX_CLICKED_FLOOR.set("")
drop_floor = OptionMenu(Input, DROPBOX_CLICKED_FLOOR, *ELEMENT_LIST)
drop_floor.config(width = 30)
drop_floor.grid(row = 0, column = 1, sticky = W, columnspan= 8)

#CANVAS_INPUT_FLOOR.grid  (row = 0, column = 15)



DROPBOX_CLICKED_CEILING = StringVar()
DROPBOX_CLICKED_CEILING.set("")
drop_floor = OptionMenu(Input, DROPBOX_CLICKED_CEILING, *ELEMENT_LIST)
drop_floor.config(width = 30)
drop_floor.grid(row = 1, column = 1, sticky = W, columnspan= 8)

oldstr  = 1
currStr = DROPBOX_CLICKED.get()

# --- THREAD ---
#background_thread = Thread(target=timer)
#background_thread.start()

#clean_thread = Thread(target=Comb_List_Clean)
#clean_thread.start()

# --- MAIN ---
#comb_statue()
#history_comb_read()
INIT()

#trash = open('trash.txt', 'w+')
#dummy = open('trash2.txt', 'w+')

root.wait_visibility()
#subthread1 = Thread(target = DROPBOX_PATTERN_LIST_CHECK)
#subthread1.start()

#subthread2 = Thread(target = CANVAS)
#subthread2.start()
root.after(0, DROPBOX_PATTERN_LIST_CHECK)
root.after(0, CANVAS)
root.after(0, INPUT)

root.mainloop()



# --- TODO ---
#1) Easter Egg!