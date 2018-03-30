#!/usr/bin/python3
from tkinter import *


class NdGui:
    """Generates an interface for the user to make selections"""
    # Constructor

    def __init__(self):
        print("I am the guuuu")
        self.genGui(self.ndFrame)

    # Attributes
    # ndMain = tkinter.Tk()
    ndMain = Tk()
    ndFrame = Frame(ndMain)
    pad = 3
    _geom = '200x200+0+0'
    ndMain.geometry("{0}x{1}+0+0".format(
        ndMain.winfo_screenwidth() - pad, ndMain.winfo_screenheight() - pad))

    # Methods
    def genGui(self, frame):

        selections = ["Just Play!", "Prepare to Die", "Choose Something", "Something New"]
        commands = ["", "", "", ""]
        directions = [LEFT, TOP, RIGHT, BOTTOM]

        for i in range(0, 4):
            Button(frame, text=selections[i]).pack(side=directions[i])

        frame.pack(fill=BOTH, expand=YES)

        self.ndMain.mainloop()
