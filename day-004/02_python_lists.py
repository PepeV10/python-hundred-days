# Ticket ID: LCI-D04-E2
# Title: Feature: Banker Roulette - Random Bill Payer Selector
# Assigned to: Pepe Venegas
# Sprint: Day 04 - Randomization & Data Structures

# User Story: A user dining with friends, I want to enter a list of names and have the program randomly select one person to pay the entire bill, so that we can have a fun (and slightly stressful) way to decide who pays.

# Systems & Architecture Overview:
# This program combines our two new concepts: Data Structures (to hold the list of names) and randomization (to select one name fram that list). This pattern-storing a collection of items and then randomly selecting one-is extremely common. Think of a game choosing a random powr-up from a list of available powr-ups, a music app shuffling a playlist, or a contest app drawing a winner from a list of entrants.

# Acceptance Criteria(AC):
# AC-1: User Input: The program must accept a single string of names from the user, with each name separated by a comma and a space (e.g., "Angela, Ben, Jenny, Michael, Chloe").
# AC-2: String to list conversion: The program must use .split() string method to convert the input string into a Python list of individual names. 
# AC-3: Random Selection: Random Selection: The program must use the random module to select one name from the list.
# AC-4: Output: The program must print a message indicating who was chosen to pay the bill (e.g., "Michael is going to buy the meal today!").

import random

print("Welcome to the 'Banker Roulette'")
friends_input = input("Please enter the friends that will participate separated by a comma\n: ")
spaceless_input = friends_input.replace(' ', '')
friends_list = spaceless_input.split(',')
friend_who_pays = random.choice(friends_list)

print(f"{friend_who_pays} is going to buy the meal today. Thank you {friend_who_pays}!")





# Angela's Solution
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(random.choice(friends))

# 2nd Option
random_index = random.randint(0, 4)
print(friends[random_index])





# Ticket ID: LCI-D04-E3
# Title: Feature: Random Team Picker v1.0
# Problem Statement: Write a program that takes a comma-separated list of player names. The program that takes a comma-separated list of player names. The program should then tell the user which player has been randomly selected to be the "captain".
# Acceptance Criteria(AC):
# 1. Accept a single string of player names from the user (e.g., "LeBron, Curry, Durant").
# 2. Clean the input string to handle potential extra spaces.
# 3. Convert the string into a list of player name.
# 4. Use random.choice() to select one player.
# 5. Print the result in the format: "The captain for today's game will be [Player Name]".

input_player = input("Please enter the list of players to choose from\n: ")
spaceless_input_player = input_player.replace(' ', '')
player_list = spaceless_input_player.split(',')
captain_player = random.choice(player_list)
print(f"The captain for today's game will be:{captain_player}")





# Ticket ID: LCI-D04-E4
# Title: Feature: Fruit Salad Surprise v1.0
# Problem Statement: You have a predefined list of fruits. Create a program that simulates making a fruit salad by randomly picking and printing three different fruits from your list.
# Acceptance Criteria:
# Create a list variable inside your code that holds at least 5 fruit names (e.g., fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry"]). You do not need user input for this ticket.
# Use random.choice() three separate times.
# Store each choice in a separate variable (e.g., fruit1, fruit2, fruit3).
# Print a message like: "For our fruit salad, we will use: [Fruit 1], [Fruit 2], and [Fruit 3]."
# Tier: Attempt Tier 2 (Assisted). Write the pseudocode plan first.

print("Welcome to the Random Fruit Salad Picker")
fruits = ["Apple", "Strawberry", "Banana", "Cherry", "Kiwi", "Blackbery", "Grapes"]
fruit_salad = random.sample(fruits, 3)
print(f"for our fruit salad, we'll use: {fruit_salad[0]}, {fruit_salad[1]}, and {fruit_salad[2]}")


# Fruit Salad v2.0
print("welcome to the Random Fruit Salad Picker 2.0")
fruit = input("Please enter more than 3 fruits (each separated by a comma) that you'd like to toss into the Fruit Picker\n: ")
spaceless_fruit_string = fruit.replace(' ', '')
clean_fruit_list = spaceless_fruit_string.split(',')
random_fruits = random.sample(clean_fruit_list, 3)
print(f"For tonights Fruit Salad we'll add: {random_fruits}. Enjoy!\n =D")
