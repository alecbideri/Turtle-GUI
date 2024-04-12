from turtle import *
import random


## chatGpt version
# pensize(15)
# for i in range(100):
#     steps = int(random.random() * 100)
#     angle = int(random.random() * 360)
#     forward(steps)
#     color(random.random(), random.random(), random.random())  # Set a random RGB color
#     right(angle)
#
# mainloop()  # Keep the window open until manually closed


colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    r_color = (r,g,b)
    return r_color


directions = [0,90,180,270]
pensize(15)
speed("fastest")

for _ in range(200):
    color(random_color())
    forward(30)
    setheading(random.choice(directions))
exitonclick()