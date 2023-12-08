#Haus vom Nikolaus

from turtle import *
from math import sqrt
speed(3)

distanz = int(numinput("Distanz","Wie hoch soll ihre Distanz sein?"))
striche = int(numinput("Striche","Wie viele Striche soll ihre Linie haben?"))

def nikolaus(distanz,striche):
    lt(90)
    strichel(distanz,striche)
    rt(90)
    strichel(distanz,striche)
    lt(120)
    strichel(distanz,striche)
    lt(120)
    strichel(distanz,striche)
    lt(75)
    strichel(distanz*sqrt(2),striche)
    lt(135)
    strichel(distanz,striche)
    lt(135)
    strichel(distanz*sqrt(2),striche)
    lt(135)
    strichel(distanz,striche)

def strichel(distanz,striche):
    spruenge = striche - 1
    strich = distanz / (striche + spruenge)
    for i in range(spruenge):
        fd(strich)
        hopp(strich)
    fd(strich)

def hopp(strich):
    penup()
    forward(strich)
    pendown()

nikolaus(distanz,striche)

done()