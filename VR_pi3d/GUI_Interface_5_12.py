# --- GUI Interface 5/12/2021 ---
#Hongtao Cai - Columbia University 

#1) Generate drop menu for combination 
#2) Set combination pattern change Simultaneously
#3) Add background timer/clean comb list function using thread
#4) Finish rest 2 combination



from tkinter import *
#import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import numpy as np
from tkinter import messagebox
import time
from threading import Thread

# --- DEFINE ---
root = Tk()
pathToImages = ["image/black.jpg",
"image/blue.jpg","image/green.jpg",
"image/red.jpg", "image/white.jpg",
"image/purple.jpg", "image/yellow.jpg"]

ImageName = ["black", "blue", "green", "red", "white", "purple", "yellow"]

ListFrame = Frame(root)
CombinationFrame = Frame(root)

com_test = []
CombArry_size = 0


# --- FUNCTIONS ---
def buttonHandler(self):
    img = ImageTk.PhotoImage(file = pathToImages[int(PatternList.curselection()[0])])
    #bi.show()
    canvas = Canvas(ListFrame, width = 40, height = 40)
    canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)
    #gif1 = bi
    img_view = canvas.create_image(30, 30, image = img, anchor = CENTER)
    #assigned the img to the canvas object
    canvas.img = img
    #print("in here, color image is ", pathToImages[int(Pattern.curselection()[0])])

def onClick_Add():
    #print("Add botton, the iamge count: ", int(Pattern.curselection()[0]))
    Add_pattern = ImageName[int(PatternList.curselection()[0])]
    #print("Add botton, the iamge name: ", ImageName[int(Pattern.curselection()[0])])
    Comb_size = len(com_test)
    if Comb_size < 4:
        CombList.insert(END, Add_pattern)
        com_test.append(pathToImages[int(PatternList.curselection()[0])])
        print("Add pattern to arrat: ", com_test, "size of array", len(com_test))

    else:
        print("out of limit")
        print("Add pattern to arrat: ", com_test, "size of array", len(com_test))
        messagebox.showerror("Error", "Out of Limit")


def onClick_Delete():
    #print("Delete Button, the image count: ", int(mylist2.curselection()[0]))
    Delete_pattern = com_test[int(CombList.curselection()[0])]
    print("delete botton, the iamge name: ", com_test[int(CombList.curselection()[0])])
    CombList.delete(ANCHOR)
    com_test.remove(Delete_pattern)
    #print("what is Anchor: ", ANCHOR)
    print("Delete pattern to array: ", com_test, "size of array", len(com_test))



def onClick_Delete_All():
    #print("Delete Button, the image count: ", int(mylist2.curselection()[0]))
    Delete_pattern = ImageName[int(CombList.curselection()[0])]
    #print("Add botton, the iamge name: ", ImageName[int(mylist2.curselection()[0])])
    CombList.delete(0, END)
    com_test.clear()
    print("Delete pattern to array: ", com_test, "size of array", len(com_test))


def onClick_Generate():
    print("generate pattern here")
    print("array to generate: ", com_test)

    GenArry_size = len(com_test)

    global currStr
    #print("in generate function: ", currStr)

    if (currStr == "Combination 1"):
        patternname = "Combination1.jpg"
    elif (currStr == "Combination 2"):
        patternname = "Combination2.jpg"
    elif (currStr == "Combination 3"):
        patternname = "Combination3.jpg"

    if GenArry_size == 0:
        messagebox.showerror("Error", "Empty Pattern")
    elif GenArry_size < 4:
        messagebox.showwarning("Warning", "Need 4 Patterns")
    else:
        images = [Image.open(x) for x in com_test]

        # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in images])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in images) )

        # save that beautiful picture
        imgs_comb = Image.fromarray( imgs_comb)
        imgs_comb.save(patternname)
        messagebox.showinfo("Information", "Generate Complete")


def onClick_Exit():
    #print("destory fram here")
    global stop_timer_threads
    global stop_clean_threads

    stop_timer_threads = True
    stop_clean_threads = True

    root.destroy()
    #print("function killed ")





