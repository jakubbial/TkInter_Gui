from Gui_Elements import *


par = Parameters()
ran = Randomizer


def saveParameters():
    par.quantity = RandomCountEntry.GetEntryValue()
    par.min = MinEntry.GetEntryValue()
    par.max = MaxEntry.GetEntryValue()


def showParamiko():
    ran.randomizeThisShieet(ran, par.quantity, par.min, par.max)
    # ran.printThisSieet(ran)
    Graph.x = ran.x
    Graph.y = ran.y
    Graph.drawIt()
    CanvaGraph(root, ran.y, ran.x, 1, 3, 1, 20)
    plt.hist(ran.x, density='true', rwidth=0.1)
    plt.show()


root = Tk()


TopLabel = LabelText(root, 'Generator liczb losowych o zadanym rozkładzie', 0, 0, 3, 1)
LeftLabel = LabelText(root, 'Parametry:', 1, 0, 2, 1)
RandomCountParameter = LabelText(root, 'Ilość liczb losowych', 2, 0, 1, 1)
Min = LabelText(root, 'Low boundary:', 3, 0, 1, 1)
Max = LabelText(root, 'High boundary:', 4, 0, 1, 1)
RandomCountEntry = TextEntry(root, 2, 1, 10, 1, 1)
MinEntry = TextEntry(root, 3, 1, 10, 1, 1)
MaxEntry = TextEntry(root, 4, 1, 10, 1, 1)
ConfirmButton = OkButton(root, 'Save', 5, 0, saveParameters, 2, 1)
RandomizeButton = OkButton(root, 'Randomizuj', 6, 0, showParamiko, 2, 1)
Graph = CanvaGraph(root, ran.x, ran.y, 1, 3, 1, 20)

root.mainloop()
