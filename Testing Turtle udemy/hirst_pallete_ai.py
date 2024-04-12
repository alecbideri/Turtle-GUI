import random
import turtle as turtle_module

# List of colors
colours = [(235, 234, 231), (235, 229, 232), (230, 237, 232), (223, 232, 237), (235, 36, 108), (143, 28, 66), (238, 75, 36), (9, 146, 93), (223, 168, 48), (48, 190, 230), (184, 158, 48), (30, 126, 192), (126, 192, 81), (253, 223, 0), (83, 28, 90), (175, 44, 93), (243, 219, 54), (40, 171, 114), (208, 132, 166), (196, 61, 43), (148, 29, 27), (239, 163, 194), (244, 167, 156), (161, 211, 177), (28, 188, 224), (136, 213, 233), (12, 111, 55), (76, 136, 183), (155, 196, 229)]

# Set up Turtle
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Calculate palette dimensions
num_columns = 10
num_rows = (len(colours) + num_columns - 1) // num_columns  # Calculate number of rows
dot_size = 20
dot_spacing = 50

# Calculate palette width and height
palette_width = num_columns * dot_spacing
palette_height = num_rows * dot_spacing

# Calculate starting position to center the palette on the screen
start_x = -palette_width / 2
start_y = palette_height / 2

# Set initial position for drawing
tim.setpos(start_x, start_y)

# Draw colored dots
number_of_dots = 100  # Number of dots to draw
for dot_count in range(1, number_of_dots + 1):
    if dot_count <= 100:  # Ensure not to exceed the number of colors available
        tim.dot(dot_size, random.choice(colours))
    tim.forward(dot_spacing)

    if dot_count % num_columns == 0:  # Move to the next row
        tim.setx(start_x)
        tim.sety(tim.ycor() - dot_spacing)

# Create screen and exit on click
screen = turtle_module.Screen()
screen.exitonclick()
