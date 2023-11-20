# World Traveller
# Author: Sommerson Ma
# Date: Nov 7 2023

import time
import random

print("wassup, imma see how many places you have visted")

time.sleep(1)

user_name = input("Before we start, what's your name friend?")

if user_name == "Sommerson" or user_name == "sommerson" or user_name == "Sam" or user_name == "sam" or user_name == "awesam" or user_name == "Awesam":
    time.sleep(.5)
    print("WHHHAAATTT! We got the same name thats so awesome pawsome!")
else:    
    time.sleep(.76)
    print(f"Sick name, {user_name}")
    time.sleep(1)


continents_visted = 0

print(f"To start {user_name}, we will see how many continenets you have been")

time.sleep(.6843543542)

print("Before we start please answer only in yes or no answers please")

asia = input("Have you been to Asia?").lower().strip(",.?! ")

time.sleep(.75)

europe = input("Have you been to Europe?").lower().strip(",.?! ")

time.sleep(.75)

north_america = input("Have you been to North America?").lower().strip(",.?! ")

time.sleep(.75)

south_america = input("Have you been to South America?").lower().strip(",.?! ")

time.sleep(.75)

australia = input("Have you been to Australia?").lower().strip(",.?! ")

time.sleep(.75)

africa = input("Have you been to Africa?").lower().strip(",.?! ")

time.sleep(.75)

antartctica = input("Have you been to Antarctica?").lower().strip(",.?! ")

time.sleep(.75)

if asia in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if north_america in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if south_america in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if europe in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if australia in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if africa in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if antartctica in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    continents_visted += 1

print(f"I see {user_name}, you have been to {continents_visted}/7, very cool!")






