import random
import turtle

#1 -> abierto
#0 -> cerrado
#L00=w,a,s,d
L01=[1,1,1,1]
L02=[1,1,1,0]
L03=[1,1,0,1]
L04=[1,0,1,1]
L05=[0,1,1,1]
L06=[1,1,0,0]
L07=[1,0,1,0]
L08=[1,0,0,1]
L09=[0,1,1,0]
L10=[0,1,0,1]
L11=[0,0,1,1]
L12=[0,0,0,1]
L13=[0,0,1,0]
L14=[0,1,0,0]
L15=[1,0,0,0]

#posibles caminos a generar desde un s
#osea, donde w esta abierto
def select_s():
    a=random.randint(1,8)
    if a==1: return [L01[0],L01[1],L01[2],L01[3]]
    if a==2: return [L02[0],L02[1],L02[2],L02[3]]
    if a==3: return [L03[0],L03[1],L03[2],L03[3]]
    if a==4: return [L04[0],L04[1],L04[2],L04[3]]
    if a==5: return [L06[0],L06[1],L06[2],L06[3]]
    if a==6: return [L07[0],L07[1],L07[2],L07[3]]
    if a==7: return [L08[0],L08[1],L08[2],L08[3]]
    if a==8: return [L15[0],L15[1],L15[2],L15[3]]
    
#posibles caminos a generar desde un w
#osea, donde s esta abierto
def select_w():
    a=random.randint(1,8)
    if a==1: return [L01[0],L01[1],L01[2],L01[3]]
    if a==2: return [L02[0],L02[1],L02[2],L02[3]]
    if a==3: return [L04[0],L04[1],L04[2],L04[3]]
    if a==4: return [L05[0],L05[1],L05[2],L05[3]]
    if a==5: return [L07[0],L07[1],L07[2],L07[3]]
    if a==6: return [L09[0],L09[1],L09[2],L09[3]]
    if a==7: return [L11[0],L11[1],L11[2],L11[3]]
    if a==8: return [L13[0],L13[1],L13[2],L13[3]]

#posibles caminos a generar desde un d
#osea, donde a esta abierto
def select_d():
    a=random.randint(1,8)
    if a==1: return [L01[0],L01[1],L01[2],L01[3]]
    if a==2: return [L02[0],L02[1],L02[2],L02[3]]
    if a==3: return [L03[0],L03[1],L03[2],L03[3]]
    if a==4: return [L05[0],L05[1],L05[2],L05[3]]
    if a==5: return [L06[0],L06[1],L06[2],L06[3]]
    if a==6: return [L09[0],L09[1],L09[2],L09[3]]
    if a==7: return [L10[0],L10[1],L10[2],L10[3]]
    if a==8: return [L14[0],L14[1],L14[2],L14[3]]

#posibles caminos a generar desde un a
#osea, donde d esta abierto
def select_a():
    a=random.randint(1,8)
    if a==1: return [L01[0],L01[1],L01[2],L01[3]]
    if a==2: return [L03[0],L03[1],L03[2],L03[3]]
    if a==3: return [L04[0],L04[1],L04[2],L04[3]]
    if a==4: return [L05[0],L05[1],L05[2],L05[3]]
    if a==5: return [L08[0],L08[1],L08[2],L08[3]]
    if a==6: return [L10[0],L10[1],L10[2],L10[3]]
    if a==7: return [L11[0],L11[1],L11[2],L11[3]]
    if a==8: return [L12[0],L12[1],L12[2],L12[3]]
    
#turtlea la pieza de laberinto
def printLabyrinth(L00):
    if L00[0]==1:
        turtle.left(90)
        turtle.forward(10)
        turtle.left(180)
        turtle.forward(10)
        turtle.left(90)
    if L00[1]==1:
        turtle.left(180)
        turtle.forward(10)
        turtle.left(180)
        turtle.forward(10)
    if L00[3]==1:
        turtle.forward(10)
        turtle.left(180)
        turtle.forward(10)
        turtle.left(180)
    if L00[2]==1:
        turtle.right(90)
        turtle.forward(10)
        turtle.right(180)
        turtle.forward(10)
        turtle.right(90)

#True si la coordenada no esta usada
def coordenada(x,y,coord):
    if coord=="end":
        return True
    elif [x,y]==coord[0]:
        return False
    else:
        return coordenada(x,y,coord[1])

#genera ramas del laberinto
def creator(L00,c=1,x=0,y=0,coord=[[0,0],"end"]):
    printLabyrinth(L00)
    if c==10:
        return coord
    if L00[0]==1 and coordenada(x,y+1,coord):
        coord=[[x,y+1],coord]
        L1=select_w()
        L1[2]=0
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        coord=creator(L1,c+1,x,y+1,coord)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
    if L00[1]==1 and coordenada(x-1,y,coord):
        coord=[[x-1,y],coord]
        L2=select_a()
        L2[3]=0
        turtle.left(180)
        turtle.forward(20)
        turtle.right(180)
        coord=creator(L2,c+1,x-1,y,coord)
        turtle.forward(20)
    if L00[2]==1 and coordenada(x,y-1,coord):
        coord=[[x,y-1],coord]
        L3=select_s()
        L3[0]=0
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        coord=creator(L3,c+1,x,y-1,coord)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
    if L00[3]==1 and coordenada(x+1,y,coord):
        coord=[[x+1,y],coord]
        L4=select_d()
        L4[1]=0
        turtle.forward(20)
        coord=creator(L4,c+1,x+1,y,coord)
        turtle.right(180)
        turtle.forward(20)
        turtle.left(180)
    return coord
    
creator(L01)
