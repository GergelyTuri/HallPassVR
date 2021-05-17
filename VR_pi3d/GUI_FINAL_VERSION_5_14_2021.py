# --- GUI Interface 5/14/2021 ---
#Hongtao Cai - Columbia University 
#1) Change Layout/Display
#2) Fix output bug
# --- THIS IS FINAL EDITION FOR NOW FUTURE CHANGE REQUIRED ---

from tkinter import *
#import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import numpy as np 
from tkinter import messagebox
import time
from threading import Thread
import datetime

# --- DEFINE ---
root = Tk()
root.geometry("1200x300")


Path = ["Combination1.jpg", "Combination2.jpg", "Combination3.jpg"]

ListFrame = Frame(root)
CombinationFrame = Frame(root)

com_test = []
com_test_count = []
Pattern2Path = []


canvas_enable = 0

comb1_on = 0
comb2_on = 0
comb3_on = 0


CombArry_size = 0

trash = open("trash.txt", "w")
history = open("history.txt","a")

output = open("path.txt", "w")
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

    global comb1_on
    global comb2_on 
    global comb3_on 

    global string0 

     
    file_list = os.listdir("image/")
    pathToImages = []
    ImageName = []
    ImageNumCount = []


    comb1_on = 0
    comb2_on = 0
    comb3_on = 0

    output_path_12 = [string0 for i in range(12)]
    output_path_12_num = [0 for i in range(11)]

    

    string1 = 'image/'
   

    pathToImages = [string1 + x for x in file_list]
    ImageName = [s.replace('.jpg', '') for s in file_list]

    ImageNumCount= [item for item in range(0, len(file_list))]

    
def buttonHandler(self):
    img = ImageTk.PhotoImage(file = pathToImages[int(PatternList.curselection()[0])])
    #bi.show()
    canvas = Canvas(ListFrame, width = 40, height = 40)
    canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)
    #gif1 = bi
    img_view = canvas.create_image(30, 30, image = img, anchor = CENTER)

    canvas.img = img

def onClick_Add():

    Add_pattern = ImageName[int(PatternList.curselection()[0])]

    Comb_size = len(com_test)
    if Comb_size < 4:
        CombList.insert(END, Add_pattern)
        com_test.append(pathToImages[int(PatternList.curselection()[0])])
        com_test_count.append(ImageNumCount[int(PatternList.curselection()[0])])
        Pattern2Path.append(pathToImages[int(PatternList.curselection()[0])])

    else:
        messagebox.showerror("Error", "Out of Limit")


def onClick_Delete():

    Delete_pattern = com_test[int(CombList.curselection()[0])]
    Delete_pattern_count = com_test_count[int(CombList.curselection()[0])]

    #print("delete botton, the iamge name: ", com_test[int(CombList.curselection()[0])])
    CombList.delete(ANCHOR)
    com_test.remove(Delete_pattern)
    Pattern2Path.remove(Delete_pattern)

    com_test_count.remove(Delete_pattern_count)




def onClick_Delete_All():

    Delete_pattern = ImageName[int(CombList.curselection()[0])]

    CombList.delete(0, END)
    com_test.clear()
    com_test_count.clear()
    Pattern2Path.clear()


def onClick_Generate():

    new_test = com_test
    new_com_test_count = com_test_count


    GenArry_size = len(com_test)

    global currStr
    global canvas_enable

    global new_list
    #global gen_count

    #print("in generate function: ", currStr)

    if (currStr == "Combination 1"):
        patternname = "Combination1.jpg"
        canvas_enable = 1

        repl_list_strt_idx = 0
        repl_list_end_idx = 4


    elif (currStr == "Combination 2"):
        patternname = "Combination2.jpg"
        canvas_enable = 2

        repl_list_strt_idx = 4
        repl_list_end_idx = 8

    elif (currStr == "Combination 3"):
        patternname = "Combination3.jpg"
        canvas_enable = 3

        repl_list_strt_idx = 8
        repl_list_end_idx = 12


    if GenArry_size == 0:
        messagebox.showerror("Error", "Empty Pattern")
    elif GenArry_size < 4:
        messagebox.showwarning("Warning", "Need 4 Patterns")
    else:
        images = [Image.open(x) for x in com_test]

        # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in images])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in images) )

        # save that combination picture
        imgs_comb = Image.fromarray( imgs_comb)
        imgs_comb.save(patternname)


        comb = [Image.open(y) for y in Path]

        min_shape_path = sorted( [(np.sum(i.size), i.size ) for i in comb])[0][1]
        imgs_path = np.hstack( (np.asarray( i.resize(min_shape_path) ) for i in comb))

        imgs_path = Image.fromarray(imgs_path)
        imgs_path.save("Path.jpg")

        comb1_refresh()
        comb2_refresh()
        comb3_refresh()
        path_refresh()

        list_gen(output_path_12, new_test, repl_list_strt_idx, repl_list_end_idx)
        #print("the current path list: ", output_path_12)

        list_gen(output_path_12_num, new_com_test_count, repl_list_strt_idx, repl_list_end_idx)
        #print("the current number array: ", output_path_12_num)
        

        messagebox.showinfo("Information", "Generate Complete")

        com_test.clear()
        com_test_count.clear()


