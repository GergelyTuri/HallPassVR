# --- GUI Interface 8/12/2021 ---
#Hongtao Cai - Columbia University 
#For Future Delevopment: 1)Add history path to history listbox 
#                        2)Inside VR_open.py, check size of window and set position

# --- THIS IS FINAL EDITION FOR NOW FUTURE CHANGE REQUIRED ---

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

# --- DEFINE ---
root = Tk()
root.geometry("1450x600")


Path              = ["Combination1.jpg", "Combination2.jpg", "Combination3.jpg"]
ListFrame         = Frame(root)
CombinationFrame  = Frame(root)
HistoryComb       = Frame(root)
Input             = Frame(root)

comb_list                = []
comb_list_count          = []
Pattern2Path             = []
curr_list                = []
curr_list_count          = []
History_comb_list        = []
array2list               = []
upload_list              = []
Upload_history_comb_path = []

canvas_enable        = 0
comb1_on             = 0
comb2_on             = 0
comb3_on             = 0
path_on              = 0
canvas1_clean_enable = 0
canvas2_clean_enable = 0
canvas3_clean_enable = 0 
str_comb1            = 0
str_comb2            = 0
str_comb3            = 0
CombArry_size        = 0
History_count        = 0
upload_sig           = 0
history_add_enable   = 0
limit_gen_patt       = 4
limit_gen_comb       = 1
comb_gen_delete_sig  = 0
result_length_digit  = 0
corridor_enable      = 0

lab_comb1         = ''
lab_comb2         = ''
lab_comb3         = ''

pic_comb1         = ''
pic_comb2         = ''
pic_comb3         = ''
pic_path          = ''
history_comb_path = ''
history_path_folder = ''
result_name       = ''

size_pattern      = (0,0)
size_comb         = (0,0)
size_path         = (0,0)



trash               = open("trash.txt", "w")
#history             = open("history.txt","a")
output_pattern2path = open("Pattern2Path.txt", "w")

string0 = "Nothing" 



# --- FUNCTIONS ---
def default():
    
    global file_list
    global pathToImages 
    global ImageName
    global ImageNumCount
    global output_path_12
    global output_path_12_num
    global path2historyComb
    global currStr

    global comb1_on
    global comb2_on 
    global comb3_on
    global str_comb1
    global str_comb2
    global str_comb3

    global lab_comb1
    global lab_comb2
    global lab_comb3 

    global pic_comb1
    global pic_comb2
    global pic_comb3
    global pic_path
    global history_comb_path
    global history_path_folder

    global size_pattern
    global size_comb
    global size_path
    global History_count

    global string0
    global upload_sig
    global corridor_enable 

    string_dir = 'image/'
    extensions = [".jpg"]
    file_list  = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]
    #file_list  = os.listdir(string_dir)

     
    pathToImages     = []
    ImageName        = []
    ImageNumCount    = []
    path2historyComb = []


    comb1_on  = 0
    comb2_on  = 0
    comb3_on  = 0

    str_comb1 = 1
    str_comb2 = 2
    str_comb3 = 3
    currStr   = 1

    size_pattern = (40,40)
    size_comb    = (300,30)
    size_path    = (480,30)

    History_count   = 0
    upload_sig      = 0
    corridor_enable = 0
    

    lab_comb1 = "Combination 1"
    lab_comb2 = "Combination 2"
    lab_comb3 = "Combination 3"
    
    pic_comb1 = "Combination1.jpg"
    pic_comb2 = "Combination2.jpg"
    pic_comb3 = "Combination3.jpg"
    pic_path  = "Path.jpg"
    history_comb_path = 'image/HistoryComb/'
    history_path_folder = 'image/HistoryPath/'

    output_path_12     = [string0 for i in range(12)]
    output_path_12_num = [0 for i in range(12)]
    

    pathToImages  = [string_dir + x for x in file_list]
    ImageName     = [s.replace('.jpg', '') for s in file_list]
    ImageNumCount = [item for item in range(0, len(file_list))]


