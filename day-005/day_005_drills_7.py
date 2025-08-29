# Ticket ID: [TICKET-P-03]
# Assigned To: Pepe Venegas
# Title: Gaming Division: Universal Dice Roller Module
# Complexity: Black Diamond (Creative Application)
# 1. Business Context:
# The gaming division is building several new tabletop-style games and needs a flexible dice-rolling function. They need a script that can simulate rolling any number of dice with any number of sides.
# 2. Technical Requirements:
# Prompt the user for two inputs:
# How many dice they want to roll? (num_dice)
# How many sides does each die have? (num_sides)
# Simulate the rolling of the dice. Use a for loop that runs num_dice times.
# Inside the loop, generate a random number between 1 and num_sides (inclusive) for each die roll.
# Store the result of each individual roll in a list called roll_results.
# After the loop, calculate and print the total sum of all the rolls.
# Print the list of individual rolls as well for transparency.
# 3. Acceptance Criteria:
# WHEN the user asks to roll 3 dice with 6 sides each,
# THEN the output should look similar to this (the numbers will be random):

# --- Rolling 3d6 ---
# The results of your rolls are: [5, 2, 6]
# The total sum of your rolls is: 13

# Skills Reinforced: input() with int(), for loop with range(), random.randint(), list append(), using a variable (num_sides) to set the bounds of a random range, using the sum() function on a list.

import random

num_dice = int(input("How many dice do you want to roll?\n: "))
num_sides = int(input("How many sides does each die have?\n: "))

roll_results = []

for dice in range(num_dice):
  roll_results.append(random.randint(1, num_sides))

total_sum = sum(roll_results)

print(f"\n--- Rolling 3d6 ---")
print(f"The results of your rolls are:{roll_results}")
print(f"The total sum of your rolls is: {total_sum}")

