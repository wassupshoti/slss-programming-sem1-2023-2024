# Semester Molester
# Author: Sommerons fd jsklfmslkdmf
# Date: Nov 7 2023

import random
import time

print("yello") 
time.sleep(1)

print("Im going to see how good, or bad your courses are this semester!")

time.sleep(1)

print("Assuming you go to Steveston-London Secondary School and have 4 classes...")

time.sleep(.7)

print("on a of scale 1 - 5...")

time.sleep(.5)

courses = [
    "What would you rate your first course?",
    "What would you rate your second course?",
    "What would you rate your third course?",
    "What would you rate your fourth and final class?"
]

course_rating = 0

for course in courses:
    print(course)
    time.sleep(1)

    courses_rating_final = int(input().strip(":,.?! "))

    course_rating += courses_rating_final

average_rating = course_rating /len(courses)

time.sleep(1)
print("ITS TIME")
time.sleep(1)
print(f"The average rating for your courses is: {average_rating:.2f} /4")

if average_rating > 3:
    print("Glad to hear that!")
if average_rating == 3:
    print("Glad to hear that!")
if 3 > average_rating > 1:
    print("Not a bad semester!")
if average_rating < 1:
    print("Ouch!")
if average_rating == 1:
    print("Ouch!")







