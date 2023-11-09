# Pumpkin Drawing
# Author:
# Date: 31 October 2023

import turtle
import time

window = turtle.Screen()
window.bgcolor("black")

# Whole pumpkin
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

# "Flatten" the lower part of the pumpkin
carver.penup()
carver.setposition(-200, -100)
carver.pensize(60)
carver.pendown()
carver.forward(600)
carver.pensize(2)

# Nose
carver.penup()
carver.setposition(0, 0)
carver.dot(10)
carver.forward(15)

# Eye
carver.setpos(-40, 30)
carver.dot(25)

# Mouth
carver.setpos(0, -50)
carver.setheading(180)
carver.pendown()
carver.forward(35)
carver.setheading(0)
carver.forward(70)

turtle.done()