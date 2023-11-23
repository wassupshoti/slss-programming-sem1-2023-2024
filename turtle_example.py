# Turtle Example
# Author: Sommerson Ma
# Date: Nov 21 2023

import turtle

# ----- CONSTANTS
TURTLE_MAGNITUDE = 40

# Create a turtle
michealangelo = turtle.Turtle()

# Get some instructions from the user
print(""" To give commands, type:
F - to go foward
L - to go left
R - to go right
B - to go backwards """)
command = input("Where should I go? ")

# Repeat the below code IINDFEINITELY
done = False


while not done:
    command = input("Where should I go?").strip(".,?! ").lower()

    # Based on those insturctions, move the turtle
    # on the screen
    if command.strip(",.?! ").lower() == "f":
        michealangelo.forward(TURTLE_MAGNITUDE)
    elif command in ["l", "left"]:
     michealangelo.left(90)
    elif command in ["r", "right"]:
        michealangelo.right(90)
    elif command in ["b", "back"]:
       michealangelo.backward(TURTLE_MAGNITUDE)
    elif command == "stop":
        done = True
        
turtle.done()