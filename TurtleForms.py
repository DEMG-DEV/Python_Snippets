from turtle import *
from random import *

speed(10)

forward(100)
right(120)
forward(100)
right(120)
forward(100)

color('red')
for i in range(6):
    forward(100)
    right(60)

color('green')
cont = 0
value = True
while value:
    forward(2)
    right(2)
    cont+=1
    if cont == 180:
        value=False

right(-45)
color('blue')
lenght = 0
for i in range(300):
    forward(lenght)
    right(15)
    lenght = lenght + 0.1

color('orange')
for i in range(4):
    forward(100)
    right(90)

colours = ['red', 'green', 'blue', 'magenta']
for i in range(360):
    forward(100)
    backward(100)
    right(1)
    color(choice(colours))
