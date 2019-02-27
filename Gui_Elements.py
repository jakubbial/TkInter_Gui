from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from random import randint, normalvariate
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


class OkButton:
    def __init__(self, parentref, buttontext, gridrow, gridcolumn, function, colspan, rospan):
        Button(parentref, text=buttontext, command=function).grid(row=gridrow, column=gridcolumn, columnspan=colspan,
                                                                  rowspan=rospan)


class LabelText:
    labeltext = Label

    def __init__(self, parentref, labeltext, labelrow, labelcolumn, colspan, rospan):
        self.labeltext = Label(parentref, text=labeltext, justify=CENTER)
        self.labeltext.grid(row=labelrow, column=labelcolumn, columnspan=colspan, rowspan=rospan)

    def ChangeLabelText(self, text):
        self.labeltext.config(text=text)


class TextEntry:
    textentry = Entry

    def __init__(self, parentref, entryrow, entrycolumn, entrywidth, colspan, rospan):
        self.textentry = Entry(parentref, width=entrywidth)
        self.textentry.grid(row=entryrow, column=entrycolumn, columnspan=colspan, rowspan=rospan)

    def GetEntryValue(self):
        value = self.textentry.get()
        return value


class CanvaGraph:

    x = []
    y = []

    fram = Frame
    fig = Figure
    canvas = Canvas
    a = Figure.add_subplot

    def __init__(self, parentref, x, y, graphrow, graphcolumn, colspan, rospan):
        self.fram = Frame(parentref, bg='grey')
        self.fig = Figure(figsize=(6, 6))
        self.a = self.fig.add_subplot(111)
        self.a.plot(x, y, 'ro')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fram)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.fram.grid(row=graphrow, column=graphcolumn, columnspan=colspan, rowspan=rospan)

    def drawIt(self):
        self.canvas.draw()
        print('I am drawing')


class Parameters:
    quantity = ''
    min = ''
    max = ''

    def __init__(self):
        self.quantity = ''
        self.min = ''
        self.max = ''

    def saveParameters(self, quantity, max, min):
        self.quantity = quantity
        self.max = max
        self.min = min

    def showParamiko(self):
        print('tekst')
        print(self.quantity)
        print(self.max)
        print(self.min)


class Randomizer:
    x = []
    y = []

    def randomizeThisShieet(self, quantity, min, max):
        self.x.clear()
        self.y.clear()
        for zmienna in range(0, int(quantity)):
            self.x.append(normalvariate(int(min), int(max)))
            self.y.append(zmienna)

    def printThisSieet(self):
        print(self.x)
        print(self.y)
