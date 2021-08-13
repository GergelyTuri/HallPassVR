from tkinter import *

root = Tk()

readfile = open("corridor_file_write.txt", "r")
sentence = readfile.readline()
label = Label(text = sentence)
label.pack()

root.mainloop()