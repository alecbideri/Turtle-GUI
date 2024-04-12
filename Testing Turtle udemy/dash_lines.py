from turtle import *

speed(1)
dash_length = 10
gap_length = 5

for _ in range(10):
    forward(dash_length)
    penup()
    forward(gap_length)
    pendown()

exitonclick()