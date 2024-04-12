import  colorgram
import random
import turtle as turtle_module
# rgb_colors = []
# colors = colorgram.extract("image.jpg" , 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# extracted all colors from the jpg image using colorgram


colours = [(235, 234, 231), (235, 229, 232), (230, 237, 232), (223, 232, 237), (235, 36, 108), (143, 28, 66), (238, 75, 36), (9, 146, 93), (223, 168, 48), (48, 190, 230), (184, 158, 48), (30, 126, 192), (126, 192, 81), (253, 223, 0), (83, 28, 90), (175, 44, 93), (243, 219, 54), (40, 171, 114), (208, 132, 166), (196, 61, 43), (148, 29, 27), (239, 163, 194), (244, 167, 156), (161, 211, 177), (28, 188, 224), (136, 213, 233), (12, 111, 55), (76, 136, 183), (155, 196, 229)]
turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20 , random.choice(colours))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()