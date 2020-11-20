from classC import *
from Tkinter import *
import time

depth=999
c1=C(0,0) #juliaset

def numberOfIterations(c): #julia set
    r=0
    while True:
        c=c*c+c1
        if abs(c)>2: return r
        r+=1
        if r==depth: return r
    
def XnumberOfIterations(c): #mandelbrot set
    f=C(); r=0
    while True:
        f=f*f+c
        if abs(c)>2: return r
        r+=1
        if r==depth: return r

def createLine(i1,i2,n):
    color='#'+str(n/100)+str(n%100/10)+str(n%10)
    c.create_line(i1,i2,i1+1,i2+1,fill=color)

a=time.time()

Lx1=range(2,402)
Lx2=range(402,802)
Ly1=range(2,402)
Ly2=range(402,802)
w=Tk()
c=Canvas(w,width=800,height=800)
c.pack()
for i1 in Lx1:
    for i2 in Ly1:
        n=numberOfIterations(C(-0.005*(400-(i1-2)),0.005*(400-(i2-2))))
        createLine(i1,i2,n)
for i1 in Lx1:
    for i2 in Ly2:
        n=numberOfIterations(C(-0.005*(400-(i1-2)),-0.005*((i2-2)-400)))
        createLine(i1,i2,n)
for i1 in Lx2:
    for i2 in Ly1:
        n=numberOfIterations(C(0.005*((i1-2)-400),0.005*(400-(i2-2))))
        createLine(i1,i2,n)
for i1 in Lx2:
    for i2 in Ly2:
        n=numberOfIterations(C(0.005*((i1-2)-400),-0.005*((i2-2)-400)))
        createLine(i1,i2,n)

b=time.time()
print b-a

w.mainloop()