def history_comb_read():
    global History_comb_list
    global history_comb_path
    global path2historyComb
    global max
    global History_count
    

    #print("history comb read in here")
    string_dir = 'image/HistoryComb'
    extensions = [".jpg"]
    max = 0
    new = 0
    
    History_comb_list_unsorted  = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]
    #print(History_comb_list_unsorted)
    History_comb_list = sorted(History_comb_list_unsorted)
    #print(History_comb_list)
    HistoryCombCount   = [item for item in range(0, len(History_comb_list))]
    HistoryCombName    = [s.replace('.jpg', '') for s in History_comb_list]
    path2historyComb   = [history_comb_path + x for x in History_comb_list]
        
    HistoryList.delete(0, END)

    for PATTERN in HistoryCombName:
        patternarray = PATTERN.split()
        new = patternarray[1]
        if int(new) > max :
            max = int(new)
        elif int(new) < max :
            max = max 

        HistoryList.insert(END, PATTERN)
    
    #print("the max number is: ", max)
    History_count = max 

    



    
def buttonHandler(self):
    file   = pathToImages[int(PatternList.curselection()[0])]
    canvas2 = Canvas(ListFrame, width = 40, height = 40)
    canvas2.grid(row = 5, column = 1, columnspan = 1, sticky = W)

    img_resize_canvas(file, size_pattern, canvas2)



def buttonHandler_History(self):
    #print("in here", path2historyComb)
    #print(str(int(HistoryList.curselection()[0])))
    file = path2historyComb[int(HistoryList.curselection()[0])]
    #print(file)

    img_resize_canvas(file, size_comb, canvas_history_comb)


def onClick_Add():
    global upload_sig
    global curr_list
    global curr_list_count
    global limit_gen_patt 

    Add_pattern = ImageName[int(PatternList.curselection()[0])]
    #print("onClick_Add: ", curr_list_count)
    #print("onClick_Add: ", curr_list)
    
    Comb_size = len(curr_list)
    if upload_sig == 1:
        messagebox.showerror("Error", "Combination exist")
    elif upload_sig == 0:
        if Comb_size < limit_gen_patt:

            CombList.insert(END, Add_pattern)
            curr_list.append(pathToImages[int(PatternList.curselection()[0])])
            curr_list_count.append(ImageNumCount[int(PatternList.curselection()[0])])
            Pattern2Path.append(pathToImages[int(PatternList.curselection()[0])])
        else:
            messagebox.showerror("Error", "Out of Limit")


def onClick_Delete():
    global curr_list
    global curr_list_count
    global upload_sig
    global comb_gen_delete_sig

    if upload_sig == 0:
        #print("current list is :", curr_list)
        Delete_pattern       = curr_list[int(CombList.curselection()[0])]
        Delete_pattern_count = curr_list_count[int(CombList.curselection()[0])]

        #print("delete botton, the iamge name: ", com_test[int(CombList.curselection()[0])])
        CombList.delete(ANCHOR)
        curr_list.remove(Delete_pattern)
        Pattern2Path.remove(Delete_pattern)

        curr_list_count.remove(Delete_pattern_count)

    elif upload_sig == 1:
        CombList.delete(0, END)
        upload_sig = 0
    
    canvas_clean()

    #comb1_refresh()


def onClick_Delete_All():

    global upload_sig

    print("delete all function")

    global curr_list
    global curr_list_count

    #Delete_pattern = ImageName[int(CombList.curselection()[0])]

    CombList.delete(0, END)
    curr_list.clear()
    curr_list_count.clear()
    Pattern2Path.clear()

    canvas_clean()
    
    upload_sig = 0

def canvas_clean():
    global str_comb1
    global str_comb2
    global str_comb3

    global canvas1_clean_enable
    global canvas2_clean_enable
    global canvas3_clean_enable
    global canvas_enable

    StringVar    = clicked.get()
    #print(StringVar)

    if StringVar == lab_comb1:
        #print("combination 1 here")
        canvas1_clean_enable = 1
        canvas_enable = 1
        comb1_refresh()
        
    
    elif StringVar == lab_comb2:
        #print("combination 2 here")
        canvas2_clean_enable = 1
        canvas_enable = 2
        comb2_refresh()

    elif StringVar == lab_comb3:
        #print("combination 3 here")     
        canvas3_clean_enable = 1
        canvas_enable = 3
        comb3_refresh()