def onClick_Exit():
    #print("destory fram here")
    global stop_timer_threads
    global stop_clean_threads

    stop_timer_threads = True
    stop_clean_threads = True

    background_thread.join()
    clean_thread.join()

    trash.close()

    output_path_12_num_string = [str(int) for int in output_path_12_num]
    final_output_path = " ".join(output_path_12_num_string)

    output.write(str(final_output_path))
    output.close()

    output_pattern2path.write(str(output_path_12))
    output_pattern2path.close()

    t = datetime.datetime.now()
    current_time = t.strftime("%Y-%m-%d %H:%M:%S")
    history.write(str(current_time).strip() + " " + str(output_path_12).strip())
    history.write("\n")
    history.close()

    os.remove("trash.txt")

    root.destroy()
    print("function killed ")





def comb1_refresh():

    global canvas_enable
    global comb1_on

    if canvas_enable == 1: 
        test_pic1 = Image.open("Combination1.jpg")
        resize_test_pic1 = test_pic1.resize((300, 40), Image.ANTIALIAS)
        img_comb1 = ImageTk.PhotoImage(resize_test_pic1)
        img_view_comb1 = canvas_comb1.create_image(150, 30, image = img_comb1, anchor = CENTER)
        canvas_comb1.img = img_comb1
        comb1_on = 1
        
        canvas_comb1.after(200, comb1_refresh)



def comb2_refresh():
    global canvas_enable
    global comb2_on

    if canvas_enable == 2: 
        test_pic2 = Image.open("Combination2.jpg")
        resize_test_pic2 = test_pic2.resize((300, 40), Image.ANTIALIAS)
        img_comb2 = ImageTk.PhotoImage(resize_test_pic2)
        img_view_comb2 = canvas_comb2.create_image(150, 30, image = img_comb2, anchor = CENTER)
        canvas_comb2.img = img_comb2
        comb2_on = 1

        canvas_comb2.after(200, comb2_refresh)



def comb3_refresh():
    global canvas_enable
    global comb3_on

    if canvas_enable == 3:
        test_pic3 = Image.open("Combination3.jpg")
        resize_test_pic3 = test_pic3.resize((300, 40), Image.ANTIALIAS)
        img_comb3 = ImageTk.PhotoImage(resize_test_pic3)
        img_view_comb3 = canvas_comb3.create_image(150, 30, image = img_comb3, anchor = CENTER)
        canvas_comb3.img = img_comb3
        comb3_on = 1

        canvas_comb3.after(200, comb3_refresh)


def path_refresh():
    global comb1_on, comb2_on, comb3_on

    if (comb3_on & comb1_on & comb2_on) :

        path_pic = Image.open("Path.jpg")
        resize_path_pic = path_pic.resize((480, 40), Image.ANTIALIAS)
        img_path = ImageTk.PhotoImage(resize_path_pic)
        img_view_comb = canvas_path.create_image(240, 30, image = img_path, anchor = CENTER)
        canvas_path.img = img_path

        canvas_path.after(200, path_refresh)



def list_gen(old_list, new_list, repl_list_strt_idx, repl_list_end_idx):

    old_list[repl_list_strt_idx : repl_list_end_idx] = new_list
    new_list = old_list

    #print("new list is: ", new_list)



def comb_statue():
    test_label = Label(root, text = clicked.get())
    #test_label.grid(row = 6, column = 5)
    global currStr
    currStr = clicked.get()
    #print("in here, the text is: ", clicked.get())
    test_label.after(200, comb_statue)


