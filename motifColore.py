from turtle import *
from math import *

def carre(longCote):
    down()
    for i in range(4):
        forward(longCote)
        right(90)
    up()
    
def triangle(longCote):
    down()
    for i in range(3):
        forward(longCote)
        right(120)
    up()

def triangleJaune (longCote):
    fillcolor("yellow")
    begin_fill()
    triangle(longCote)
    end_fill()

def carreRouge (longCote):
    fillcolor("red")
    begin_fill()
    carre(longCote)
    end_fill()

def motif (longCote):
    carreRouge(longCote)
    triangleJaune(longCote)
    forward(longCote)
    
if __name__=='__main__':
    #execution plus rapide
    motif(200)