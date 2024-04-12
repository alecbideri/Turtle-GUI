from turtle import *
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    r_color = (r,g,b)
    return r_color

colormode(255)
angle = 0
speed("fastest")

for _ in range(200):
    color(random_color())
    circle(100)
    left(10)

exitonclick()