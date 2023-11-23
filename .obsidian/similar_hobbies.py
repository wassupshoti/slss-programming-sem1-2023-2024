# Similarity score thingy majob
# Author: Sommerson smammsamsmammsmamam mamamamma amamaammamaaaaaa
# Date: Nov 20 2023

import random
import time

person1_fav_hobbies = input("Hello there, what are your top 4 hobbies? please seperate them with spaces!").lower().split(" ")

time.sleep(1)

person2_fav_hobbies = input("Hello there, what are your top 4 hobbies? please seperate them with spaces! ").lower().split(" ")

time.sleep(1)

print(f"Person 1: {person1_fav_hobbies}")

time.sleep(.5)

print(f"Person 2: {person2_fav_hobbies}")

time.sleep(.5)

similarity_score = 0
for hobby in person1_fav_hobbies:
    if hobby in person2_fav_hobbies:
        similarity_score += 1
print(f"You have {similarity_score} hobbies in common!")














