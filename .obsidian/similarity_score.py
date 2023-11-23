# Similarity score
# Author: Sommerson ma
# Date: November 9 2023

import random
import time

# Calculate simllarity scores between two people

# Create two lists that represent the moveis
# that they like
ubials_fave_moives = [
    "the matrix",
    "avengers: infinity war",
    "infernal affairs",
    "rogue one",
    "the empire strikes back"
]

bens_fave_moives = [
    "thomas friends, big world big advanture",
    "paddington 2",
    "avengers: infinity war",
    "minions",
    "rouge one"
]

similarity_score = 0

# For every movie in the first list
    # if that movie is in the second list
        # Increase the similarity score by 1
for movie in ubials_fave_moives:
    if movie in bens_fave_moives:
        similarity_score += 1

# Display the results
print(f"The similarity score between the users is:")
print(similarity_score)


