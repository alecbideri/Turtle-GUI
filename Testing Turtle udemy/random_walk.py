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



colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]
pensize(15)
speed("fastest")

for _ in range(200):
    color(random.choice(colours))
    forward(30)
    setheading(random.choice(directions))
exitonclick()