def onClick_Generate():

    global comb_list
    global comb_list_count
    global curr_list
    global curr_list_count
    global str_comb1
    global str_comb2
    global str_comb3

    global canvas_enable
    global History_count
    global history_comb_path
    global upload_sig

    global upload_list
    global Upload_history_comb_path
    global history_add_enable
    global comb_gen_delete_sig

    global canvas1_clean_enable
    global canvas2_clean_enable
    global canvas3_clean_enable

    GenArry_size    = CombList.size()

    if upload_sig == 1:
        limit = limit_gen_comb
    elif upload_sig == 0:
        limit = limit_gen_patt

    #global gen_count

    #print("in generate function: ", currStr)

    if GenArry_size == 0:
        messagebox.showerror("Error", "Empty Pattern")
    elif GenArry_size < limit:
        messagebox.showwarning("Warning", "Need "+str(limit)+" Patterns")
    else:
        if (currStr == str_comb1):
            patternname          = pic_comb1
            canvas_enable        = 1

            repl_list_strt_idx   = 0
            repl_list_end_idx    = 4

            canvas1_clean_enable = 0

        elif (currStr == str_comb2):
            patternname          = pic_comb2
            canvas_enable        = 2

            repl_list_strt_idx   = 4
            repl_list_end_idx    = 8

            canvas2_clean_enable = 0

        elif (currStr == str_comb3):
            patternname          = pic_comb3
            canvas_enable        = 3

            repl_list_strt_idx   = 8
            repl_list_end_idx    = 12

            canvas3_clean_enable = 0

        if upload_sig == 0:

            comb_list       = curr_list
            comb_list_count = curr_list_count

            images          = [Image.open(x) for x in comb_list]
            # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
            min_shape       = sorted( [(np.sum(i.size), i.size ) for i in images])[0][1]
            imgs_comb       = np.hstack( (np.asarray( i.resize(min_shape) ) for i in images) )
            # save that combination picture
            imgs_comb       = Image.fromarray( imgs_comb)
            imgs_comb.save(patternname)

            comb_gen_delete_sig = 0

            CombinationCheck(comb_list_count)

            if history_add_enable == 0:
                History_count += 1
                History_list(imgs_comb, History_count, comb_list_count)

            elif history_add_enable == 1:
                #print("pattern already exist, should fuck off")
                messagebox.showerror("Error", "Combination already exist")

        if upload_sig == 1:
            #print("here comes generate combination function")
            comb_list_count = upload_list
            comb_list       = [str(Upload_history_comb_path) for i in range(4)]
            #print("comb list: ", comb_list)
            img             = Image.open(Upload_history_comb_path)
            C_img           = img.copy()
            C_img.save(patternname)


            #print (comb_list)


        comb           = [Image.open(y) for y in Path]
        min_shape_path = sorted( [(np.sum(i.size), i.size ) for i in comb])[0][1]
        imgs_path      = np.hstack( (np.asarray( i.resize(min_shape_path) ) for i in comb))

        imgs_path      = Image.fromarray(imgs_path)
        imgs_path.save(pic_path)

        comb1_refresh()
        comb2_refresh()
        comb3_refresh()
        path_refresh ()
        list_gen    (output_path_12, comb_list, repl_list_strt_idx, repl_list_end_idx)
        #print("the current path list: ", output_path_12)

        list_gen    (output_path_12_num, comb_list_count, repl_list_strt_idx, repl_list_end_idx)
        #print("the current number array: ", output_path_12_num)
        messagebox.showinfo("Information", "Generate Complete")

        canvas_enable = 0

        



def onClick_Exit():
    #print("destory fram here")
    global stop_timer_threads
    global stop_clean_threads

    stop_timer_threads = True
    stop_clean_threads = True

    background_thread.join()
    clean_thread.join()

    trash.close()

    output_pattern2path.write(str(output_path_12))
    output_pattern2path.close()

    #onClick_Start()  ########################################Need to fix 

    t = datetime.datetime.now()
    current_time = t.strftime("%Y-%m-%d %H:%M:%S")
    #history.write(str(current_time).strip() + " " + str(output_path_12).strip())
    #history.write("\n")
    #history.close()

    os.remove("trash.txt")

    root.destroy()
    #print("function killed ")

    
def onClick_Start():
    global result_length_digit
    global corridor_enable 
    
    corridor_enable = 0

    output_path_12_num_string = [str(int) for int in output_path_12_num]
    final_output_path         = " ".join(output_path_12_num_string)
    output                    = open("path.txt", "w")
    output.write(str(final_output_path))
    output.write('\n')
    output.write(str(result_length_digit))
    output.close()
    #print("call from here, GUI")
    HistoryPath(str(final_output_path))
    
    corridor_enable = 0
    
    
