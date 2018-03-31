#!/usr/bin/python3
from tkinter import *
import os


class NdGui:
    """Generates an interface for the user to make selections"""
    # Constructor

    def __init__(self):
        print("I am the guuuu")
        self.genGui()

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
        rows = [1, 0, 1, 2]
        cols = [0, 1, 2, 1]

        for i in range(0, 4):
            b = Button(self.ndMain, text=selections[i], command=self.goSelect)
            b.grid(row=rows[i], column=cols[i])

        self.ndMain.mainloop()

    # Generate selection screen (number of players, genre, rating, popularity)
    def genSelect(self):
        b = Button(self.ndMain, text="PLAY!", command=self.goPlay)
        b.grid(row=0, column=0)
        b = Button(self.ndMain, text="BACK!", command=self.goBack)
        b.grid(row=1, column=0)

        gPath = os.path.join('docs', 'genres.txt')
        f = open(gPath, 'r')
        lines = f.readlines()
        genres = [x.strip() for x in lines]
        labels = ["Players", "Genres", "Ratings", "", "Popular In"]
        players = ["1", "2", "3", "4"]
        ratings = ["USA", "JAPAN", "EUROPE", "ELSEWHERE", "...NOWHERE"]

        for i in range(len(labels)):
            Label(self.ndMain, text=labels[i]).grid(row=0, column=i + 1)

        self.genChecks(0, players)
        self.genChecks(1, genres)
        self.genRating(2)
        self.genChecks(4, ratings)

        self.ndMain.mainloop()

    def genChecks(self, col, entries=[]):
        cButtons = []
        for i in range(0, len(entries)):
            CheckVar = IntVar()
            cButton = Checkbutton(self.ndMain, text=entries[i], variable=CheckVar, onvalue=1, offvalue=0, height=5, width=20)
            cButtons.append(cButton.grid(row=i + 1, column=col + 1))

    # TODO: dynamic selection as MIN/MAX can clash
    def genRating(self, col):
        Label(self.ndMain, text="Min").grid(row=1, column=col + 1)
        Label(self.ndMain, text="Max").grid(row=2, column=col + 1)

        a = list(range(11))
        varMin = IntVar(self.ndMain)
        varMin.set(0)
        varMax = IntVar(self.ndMain)
        varMax.set(10)
        oMenu = OptionMenu(self.ndMain, varMin, *a)
        oMenu.grid(row=1, column=col + 2)

        oMenu = OptionMenu(self.ndMain, varMax, *a)
        oMenu.grid(row=2, column=col + 2)

    def goSelect(self):
        widgets = self.ndMain.grid_slaves()
        for widget in widgets:
            widget.grid_forget()

        self.genSelect()

    def goBack(self):
        widgets = self.ndMain.grid_slaves()
        for widget in widgets:
            widget.grid_forget()

        self.genGui()

    def goPlay(self):
        widgets = self.ndMain.grid_slaves()
        print(widgets)
        for w in widgets:
            print(w.text.get())
