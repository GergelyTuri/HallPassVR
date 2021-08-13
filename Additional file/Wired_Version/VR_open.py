from tkinter import *
import os
import time

root = Tk()

root.geometry("10x10+2500+200")

def test_case():
	os.system('python Corridor_demo_7_2.py')
	time.sleep(0.001)
	root.destroy()

button = Button(root, text = "button", width = 10, height = 10, command = test_case)

root.wait_visibility()
test_case()
root.mainloop()

