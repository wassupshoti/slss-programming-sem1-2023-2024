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

# If they answer pasta, respond with something related
if fave_food == "ramen":
    print("bro think he naruto uzumaki")
    print("As a robot, I think it taste pretty good, miso the best though")
elif fave_food == "burgers" or fave_food == "Burgers":
    print("mmm chese burgers")
    print("Do you get the joke? Like from, nevermind")
elif fave_food == "rayburn" or fave_food == "Rayburn" or fave_food == "rayzaddy" or fave_food == "Rayzaddy":
    print("yo what the monke") 


else:
    # Respond with sometihng that is NOT TOO repetitive
    # Create a list of appropriate responses
    list_of_fave_food_responses = [
        "sounds delicious.",
        f"Yes, {fave_food} is one of my favourties too!",
        "N i c e.",
        "Straight gas",
        "Heard it taste like dog poop, can't say if I never tried it",
        "not bad",
        "bro that sucks, no I haven't tried it"
        ] 

print(list_of_fave_food_responses)

# Choose one response randomly from the list
random_response = random.choice(list_of_fave_food_responses)

# Print out the chosen response
