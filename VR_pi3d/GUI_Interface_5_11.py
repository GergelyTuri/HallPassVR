# --- GUI Interface 5/11/2021 ---
#Hongtao Cai
#1)Fix srollbar   
#2)Fix layout  
#3)Generate Delete_All, Delete, Add, Generate button 
#4)Generate pattern pic


from tkinter import *
#import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import numpy as np
from tkinter import messagebox

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
    Delete_pattern = ImageName[int(mylist2.curselection()[0])]
    #print("Add botton, the iamge name: ", ImageName[int(mylist2.curselection()[0])])
    CombList.delete(0, END)
    com_test.clear()
    print("Delete pattern to array: ", com_test, "size of array", len(com_test))


def onClick_Generate():
    print("generate pattern here")
    print("array to generate: ", com_test)

    GenArry_size = len(com_test)

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
        imgs_comb.save( 'Combination.jpg' )
        messagebox.showinfo("Information", "Generate Complete")

# --- LIST ---
PatternList = Listbox(ListFrame, font = "Helvetica", height= 5, width = 20 )
PatternList.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10)

CombList = Listbox(ListFrame, font = "Helvetica", height= 5, width = 20 )
CombList.grid(row = 0, column = 8, columnspan = 5, padx=10, pady=10)

for PATTERN in ImageName:
    PatternList.insert(END, PATTERN)

PatternList.bind('<<ListboxSelect>>', buttonHandler)

# --- LABEL ---


# --- Button ---
Button_ADD = Button(ListFrame, text = "Add", width = 5, height = 2, command = onClick_Add)
Button_Delete = Button(ListFrame, text = "Delete", width = 5, height = 2, command = onClick_Delete)
Button_Delete_All = Button(ListFrame, text = "Delete All", width = 7, height = 2, command = onClick_Delete_All)
Button_Generate = Button(ListFrame, text = "Generate", width = 8, height = 2, command = onClick_Generate)


Button_ADD.grid(row = 5, column = 2, sticky = N)
Button_Delete.grid(row = 5, column = 3,sticky = N)
Button_Delete_All.grid(row = 5, column = 4, sticky = N)
Button_Generate.grid(row = 5, column = 10, sticky = N)
 
# --- SCROLLBAR ---
scrobar = Scrollbar(ListFrame)
scrobar.grid(row = 0, column = 5, sticky= "ns")

scrobar.config( command = PatternList.yview )
PatternList.config(yscrollcommand=scrobar.set)

# --- Frame GRID ---
ListFrame.grid(row = 0, column = 0, columnspan = 10)


# --- DEFAULT ---
img = ImageTk.PhotoImage(file = "image/default.jpg")
#bi.show()
canvas = Canvas(ListFrame, width = 40, height = 40)
canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)
#gif1 = bi
img_view = canvas.create_image(30, 30, image = img, anchor = CENTER)
#assigned the img to the canvas object
canvas.img = img


# --- MAIN ---
root.mainloop()