def corridor_build():
    global corridor_enable
    
    #print("please fix the shit!!!")
    Label8 = Label(root, text ="just for test", font = ("Arial", 10))
    
    if corridor_enable == 1:
        #os.system('python Corridor_test_6_1.py')
        os.system('python3 VR_open.py')
        #os.system('python test7.py')
    else:
        pass
        
    corridor_enable = 0
    #Label8.after(200, corridor_build)
    


def onClick_upload():
    #print("onClick_upload in here")
    #print(HistoryList.size())
    #print(path2historyComb)
    global array2list
    global upload_list
    global upload_sig
    global limit_gen_patt
    global limit_gen_comb
    global Upload_history_comb_path

    history_comb_pos         = int(HistoryList.curselection()[0])
    Upload_history_comb_path = path2historyComb[int(HistoryList.curselection()[0])]
    #print("upload history combination is: ", Upload_history_comb_path)
    historyCombCount         = open("historyCombCount.txt", "r+")

    if historyCombCount.readline() == "\n":
        #print("in here")
        historyCombCount.seek(0)
        next(historyCombCount)
    else:
        #print("not in here")
        historyCombCount.seek(0)


    readfile   = historyCombCount.readlines()
    #print("read file: ", readfile,  "history comb position: ", history_comb_pos)
    array2list  = readfile[history_comb_pos]
    sentence2list(array2list)
    upload_list = array2list
    comb_name   = HistoryList.get(HistoryList.curselection())

    historyCombCount.close()

    if CombList.size() < limit_gen_comb:
        CombList.insert(END, comb_name)
        upload_sig = 1 
    else:
        messagebox.showerror("Error", "Out of Limit")


def onClick_Delete_hi():
    #print("onClick_delete_history in here")
    click_count = int(HistoryList.curselection()[0])+1
    comb_name   = HistoryList.get(HistoryList.curselection())
    #print(comb_name)
    delete_hi(comb_name)
    history_comb_read()
    canvas_history_comb.delete("all")


def onClick_Del_hi_all():
    #print("onClick_Del_hi_all in here")
    result=messagebox.askquestion('Delete All','This will remove all historys, do you want to do that')
    if result=='yes':

        deleteall = open("historyCombCount.txt", "r+")
        deleteall.truncate()
        deleteall.close()

        #print("Delete all here")
        folder = "image/HistoryComb"
        deleteallfile(folder)

        history_comb_read()
        canvas_history_comb.delete("all")

        messagebox.showinfo('Information',"Delete All History finished")

    else:
        pass
        #print("not clean") #Closing Tkinter window forcefully.


def delete_hi(deletestring):
    teststring2string = deletestring.split()
    click_line_mark   = teststring2string[1]
    size_1            = len(teststring2string[1])
    #print("testing number is :", teststring2string[1], " testing size is: ", size_1)

    line_list = []

    #print(click_line)

    readfile = open("historyCombCount.txt", "r")
    count = 1
    while True: 
        line = readfile.readline()
             
        if line == "":
            pass
        else: 
            click_line        = line.split('\n')[0]
            #print("click line is: ", click_line)
            click_line_split  = click_line.split(' , ')[0]
            res = ''.join(filter(lambda i: i.isdigit(), click_line_split))
            #print(str(res))

            compare_last_digt = str(res).zfill(4)
            #print("the compare number is: ", compare_last_digt)

            if compare_last_digt == click_line_mark:
                #print("the list already exist", display_list)
                #print("match here, the count number is: ", count)
                pass  
            else:
                line_list.append(click_line)
        
        count += 1

        if not line:
            break
        
    readfile.close()
    #print(line_list)

    readfile = open("historyCombCount.txt", "w")
    for item in line_list:
        readfile.write(item)
        readfile.write('\n')

    readfile.close()
    
    #history_comb_path = 'test/HistoryComb/'

    find_path_string = history_comb_path + deletestring + '.jpg'
    #print(find_path_string)

    if path.exists(find_path_string):
        #print("just for test")
        os.remove(find_path_string)
    else:
        print("not here")
        

def comb1_refresh():
    global canvas_enable
    global comb1_on
    global canvas1_clean_enable

    #print("canvas1_clean1 is : ",canvas1_clean_enable)

    if canvas_enable == 1: 
        if canvas1_clean_enable == 1:
            canvas_comb1.delete("all")
            comb1_on = 0
            #print("in here - comb1_refresh")

        elif canvas1_clean_enable == 0:
            img_resize_canvas(pic_comb1, (300,30), canvas_comb1)
            comb1_on         = 1
        
        canvas_comb1.after(200, comb1_refresh)

        