def comb1_refresh():
    test_pic1 = Image.open("Combination1.jpg")

    resize_test_pic1 = test_pic1.resize((300, 40), Image.ANTIALIAS)

    img_comb1 = ImageTk.PhotoImage(resize_test_pic1)

    img_view_comb1 = canvas_comb1.create_image(150, 30, image = img_comb1, anchor = CENTER)

    canvas_comb1.img = img_comb1

    canvas_comb1.after(200, comb1_refresh)



def comb2_refresh():
    test_pic2 = Image.open("Combination2.jpg")
    
    resize_test_pic2 = test_pic2.resize((300, 40), Image.ANTIALIAS)

    img_comb2 = ImageTk.PhotoImage(resize_test_pic2)

    img_view_comb2 = canvas_comb2.create_image(150, 30, image = img_comb2, anchor = CENTER)

    canvas_comb2.img = img_comb2

    canvas_comb2.after(200, comb2_refresh)



def comb3_refresh():
    test_pic3 = Image.open("Combination3.jpg")

    resize_test_pic3 = test_pic3.resize((300, 40), Image.ANTIALIAS)

    img_comb3 = ImageTk.PhotoImage(resize_test_pic3)

    img_view_comb3 = canvas_comb3.create_image(150, 30, image = img_comb3, anchor = CENTER)

    canvas_comb3.img = img_comb3

    canvas_comb3.after(200, comb3_refresh)

def comb_statue():
    test_label = Label(root, text = clicked.get())
    test_label.grid(row = 6, column = 5)
    global currStr
    currStr = clicked.get()
    #print("in here, the text is: ", clicked.get())
    test_label.after(200, comb_statue)


def Comb_List_Clean():
    global oldstr
    global currStr
    #print("current str-in comb_list_clean: ", oldstr)
    #print("current str-in comb_list_clean: ", currStr)
    count = 0
    while True:
        #print("current str: ", currStr)
        #print("old str: ", oldstr)

        global stop_clean_threads

        if stop_clean_threads:
            print("clean thread ends")
            return 1
            break
        else:
            if oldstr == currStr:
                #count = ~count
                #print("In combination ", currStr) 
                return 0
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
img = ImageTk.PhotoImage(file = "image/default.jpg")
#bi.show()
canvas = Canvas(ListFrame, width = 40, height = 40)
canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)
#gif1 = bi
img_view = canvas.create_image(30, 30, image = img, anchor = CENTER)
#assigned the img to the canvas object
canvas.img = img

stop_timer_threads = False
stop_clean_threads = False





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
Button_Exit.grid(row = 10, column = 20, sticky = N)
 
# --- SCROLLBAR ---
scrobar = Scrollbar(ListFrame)
scrobar.grid(row = 0, column = 5, sticky= "ns")

scrobar.config( command = PatternList.yview )
PatternList.config(yscrollcommand=scrobar.set)

# --- Frame GRID ---
ListFrame.grid(row = 0, column = 0, columnspan = 10)
CombinationFrame.grid(row = 0, column = 10, padx = 20,  pady= 20)

# --- LABEL ---
Label1= Label(CombinationFrame, text =" Combination 1")
Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)

Label2= Label(CombinationFrame, text =" Combination 2")
Label2.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = N)

Label3= Label(CombinationFrame, text =" Combination 3")
Label3.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = N)

Label4 = Label(root, text = "Path")
Label4.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = N)



# --- CANVAS ---
canvas_comb1 = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb1.grid(row = 0, column = 1, columnspan = 6, sticky = W)

canvas_comb2 = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb2.grid(row = 1, column = 1, columnspan = 6, sticky = W)

canvas_comb3 = Canvas(CombinationFrame, width = 300, height = 30)
canvas_comb3.grid(row = 2, column = 1, columnspan = 6, sticky = W)

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
comb1_refresh()
comb2_refresh()
comb3_refresh()

comb_statue()





root.mainloop()