#Haus vom Nikolaus

from turtle import *
from math import sqrt
speed(3)

distanz = int(numinput("Distanz","Wie hoch soll ihre Distanz sein?"))
winkel = int(numinput("Sprungwinkel","Wie groß soll ihr Sprungwinkel sein?"))
jump_distanz = int(numinput("Sprungdistanz","Wie hoch soll ihre Sprungdistanz sein?"))

def nikolaus(distanz):
    lt(90)
    fd(distanz)
    rt(90)
    fd(distanz)
    lt(120)
    fd(distanz)
    lt(120)
    fd(distanz)
    lt(75)
    fd(distanz*sqrt(2))
    lt(135)
    fd(distanz)
    lt(135)
    fd(distanz*sqrt(2))
    lt(135)
    fd(distanz)

def jump(jump_distanz,winkel):
    penup()
    right(winkel)
    forward(jump_distanz)
    left(winkel)
    pendown()

nikolaus(distanz)
jump(jump_distanz,winkel)
nikolaus(distanz)

done()