def comb2_refresh():
    global canvas_enable
    global comb2_on
    global canvas2_clean_enable

    #print("canvas1_clean2 is : ",canvas1_clean_enable)

    if canvas_enable == 2: 
        if canvas2_clean_enable == 1:
            canvas_comb2.delete("all")
            comb2_on = 0

        elif canvas2_clean_enable == 0:
            img_resize_canvas(pic_comb2, (300,30), canvas_comb2)
            comb2_on         = 1

        canvas_comb2.after(200, comb2_refresh)


def comb3_refresh():
    global canvas_enable
    global comb3_on
    global canvas3_clean_enable

    #print("canvas1_clean3 is : ",canvas1_clean_enable)

    if canvas_enable == 3:
        if canvas3_clean_enable == 1:
            canvas_comb3.delete("all")
            comb3_on = 0

        elif canvas3_clean_enable == 0:
            img_resize_canvas(pic_comb3, (300,30), canvas_comb3)
            comb3_on         = 1

        canvas_comb3.after(200, comb3_refresh)


def path_refresh():
    global comb1_on, comb2_on, comb3_on
    global path_on

    if (comb3_on & comb1_on & comb2_on) :
        img_resize_canvas(pic_path, (480,30), canvas_path)
        path_on = 1
        if path_on:
            canvas_path.after(200, path_refresh)

    else:
        canvas_path.delete("all")


def list_gen(old_list, new_list, repl_list_strt_idx, repl_list_end_idx):

    old_list[repl_list_strt_idx : repl_list_end_idx] = new_list
    new_list                                         = old_list

    #print("new list is: ", new_list)


def img_resize_canvas(img, size, canvas):
    #print("img_resize here")
    path_pic        = Image.open(img)
    resize_path_pic = path_pic.resize(size, Image.ANTIALIAS)
    img_path        = ImageTk.PhotoImage(resize_path_pic)
    img_view_comb   = canvas.create_image(0, 0, image = img_path, anchor = "nw")
    canvas.img = img_path


def History_list(comb, count, InforArray):
    global history_comb_path

    #print("history list function in here")
    t = datetime.datetime.now()
    current_time = t.strftime("%Y-%m-%d %H:%M:%S")

    pattern_count = "HistoryComb"+str(count)
    history_pic   = history_comb_path + "HistoryComb " + str(History_count).zfill(4) + '.jpg'

    #print("InforArray is: ", InforArray)

    InforArray2String      = [str(int) for int in InforArray]
    InforArray2String_path = " ".join(InforArray2String)

    historyCombCount = open("historyCombCount.txt", "r+")
    CombInfo = pattern_count + " , " + str(InforArray2String_path)

    line = historyCombCount.readlines()

    historyCombCount.write(CombInfo)
    historyCombCount.write("\n")
    #print(linecache.getline('historyCombCount.txt',1))

    line = historyCombCount.readlines()

    historyCombCount.close()

    #HistoryList.insert(END, str(current_time).strip() + "       " + str(pattern_count).strip())
    comb.save(history_pic)

    history_comb_read()


def CombinationCheck(sentence):
    global history_add_enable 
    readfile = open("historyCombCount.txt", "r+")
    #print("comb in here")
    c = 0
    while True:
        c = c + 1 
        a = readfile.readline()
        #print(c)
        #print(a)
        if not a:
            break
            
        if a == "\n" or "":
            print("a is empty")
            pass
            print("the empty line is: ", a)
        else: 
            #print("in here")
            #print("the name is: ",a)
            a2list = a.split(" , ")
            #print(a2list)
            display_list = [int(x) for x in a2list[1].split()]
            #print (display_list)

            if sentence == display_list:
                #print("the list already exist", display_list)
                history_add_enable = 1
                break  
            else:
                history_add_enable = 0


    readfile.close()


def comb_statue():
    global currStr
        
    test_label = Label(root, text = clicked.get())
    StringVar    = clicked.get()
    #print("in here, the text is: ", clicked.get())
    if   (StringVar == lab_comb1):
        currStr = 1
    elif (StringVar == lab_comb2):
        currStr = 2
    elif (StringVar == lab_comb3):
        currStr = 3
    
    test_label.after(200, comb_statue)


