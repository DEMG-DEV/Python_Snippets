import math
import random
import turtle

numPts = 6
frac = 0.33
numDots = 30000
angle = 2*math.pi/numPts
points = [[300*math.sin(angle*i), 300*math.cos(angle*i)]
          for i in range(numPts)]
pos = [0, 300]
t = turtle.Turtle()
t.penup()
t.speed(0)
for i in range(numDots):
    point = random.choice(points)
    pos = [frac*pos[i]+(1-frac)*point[i] for i in range(2)]
    t.goto(pos[0], pos[1])
    t.dot(2)

input("Hit return to quit\n")

import math
import random
import turtle

numPts = 6
frac = 0.33
numDots = 30000
angle = 2*math.pi/numPts
points = [[300*math.sin(angle*i), 300*math.cos(angle*i)]
          for i in range(numPts)]
pos = [0, 300]
t = turtle.Turtle()
t.penup()
for i in range(numDots):
    point = random.choice(points)
    pos = [frac*pos[i]+(1-frac)*point[i] for i in range(2)]
    t.goto(pos[0], pos[1])
    t.dot(2)
input("Hit return to quit\n")
