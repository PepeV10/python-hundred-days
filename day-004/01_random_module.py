# Ticket ID: LCI-D04-E1
# Title: Feature Implement Coin Toss Simulator v1.0
# Assigned To: Pepe Venegas
# Sprint: Day 04 - Randomization & Data Structures

# User Story:
# As a user, I want to run a program that simulates a fair coin toss, so that I can get a random binary outcome("Heads" or "Tails") for decision-making purposes.

# Systems & Architecture OVerview:
# This exercise is a foundational implementation of a random binary event generator. While simple, this concept is a building block for more comlex systems. It's used in game development(e.g., determning a critical hit chance), statistical sampling(A/B testing), and even basic cryptographic protocols. This ticket serves as the "Hello, World!" for using imported modules and applying randomization to control program flow.

# Acceptance Criteria(AC):
# AC-1: Module Import: The program must correctly import the random module at the beginning of the script.
# AC-2: Random Number Generation: THe program must use random.randint() to generate a random integer. The choice of the two integers(e.g., 0 and 1, or 1 and 2) is up to the developer, but it must represent the two possible outcomes of a coin toss.
# AC-3: Conditional Logic: AN if/else statement must be used to check the value of the generated random integer.
# AC-4: "Heads" Output: If the random integer matches the condition for "Heads", the program must print the exact string Heads to the console.
# AC-5: "Tails" Output: If the random integer matches the condition for "Tails", the program must print the exact string Tails to the console.

# Tiered Development Program:
# As this is the first application of a newly learned module, I recommend proceeding with Tier 2(Assited)

# Action Required:
# Please provide your implementation plan (pseudocode) for review. This plan should outline the logical steps you will take to meet all Acceptance Criteria before you write a single line of Python code.

import random

print("Welcome to Pepe's Coin Flip Simulator v1.0")
# coin_choice = input("What is your choice? 'heads', or 'tails'?\n:").lower()
random_integer = random.randint(0,1)

if random_integer == 0:
  print("Heads")
else:
  print("Tails")
# if coin_choice == 'heads' and random_integer == 0:
#   print("Heads")
# elif coin_choice == 'tails' and random_integer == 1:
#   print("Tails")

