# Star Wars Bot
# Author: Sommerson MAAAA
# October 16 2023

import time
import random

# Bot. Shall. Commence. With. Thy. Examination.

print("Greetings Traveller,")

time.sleep(.75)

print("Before you begin your epic conquest, we must determine your fate")

time.sleep(1)

# Ask the questions now

fighting = input("Do you like fighting people?")
if fighting.lower() in ["yes", "yea", "fo sho", "duh", "uh huh", "si", "oui"]:
    time.sleep(.75)
    print("I see, I see, very informative")

# First question doesn't even matter

elif fighting.lower() in ["nah", "no", "nada", "negative", "never", "n o n"]:
    time.sleep(.75)
    print("I see, very, Informative")

# Its really not informative

else:
    print("what is bro saying")

time.sleep(1)
connection_red = input("Tell me, do you feel a connection to the color red?")

if connection_red.lower() in ["yes", "yea", "yuppers", "yup", "fo sho", "ye", "ofc", "uh huh"]:
    time.sleep(.50)
    print("Ight your ass is in the Dark Side")

elif connection_red.lower() in ["no", "nada", "never", "negative", "nope", "nah"]:
    time.sleep(.50)
    print("Ight your on the light side")

else:
    time.sleep(2)
    print("Blud you gotta answer the question to see if your on the light side or the dark side")




