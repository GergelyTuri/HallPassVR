import json
import glob, os
import time
from json.decoder import JSONDecodeError

'''with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
        PATTERN_DICT = json.loads(f.read())

length = len(PATTERN_DICT)

if 'format' not in PATTERN_DICT:
        print("error")

else:
        print(PATTERN_DICT['format']['element_decode'])

print(length)

#PATTERN_DICT = {}

def JSON_INIT():
    PATTERN_DICT['format'] = {
    'element_decode': ['index1', 'index2', 'index3', 'index4'],
    'element_name': ['IMG1', 'IMG2', 'IMG3', 'IMG4'],
    'element_num': ['NUM1', 'NUM2', 'NUM3', 'NUM4'], 
    'GENE_TIME':   time.ctime()
    }
    
    json_string = json.dumps(PATTERN_DICT, indent=4)

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
                        

#JSON_INIT()
filelist = glob.glob('image/HIST_PATTERN/*.jpg')
print(len(filelist))
for file in filelist:
    print(file)

fileName_absolute_list = [os.path.basename(s) for s in filelist]
img_absolute_list = [element[:element.index('.')] for element in fileName_absolute_list] 

print (fileName_absolute_list)
print (img_absolute_list)
#print (PATTERN_DICT)

error_count = 0
for element in img_absolute_list:
        if 'bkbkbkbk' not in PATTERN_DICT:
                print("error")
                error_count +=1

        else:
                #print(PATTERN_DICT['format']['element_decode'])
                pass
        
print(error_count)'''

'''with open('PATTERN_test.json', 'r') as f:
        PATTERN_DICT = json.loads(f.read())

print(PATTERN_DICT)'''

#c5c5c5c5.jpg

pattern2delete = "image/HIST_PATTERN/bkbkbkbk.jpg"

HIST_PATT_NAME_AB = pattern2delete[:pattern2delete.index('.')]

PATH_GEN_PATTERN_LOC = ['image/HIST_PATTERN/bkbkbknk.jpg', 'image/HIST_PATTERN/bkbkbkbk.jpg', 'image/HIST_PATTERN/bkbkbkbk.jpg']
CANVAS_CLEAN = [0,0,0]
#print(PATTERN_DICT)
try:
        for i in range(len(PATH_GEN_PATTERN_LOC)):
                if (PATH_GEN_PATTERN_LOC[i] == pattern2delete):
                        #print(i)
                        CANVAS_CLEAN[i] = 1
                        
        print(CANVAS_CLEAN)
                        
                
except:
        print("sorry wrong here")
        
with open('image/HIST_PATTERN/PATTERN.json', 'r') as f:
        PATTERN_DICT = json.loads(f.read())
        
for key in PATTERN_DICT.keys():
        print(key)