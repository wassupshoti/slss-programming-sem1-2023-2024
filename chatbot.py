# Chatbot
# Author: Sommerson
# Date: 21 September 2023

import random
import time


# Greet the user
print("wassup 🧌")
time.sleep(2)
print("Im a crude chatbot, here to talk to you.")
time.sleep(1.5)



# Get the user's name and store in a variable
user_name = input("So... what's your name?")

time.sleep(2)

# Respond with the user's name
print(f"It's nice to meet you, {user_name}!")

time.sleep(1)

# Ask the user what their favourite food is
fave_food = input("What's your favourie food? ")

# Respond with sometihng that is NOT TOO repetitive
# Create a list of appropriate responses
list_of_fave_food_responses = [
    "sounds delicious.",
    f"Yes, {fave_food} is one of my favourties too!",
    "N i c e.",
    "Straight gas",
    "Heard it taste like dog poop, can't say if I never tried it",
    "not bad",
    "bro that sucks, no I haven't tried it",
    "Really? I know how to cook it, if you want some, hmu!"
    ] 

print(list_of_fave_food_responses[5])

# Choose one response randomly from the list
random_response = random.choice(list_of_fave_food_responses)

# Print out the chosen response
print(random_response)