def Comb_List_Clean():

    global oldstr
    global currStr
    global curr_list
    global curr_list_count

    global canvas1_clean_enable
    global canvas2_clean_enable
    global canvas3_clean_enable
    global upload_sig

    global canvas_enable

    count = 0
    while True:

        global stop_clean_threads

        if stop_clean_threads:
            print("clean thread ends")
            return 1
            break
        else:
            #print(currStr)
            if (oldstr == currStr):
                count = ~count
                
                trash.seek(0)
                trash.write(str(currStr))
                #print("equal")

            if (oldstr != currStr):

                if (currStr == 1):
                    canvas_enable        = 1
                    canvas1_clean_enable = 1
                    comb1_refresh()
                    #print("canvas1 in here - call from comb_list clean")

                elif (currStr == 2):
                    canvas_enable        = 2
                    canvas2_clean_enable = 1
                    comb2_refresh()

                elif (currStr == 3):
                    canvas_enable        = 3
                    canvas3_clean_enable = 1
                    comb3_refresh()

                canvas_enable = 0
                upload_sig = 0

                CombList.delete(0, END)
                curr_list.clear()
                curr_list_count.clear()
                #print("Delete pattern to array: ", comb_list, "size of array", len(curr_list))
                oldstr = currStr


def getTextInput():
    global result_name
    global result_length_digit

    #print(result_name)

    result_length = Input_Length.get()
    result_name=Input_Name.get()

    if result_name == '':
        messagebox.showerror("Error","The path can't be named")
    else:
        if not (result_length.isdigit()):
            messagebox.showerror("Error","the Length enter should be digit")        
        else: 
            result_length_digit = int(result_length)
            messagebox.showinfo("Information", "Reading input Complete")


def HistoryPath(sentence):
    global result_name
    global result_length_digit
    global history_path_folder
    global corridor_enable

    if result_name == '' or result_length_digit == '':
        messagebox.showerror("Error", "Path Name and Length is not defined")

    else:
        t = datetime.datetime.now()
        current_time = t.strftime("%Y-%m-%d %H:%M:%S")
        history_path_img    = history_path_folder + result_name + str(current_time)+ '.jpg'
        print(history_path_img)

        img   = Image.open(pic_path)
        C_img = img.copy()
        C_img.save(history_path_img)

        historypathfile = open("historyPath.txt", "a")

        #t = datetime.datetime.now()
        #current_time = t.strftime("%Y-%m-%d %H:%M:%S")
        historypathfile.write(str(current_time).strip())
        historypathfile.write("\n")
    
        historypathfile.write(history_path_img)
        historypathfile.write('\n')

        historypathfile.write(sentence)
        historypathfile.write('\n')

        historypathfile.write("Length: "+ str(result_length_digit))
        historypathfile.write('\n')
        historypathfile.write('\n')

        historypathfile.close()

        messagebox.showinfo("Information", "Information saved")
        
        corridor_enable = 1
        
        corridor_build()


    #time
    #name
    #array

    #img.save(history_path_img)


def sentence2list(sentence):
    global array2list
    #print("sentence: ", sentence)
    sentence2array = sentence.split(",")
    #print(sentence2array)
    sentence2array = sentence2array[1]
    array2list = [int(x) for x in sentence2array.split()]
    print(array2list)