def Comb_List_Clean():
    global oldstr
    global currStr

    count = 0
    while True:

        global stop_clean_threads

        if stop_clean_threads:
            print("clean thread ends")
            return 1
            break
        else:
            if (oldstr == currStr):
                count = ~count
                
                trash.seek(0)
                trash.write(currStr)

            if (oldstr != currStr):
                CombList.delete(0, END)
                com_test.clear()
                print("Delete pattern to array: ", com_test, "size of array", len(com_test))
                oldstr = currStr

        
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



# --- DEFAULT ---
img = ImageTk.PhotoImage(file = "default.jpg")
#bi.show()
canvas = Canvas(ListFrame, width = 40, height = 40)
canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)
#gif1 = bi
img_view = canvas.create_image(30, 30, image = img, anchor = CENTER)
#assigned the img to the canvas object
canvas.img = img

stop_timer_threads = False
stop_clean_threads = False

default()





# --- LIST ---
PatternList = Listbox(ListFrame, font = "Helvetica", height= 5, width = 20 )
PatternList.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10)

CombList = Listbox(ListFrame, font = "Helvetica", height= 5, width = 20 )
CombList.grid(row = 0, column = 8, columnspan = 5, padx=10, pady=10)

for PATTERN in ImageName:
    PatternList.insert(END, PATTERN)

PatternList.bind('<<ListboxSelect>>', buttonHandler)

# --- Button ---
Button_ADD = Button(ListFrame, text = "Add", width = 5, height = 2, command = onClick_Add)
Button_Delete = Button(ListFrame, text = "Delete", width = 5, height = 2, command = onClick_Delete)
Button_Delete_All = Button(ListFrame, text = "Delete All", width = 7, height = 2, command = onClick_Delete_All)
Button_Generate = Button(ListFrame, text = "Generate", width = 8, height = 2, command = onClick_Generate)
Button_Exit = Button(root, text = "Exit", width = 10, height = 2, command = onClick_Exit)


Button_ADD.grid(row = 5, column = 2, sticky = N)
Button_Delete.grid(row = 5, column = 3,sticky = N)
Button_Delete_All.grid(row = 5, column = 4, sticky = N)
Button_Generate.grid(row = 5, column = 10, sticky = N)
Button_Exit.grid(row = 10, column = 15, sticky = N)
 
# --- SCROLLBAR ---
scrobar = Scrollbar(ListFrame)
scrobar.grid(row = 0, column = 5, sticky= "ns")

scrobar.config( command = PatternList.yview )
PatternList.config(yscrollcommand=scrobar.set)

# --- Frame GRID ---
ListFrame.grid(row = 0, column = 0, columnspan = 10)
CombinationFrame.grid(row = 0, column = 10, padx = 20,  pady= 20)

# --- LABEL ---
Label1= Label(CombinationFrame, text =" Combination 1", font=("Arial", 15))
Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)

Label2= Label(CombinationFrame, text =" Combination 2", font=("Arial", 15))
Label2.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = N)

Label3= Label(CombinationFrame, text =" Combination 3", font=("Arial", 15))
Label3.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = N)

Label4 = Label(root, text = "Path", font=("Arial", 25))
Label4.grid(row = 7, column = 4, padx = 10, pady = 10, sticky = N)



# --- CANVAS ---
canvas_comb1 = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb1.grid(row = 0, column = 1, columnspan = 6, sticky = W)

canvas_comb2 = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb2.grid(row = 1, column = 1, columnspan = 6, sticky = W)

canvas_comb3 = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb3.grid(row = 2, column = 1, columnspan = 6, sticky = W)

canvas_path = Canvas(root, width = 480, height = 30)
canvas_path.grid(row = 7, column = 5, columnspan = 15, sticky = W)

#canvas_path = Canvas(root, )

# --- OPTION MEUN ---
clicked = StringVar()
clicked.set("Combination 1")
drop = OptionMenu(ListFrame, clicked, "Combination 1", "Combination 2", "Combination 3")
drop.grid(row = 5, column = 9)

oldstr = clicked.get()
currStr = clicked.get()

# --- THREAD ---
background_thread = Thread(target=timer)
background_thread.start()

clean_thread = Thread(target=Comb_List_Clean)
clean_thread.start()

# --- MAIN ---
comb_statue()





root.mainloop()