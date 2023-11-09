# Mcdonaldo
# Authot: Sommerson meh
# Date: Nov 2 2023

import time
import random

print("Welcome to mcdolands...")

time.sleep(1)

burger_price = input("would you like a delicous burger for 5 bucks?").lower().strip(",.?! ")

fries_price = input("What about a tasty, oily fries, for only 3 bucks!").lower().strip(",.?! ")

total_price = 0

# If they want a burger
if burger_price in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    # add a burger to their total_price
    total_price += 5

if fries_price in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please"]:
    time.sleep(1)
    # add fries to their total_price
    total_price += 3


# Calculate the total price with taxes
print(f"Your total price is ${total_price * 1.14}!")
time.sleep(.5)
print("How would you like to pay?")









