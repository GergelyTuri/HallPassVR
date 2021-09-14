"""Initializes the virtual environment using a Tk interface.
"""
from tkinter import *
import os
import time

# Create a new Tk interface and set the window geometry.
root = Tk()
root.geometry("10x10+2500+200")


def test_case():
	os.system("python3 vr_environment.py")
	time.sleep(0.001)
	root.destroy()


# Construct a button widget with the parent MASTER (root).
button = Button(root, text="button", width=10, height=10, command=test_case)

# Call the main loop in a Tkinter application.
root.wait_visibility()
test_case()
root.mainloop()
