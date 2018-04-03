#!/usr/bin/python3
from tkinter import *
import os
import datetime


class NdGui:
    """Generates an interface for the user to make selections"""
    # Constructor

    def __init__(self):
        print("GUI Constructed")
        self.genGui()

    # Attributes
    key = 1
    ndMain = Tk()
    pad = 3
    _geom = '200x200+0+0'
    ndMain.geometry("{0}x{1}+0+0".format(
        ndMain.winfo_screenwidth() - pad, ndMain.winfo_screenheight() - pad))

    selections = {}

    # Methods
    # Generate opening screen
    def genGui(self):
        options = ["Just Play!", "Prepare to Die", "Choose Something", "Something New"]
        rows = [1, 0, 1, 2]
        cols = [0, 1, 2, 1]

        dOptions = {}

        for i in range(0, 4):
            b = Button(self.ndMain, text=options[i], command=self.goSelect)
            b.grid(row=rows[i], column=cols[i])
            dOptions['option'] = options[i]
            dOptions['button'] = b

        self.ndMain.mainloop()

    def optionInterpret(self, index):
        if index == 0:
            self.genRandomGame()
        elif index == 1:
            self.genHardGame()

    def genRandomGame():
        print("Returning a Random Game")

    def genHardGame():
        print("Returning a Difficult Game")

    # Generate selection screen (number of players, genre, rating, popularity)
    def genSelect(self):
        b = Button(self.ndMain, text="PLAY!", command=self.goPlay)
        b.grid(row=0, column=0)
        b = Button(self.ndMain, text="BACK!", command=self.goBack)
        b.grid(row=1, column=0)

        genres = self.getTextOptions('genres')
        labels = ["Players", "Genres", "Ratings", "", "Popular In"]
        players = self.getTextOptions('players')
        popularity = ["USA", "JAPAN", "EUROPE", "ELSEWHERE", "...NOWHERE"]

        for i in range(len(labels)):
            Label(self.ndMain, text=labels[i]).grid(row=0, column=i + 1)

        self.genChecks(0, 'players', players)
        self.genChecks(1, 'genres', genres)
        self.genRating(2)
        self.genChecks(4, 'popularity', popularity)

        self.ndMain.mainloop()

    def genChecks(self, col, type, entries=[]):
        for i in range(0, len(entries)):
            CheckVar = BooleanVar()
            cButton = Checkbutton(self.ndMain, text=entries[i], variable=CheckVar, height=5, width=20)
            cButton.grid(row=i + 1, column=col + 1)

            entry = {'entry': {'type': 'check', 'data': type, 'text': cButton['text'], 'val': CheckVar}}
            self.selections[self.key] = entry
            self.key += 1

    # TODO: dynamic selection as MIN/MAX can clash, DRY
    def genRating(self, col):
        minLabel = Label(self.ndMain, text="Min").grid(row=1, column=col + 1)
        maxLabel = Label(self.ndMain, text="Max").grid(row=2, column=col + 1)

        a = list(range(11))
        varMin = IntVar(self.ndMain)
        varMin.set(0)
        varMax = IntVar(self.ndMain)
        varMax.set(10)
        oMenuMin = OptionMenu(self.ndMain, varMin, *a)
        oMenuMin.grid(row=1, column=col + 2)

        oMenuMax = OptionMenu(self.ndMain, varMax, *a)
        oMenuMax.grid(row=2, column=col + 2)

        entry = {'entry': {'type': 'Option', 'data': 'rating', 'text': 'Min', 'val': varMin}}
        self.selections[self.key] = entry
        self.key += 1
        entry = {'entry': {'type': 'Option', 'data': 'rating', 'text': 'Max', 'val': varMax}}
        self.selections[self.key] = entry
        self.key += 1

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
        # print(self.selections[2]['entry']['val'].get())
        outpath = os.path.join('docs', 'log.txt')
        file = open(outpath, 'w')
        now = datetime.datetime.now()
        file.write('\n' + str(now) + ': Start Selections' + '\n')
        for i in range(1, len(self.selections) + 1):
            col = self.selections[i]['entry']['data']
            item = self.selections[i]['entry']['text']
            val = self.selections[i]['entry']['val'].get()
            file.write(col + ' ' + item + ' ' + str(val) + '\n')

        file.write('End Selections' + '\n')
        self.ndMain.destroy()

    def getTextOptions(self, item):
        filename = item + '.txt'
        gPath = os.path.join('docs', 'selections', filename)
        f = open(gPath, 'r')
        lines = f.readlines()[:-1]
        lines.sort()
        return [x.strip() for x in lines]
