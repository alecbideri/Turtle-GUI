from turtle import *
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        forward(100)
        right(angle)

for shape_side in range(3,10):
    color(random.choice(colours))
    draw_shape(shape_side)
exitonclick()