def deleteallfile(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        print(file_path)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print("deal 1")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print("deal 2")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

        
def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1            
        global stop_timer_threads
        #print("stop_thread is: ", stop_timer_threads)
        if stop_timer_threads:
            print("Hi This program has now been running for " 
            + str(count) + " seconds")
            break

def img_resize(img, size):
    #print("img_resize here")
    pic        = Image.open(img)
    resize_pic = pic.resize(size, Image.ANTIALIAS)
    resize_pic.save(img)


def vr_image_build(file_list, corridor_pattern_dir_list, size):

    string_dir = 'image/'
    corridor_pattern_dir = 'vr_pattern/'

    corridor_pattern_dir_size = len(corridor_pattern_dir_list)
    file_list_size            = len(file_list)

    #path2corridorfile = [corridor_pattern_dir + element for element in corridor_pattern_dir_list]
    #path2file         = [string_dir + element for element in file_list]


    if corridor_pattern_dir_size == 0:
        for element in file_list:
            path2corridorfile = corridor_pattern_dir + element
            path2file_element = string_dir + element
            pic               = Image.open(path2file_element)
            resize_pic        = pic.resize(size, Image.ANTIALIAS)
            c_img             = resize_pic.copy()
            c_img.save(path2corridorfile)
    
    elif file_list_size > corridor_pattern_dir_size:
        for element in file_list:
            if element not in corridor_pattern_dir_list:
                path2corridorfile = corridor_pattern_dir + element
                path2file_element = string_dir + element
                pic               = Image.open(path2file_element)
                resize_pic        = pic.resize(size, Image.ANTIALIAS)
                c_img             = resize_pic.copy()
                c_img.save(path2corridorfile)
            else: 
                pass

    elif file_list_size < corridor_pattern_dir_size:
        for element in corridor_pattern_dir_list:
            if element not in file_list:
                path2corridorfile = corridor_pattern_dir + element
                path2file_element = string_dir + element
                pic               = Image.open(path2corridorfile)
                resize_pic        = pic.resize((200,200), Image.ANTIALIAS)
                c_img             = resize_pic.copy()
                c_img.save(path2file_element)

    elif file_list_size == corridor_pattern_dir_size:
        pass

            
def image_process():
    default_size_num = (200,200)
    default_size_vr  = (992,992)


    string_dir = 'image/'
    corridor_pattern_dir = 'vr_pattern/'

    extensions = [".jpg"]

    file_list  = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]
    corridor_pattern_dir_list = [f for f in os.listdir(corridor_pattern_dir) if os.path.splitext(f)[1] in extensions]

    #print(file_list)
    #print(corridor_pattern_dir_list)

    path2file  = [string_dir + element for element in file_list]


    #print(path2file)

    vr_image_build(file_list, corridor_pattern_dir_list, default_size_vr)

    for element in path2file:
        image = Image.open(element)
        size_num = image.size

        #print("defore resize: ", size_num)

        if size_num > default_size_num:
            img_resize(element,default_size_num)

        else:
            pass


        image = Image.open(element)
        size_num = image.size

        #print("after resize: ", size_num)



def test():
    #os.system('python Corridor_test_6_1.py')
    os.system('python3 VR_open.py')


# --- DEFAULT ---
canvas = Canvas(ListFrame, width = 65, height = 40)
canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)

canvas2 = Canvas(ListFrame, width = 40, height = 40)
canvas2.grid(row = 5, column = 1, columnspan = 1, sticky = W)

img_resize_canvas("default.jpg", (65,40), canvas)

stop_timer_threads = False
stop_clean_threads = False

default()




# --- LIST ---
PatternList = Listbox(ListFrame,   font = "Helvetica", height = 5, width = 30 )
CombList    = Listbox(ListFrame,   font = "Helvetica", height = 5, width = 30 )
HistoryList = Listbox(HistoryComb, font = "Helvetica", height = 5, width = 35 )

CombList.grid   (row = 0, column = 8, columnspan = 5, padx=10, pady=10, sticky = W)
PatternList.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10, sticky = W)
HistoryList.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10, sticky = W)




for PATTERN in ImageName:
    PatternList.insert(END, PATTERN)

PatternList.bind('<<ListboxSelect>>', buttonHandler)
HistoryList.bind('<<ListboxSelect>>', buttonHandler_History)

# --- Button ---
Button_ADD        = Button(ListFrame,   text = "Add",        width = 5,  height = 2, command = onClick_Add)
Button_Delete     = Button(ListFrame,   text = "Delete",     width = 5,  height = 2, command = onClick_Delete)
Button_Delete_All = Button(ListFrame,   text = "Delete All", width = 7,  height = 2, command = onClick_Delete_All)
Button_Generate   = Button(ListFrame,   text = "Generate",   width = 8,  height = 2, command = onClick_Generate)
Button_Exit       = Button(root,        text = "Exit",       width = 10, height = 2, command = onClick_Exit)
Button_Upload     = Button(HistoryComb, text = "Upload",     width = 7,  height = 2, command = onClick_upload)
Button_Delete_hi  = Button(HistoryComb, text = "Delete",     width = 7,  height = 2, command = onClick_Delete_hi)
Button_Del_hi_all = Button(HistoryComb, text = "Delete All", width = 10, height = 2, command = onClick_Del_hi_all)
Button_Input      = Button(Input,       text = "Read",       width = 7,  height = 2, command = getTextInput)
Button_Start      = Button(root,        text = "Start",      width = 10, height = 2, command = onClick_Start)
#lambda: [onClick_Start(),os.system('python Corridor_test_5_20.py')]

