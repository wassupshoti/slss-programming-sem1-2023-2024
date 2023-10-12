# Loop Practice
# Author: Sommerson MAAA
# Date: 10 October 2023

import time
# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do sometihng for each thing in the list
# Print it out in a pretty way
#   e.g 
#     
#
#

for item in groceries:
    print(f"* {item}")
    print("  ---")

# Create a pyramid like this using a for loop.

# *
# **
# *** 
# **** 
# *****
# ******

stars = ["*", "**", "***", "****", "*****", "******", "*******"]
for row in stars:
    print(row)
    
# Problem:
# Create a new years eve countdown
# Requirements: 
# * Starts off at 10
# * Countdown every second and print the second that it's at
# * Instead of reaching zero it says "Happy New Year"
# Example Output:
#   10
#   9
#   8
#   7
#   6
#   5
#   4
#   3
#   2
#   1
#   Happy New Year!

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!"]
for timer in countdown:
    print(timer)
    time.sleep(1)