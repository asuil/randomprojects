from random import randint
from Tkinter import *

def pickRand():
    return str(randint(0,1))+str(randint(0,1))+\
           str(randint(0,1))+str(randint(0,1))

def drawLine(lu):
    canvas.create_line(cursor[0]-10,cursor[1]-10,\
                       cursor[0]+10,cursor[1]+10)
    canvas.create_line(cursor[0]+10,cursor[1]-10,\
                       cursor[0]-10,cursor[1]+10)

cursor=[640,360]

window=Tk()
canvas=Canvas(window,width=1280,height=720); canvas.pack()

lu=pickRand()
drawLine(lu)    

window.mainloop()