Button_ADD.grid       (row = 5,  column = 2,   sticky = N)
Button_Delete.grid    (row = 5,  column = 3,   sticky = N)
Button_Delete_All.grid(row = 5,  column = 4,   sticky = N)
Button_Generate.grid  (row = 5,  column = 10,  sticky = N)
Button_Exit.grid      (row = 10, column = 12,  sticky = N)
Button_Start.grid     (row = 10, column = 11,  sticky = N)
Button_Upload.grid    (row = 0,  column = 6,   sticky = N, padx = 10, pady = 10)
Button_Delete_hi.grid (row = 0,  column = 7,   sticky = N, padx = 10, pady = 10)
Button_Del_hi_all.grid(row = 0,  column = 8,   sticky = N, padx = 10, pady = 10)
Button_Input.grid     (row = 0,  column = 4,   sticky = W, padx = 10)

# --- EntryBox ---
Input_Name   = Entry(Input, width = 20)
Input_Length = Entry(Input, width = 10)
Input_Length.insert(0, "2")

Input_Name.grid  (row = 0, column = 1, sticky = W, padx = 5)
Input_Length.grid(row = 0, column = 3, sticky = W, padx = 5) 

# --- SCROLLBAR ---
scrobar  = Scrollbar(ListFrame)
scrobar1 = Scrollbar(HistoryComb)


scrobar.grid (row = 0, column = 5, sticky= "ns")
scrobar1.grid(row = 0, column = 5, sticky= "ns")

scrobar.config (command = PatternList.yview)
scrobar1.config(command = HistoryList.yview)

PatternList.config(yscrollcommand = scrobar.set)
HistoryList.config(yscrollcommand = scrobar1.set)


# --- Frame GRID ---
ListFrame.grid       (row = 0, column = 0,  columnspan = 10, sticky = W)
CombinationFrame.grid(row = 0, column = 10, padx = 20,       pady= 20, sticky = W)
HistoryComb.grid     (row = 8, column = 0,  columnspan= 10,  sticky = W)
Input.grid           (row = 9, column = 0,  columnspan = 5,  sticky = W)

# --- LABEL ---
Label1 = Label(CombinationFrame,  text =" Combination 1",         font = ("Arial", 15))
Label2 = Label(CombinationFrame,  text =" Combination 2",         font = ("Arial", 15))
Label3 = Label(CombinationFrame,  text =" Combination 3",         font = ("Arial", 15))
Label4 = Label(root,              text =" Path",                  font = ("Arial", 25))
Label5 = Label(HistoryComb,       text =" History Combination",   font = ("Arial", 15))
Label6 = Label(Input,             text =" Path Name",             font = ("Arial", 10))
Label7 = Label(Input,             text =" Path Length(m)",        font = ("Arial", 10))

Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)
Label2.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = N)
Label3.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = N)
Label4.grid(row = 7, column = 4, padx = 10, pady = 10, sticky = N)
Label5.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = NW)
Label6.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = W)
Label7.grid(row = 0, column = 2, padx = 15, pady = 15, sticky = W)



# --- CANVAS ---
canvas_comb1        = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb2        = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb3        = Canvas(CombinationFrame, width = 300, height = 30)
canvas_path         = Canvas(root,             width = 480, height = 30)
canvas_history_comb = Canvas(HistoryComb,      width = 300, height = 30)

canvas_comb1.grid       (row = 0, column = 1, columnspan = 6,  sticky = W)
canvas_comb2.grid       (row = 1, column = 1, columnspan = 6,  sticky = W)
canvas_comb3.grid       (row = 2, column = 1, columnspan = 6,  sticky = W)
canvas_path.grid        (row = 7, column = 5, columnspan = 15, sticky = W)
canvas_history_comb.grid(row = 6, column = 0, columnspan = 6,  sticky = W, padx = 10)

#canvas_path = Canvas(root, )

# --- OPTION MEUN ---
clicked = StringVar()
clicked.set("Combination 1")
drop   = OptionMenu(ListFrame, clicked, "Combination 1", "Combination 2", "Combination 3")
drop.grid(row = 5, column = 9)

oldstr  = 1
currStr = clicked.get()

# --- THREAD ---
background_thread = Thread(target=timer)
background_thread.start()

clean_thread = Thread(target=Comb_List_Clean)
clean_thread.start()

# --- MAIN ---
image_process()
comb_statue()
history_comb_read()
root.mainloop()



# --- TODO ---
#1) Easter Egg!
