# Parent Bot
# Atuhor: Sommerson Ma
# Date: Nov 23 2023

import time
import random

print("ring ring")

time.sleep(.85)

print("ring ring ring")

time.sleep(.85)

print("* picks up land line *")

time.sleep(.85)

print("Hello Child, hope you are fine at home right now...")

time.sleep(.50)

eat = input("Did you eat yet?").lower().strip(",.?! ")

time.sleep(1)

study = input("Did you study yet?").lower().strip(",.?! ")

time.sleep(1)

laundry = input("Did you do the laundry yet?").lower().strip(",.?! ")

time.sleep(1)

lola_check = input("Did you call your lola yet").lower

chores_check_list = 0

if eat in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please", "yup"]:
    time.sleep(1)
    chores_check_list += 1

if study in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please", "yup"]:
    time.sleep(1)
    chores_check_list += 1

if laundry in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please", "yup"]:
    time.sleep(1)
    chores_check_list += 1

if lola_check in ["yes", "sure", "shore","yuppers", "yea", "yeah", "uh huh", "duh", "yes please", "yup"]:
    time.sleep(1)
    chores_check_list += 1

if chores_check_list > 3:
    print("Glad to hear that!")
if chores_check_list == 3:
    print("Glad to hear that!")
if 3 > chores_check_list > 1:
    print("ok")
if chores_check_list < 1:
    print("Coming home right now")
if chores_check_list == 1:
    print("erm, ok")

