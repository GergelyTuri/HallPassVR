from tkinter import *
#import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import os 

# --- DEFINE ---
root = Tk()
pathToImages = ["image/black.jpg",
"image/blue.jpg","image/green.jpg",
"image/red.jpg", "image/white.jpg"]



# --- FUNCTIONS ---
def buttonHandler(self):
    img = ImageTk.PhotoImage(file = pathToImages[int(mylist.curselection()[0])])
    #bi.show()
    canvas = Canvas(root, width = 50, height = 50)
    canvas.grid(row = 5, column = 0, columnspan = 1)
    #gif1 = bi
    img_view = canvas.create_image(30, 30, image = img, anchor = CENTER)
    #assigned the img to the canvas object
    canvas.img = img
    print("in here, color image is ", pathToImages[int(mylist.curselection()[0])])

# --- CREATE LIST ---
mylist = Listbox(root, font = "Helvetica", height= 5, width = 10 )

a = mylist.insert(END,str('black'))
b = mylist.insert(END,str('blue'))
c = mylist.insert(END,str('green'))
d = mylist.insert(END,str('red'))
e = mylist.insert(END,str("white"))
f = mylist.insert(END,str("purple"))
g = mylist.insert(END,str("yellow"))

mylist.bind('<<ListboxSelect>>', buttonHandler)

# --- CREATE SCROLLBAR ---
scrobar = Scrollbar(root)
scrobar.grid(row = 0, column = 5, sticky= "ns")
#mylist = Listbox(root, font = "Helvetica", height= 5, width = 10 )

# --- MAIN ---
mylist.grid(row = 0, column = 0, columnspan = 4)
scrobar.config( command = mylist.yview )

root.mainloop()