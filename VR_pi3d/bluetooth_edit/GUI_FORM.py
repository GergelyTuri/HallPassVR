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
root.geometry("1450x600") # set size of window


Path              = ["Combination1.jpg", "Combination2.jpg", "Combination3.jpg"]


ListFrame         = Frame(root, background= '#10ccef')
CombinationFrame  = Frame(root, background= '#c9b5fa')
HistoryComb       = Frame(root, background= '#0a5cf5')
Input             = Frame(root, background= '#9714eb')



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


    #file_list  = os.listdir(string_dir)

     
    pathToImages     = []
    ImageName        = []
    ImageNumCount    = []
    path2historyComb = []

    size_pattern = (40,40)
    size_comb    = (300,30)
    size_path    = (480,30)

    ImageName     = {'Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift'}
    
   
   
    

    
# --- DEFAULT ---
canvas = Canvas(ListFrame, width = 65, height = 40, background= '#6251ae')
canvas.grid(row = 5, column = 0, columnspan = 1, sticky = W)

canvas2 = Canvas(ListFrame, width = 40, height = 40, background= '#51c03f')
canvas2.grid(row = 5, column = 1, columnspan = 1, sticky = W)

#img_resize_canvas("default.jpg", (65,40), canvas)

stop_timer_threads = False
stop_clean_threads = False

default()




# --- LIST ---
PatternList = Listbox(ListFrame,   font = "Helvetica", height = 5, width = 30, background= 'grey')
CombList    = Listbox(ListFrame,   font = "Helvetica", height = 5, width = 30, background= '#1ecbe1')
HistoryList = Listbox(HistoryComb, font = "Helvetica", height = 5, width = 35 )

CombList.grid   (row = 0, column = 8, columnspan = 5, padx=10, pady=10, sticky = W)
PatternList.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10, sticky = W)
HistoryList.grid(row = 0, column = 0, columnspan = 5, padx=10, pady=10, sticky = W)




for PATTERN in ImageName:
    PatternList.insert(END, PATTERN)

#PatternList.bind('<<ListboxSelect>>', buttonHandler)
#HistoryList.bind('<<ListboxSelect>>', buttonHandler_History)

# --- Button ---
Button_ADD        = Button(ListFrame,   text = "Add",        width = 5,  height = 2)
Button_Delete     = Button(ListFrame,   text = "Delete",     width = 5,  height = 2)
Button_Delete_All = Button(ListFrame,   text = "Delete All", width = 7,  height = 2)
Button_Generate   = Button(ListFrame,   text = "Generate",   width = 8,  height = 2)
Button_Exit       = Button(root,        text = "Exit",       width = 10, height = 2)
Button_Upload     = Button(HistoryComb, text = "Upload",     width = 7,  height = 2)
Button_Delete_hi  = Button(HistoryComb, text = "Delete",     width = 7,  height = 2)
Button_Del_hi_all = Button(HistoryComb, text = "Delete All", width = 10, height = 2)
Button_Input      = Button(Input,       text = "Read",       width = 7,  height = 2)
Button_Start      = Button(root,        text = "Start",      width = 10, height = 2)
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
Label4 = Label(CombinationFrame,  text =" Path",                  font = ("Arial", 15))
Label5 = Label(HistoryComb,       text =" Combination   ",           font = ("Arial", 15))
Label6 = Label(Input,             text =" Path Name",             font = ("Arial", 10))
Label7 = Label(Input,             text =" Path Length(m)",        font = ("Arial", 10))

Label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = N)
Label2.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = N)
Label3.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = N)
Label4.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = W)
Label5.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = W)
Label6.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = W)
Label7.grid(row = 0, column = 2, padx = 15, pady = 15, sticky = W)



# --- CANVAS ---
canvas_comb1        = Canvas(CombinationFrame, width = 300, height = 30, bg = 'red')
canvas_comb2        = Canvas(CombinationFrame, width = 300, height = 30, bg = 'blue')
canvas_comb3        = Canvas(CombinationFrame, width = 300, height = 30, bg = 'green')
canvas_path         = Canvas(CombinationFrame, width = 480, height = 30, bg = 'yellow')
canvas_history_comb = Canvas(HistoryComb,      width = 300, height = 30, bg = 'black')

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
#background_thread = Thread(target=timer)
#background_thread.start()

#clean_thread = Thread(target=Comb_List_Clean)
#clean_thread.start()

# --- MAIN ---
#comb_statue()
#history_comb_read()
root.mainloop()



# --- TODO ---
#1) Easter Egg!