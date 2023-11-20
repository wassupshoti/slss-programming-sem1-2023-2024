# Score for SFU
# Author: Sommerson ma
# Date: Nov 10 2023

# Load data from a file
# "Read" it in a meaningful way
# Link our Sim Score algo to the data

# Open the file
with open("./data.csv") as f:
    print(f.readline())

# Create a "profile" of likes (fave places in Simon Fraser University)
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fatih's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]


most_similar_score = 0
most_similar_name = ""

with open("./data.csv") as f:
    # Throw away header
    header = f.readline()

    for line in f:
        # Conver the string to a list
        current_likes = line.split(",")

        # Store the person's name
        current_name = current_likes[1]

        # Initialize the current sim score
        current_sim_score = 0

        for item in profile:
            if item in current_likes:
                current_sim_score += 1


        # Print the results from this line of data
        print(f"{current_name} - Score: {current_sim_score}")

        if current_sim_score > most_similar_score:
            most_similar_score = current_sim_score
            most_simlar_name = current_name
        
print("Most similar person is...")
print(f"{most_similar_name} - Score: {most_similar_score}")


