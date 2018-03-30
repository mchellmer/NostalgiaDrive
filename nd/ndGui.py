#!/usr/bin/python3
from tkinter import *


class NdGui:
    """Generates an interface for the user to make selections"""
    # Constructor

    def __init__(self):
        print("I am the guuuu")
        # self.genGui()
        self.genSelect()

    # Attributes
    ndMain = Tk()
    pad = 3
    _geom = '200x200+0+0'
    ndMain.geometry("{0}x{1}+0+0".format(
        ndMain.winfo_screenwidth() - pad, ndMain.winfo_screenheight() - pad))

    # Methods
    # Generate opening screen
    def genGui(self):
        selections = ["Just Play!", "Prepare to Die", "Choose Something", "Something New"]
        commands = ["", "", "", ""]
        directions = [LEFT, TOP, RIGHT, BOTTOM]

        frame = Frame(self.ndMain)

        for i in range(0, 4):
            Button(frame, text=selections[i]).pack(side=directions[i])

        frame.pack(fill=BOTH, expand=YES)

        self.ndMain.mainloop()

    # Generate selection screen (number of players, genre, rating, popularity)
    def genSelect(self):
        players = ["1", "2", "3", "4"]

        self.genChecks(0, players)

        self.ndMain.mainloop()

    def genChecks(self, col, entries=[]):
        cButtons = []
        for i in range(0, len(entries)):
            CheckVar = IntVar()
            cButton = Checkbutton(self.ndMain, text=entries[i], variable=CheckVar, onvalue=1, offvalue=0, height=5, width=20)
            cButtons.append(cButton.grid(row=i, column=col))

        for i in range(0, len()):
            cButtons[i].pack()
