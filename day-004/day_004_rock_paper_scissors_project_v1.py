# LearnCode Inc. Project Brief
# Project ID: LCI-PROJ-D04
# Project Name: Command-Line RPS v1.0 (Rock, Paper, Scissors)
# Assigned To: Pepe Venegas
# Sprint: Day 04 - Randomization & Data Structures
# Project Goal:
# Develop a command-line interface (CLI) game where a human user can play a single round of Rock, Paper, Scissors against a computer opponent with a randomized choice.
# Systems & Architecture Overview:
# This project simulates a simple turn-based game loop, a foundational pattern in all game development. The core architecture involves three stages: (1) State Gathering (getting user and computer inputs), (2) State Evaluation (applying game rules to determine the outcome), and (3) State Display (presenting the results to the user). This project is an excellent exercise in mapping real-world rules and entities (like game choices and outcomes) to programming constructs like lists and conditional logic.
# ASCII Art (Provided Assets)
# You will need these for the project. Create a list variable to hold them.

# Acceptance Criteria (AC):
# AC-1: Game Assets: The program must store the rock, paper, and scissors ASCII art strings in a single list data structure.
# AC-2: User Input: The program must prompt the user with: What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. and store their input.
# AC-3: Input Validation: The program must check if the user's input is a valid choice (0, 1, or 2).
# If the input is invalid (e.g., 3, -1, or not a number), it must print an error message like You typed an invalid number, you lose! and terminate gracefully without crashing.
# AC-4: User Choice Display: If the user's input is valid, the program must print the corresponding ASCII art for their choice from the list defined in AC-1.
# AC-5: Computer Choice Generation: The program must generate a random integer between 0 and 2 (inclusive) to represent the computer's choice.
# AC-6: Computer Choice Display: The program must print a header like Computer chose: followed by the corresponding ASCII art for the computer's choice.
# AC-7: Game Logic - Draw: The program must correctly identify and announce a draw if the user's choice and the computer's choice are the same. (e.g., It's a draw).
# AC-8: Game Logic - Win/Loss: The program must implement all winning and losing conditions correctly and print the appropriate outcome (You win! or You lose!).
# Rock (0) beats Scissors (2)
# Scissors (2) beats Paper (1)
# Paper (1) beats Rock (0)

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# import random

# print("Welcome to Pepe's Rock, Paper, Scissors Game!")
# rock_paper_scissors = [rock, paper, scissors]

# usr_1_choice = int(input("What do you choose? Please type 0 for Rock, 1 for Paper, or 2 for Scissors!\n: "))
# if usr_1_choice == 0:
#   print("You chose Rock!")
#   print(rock)
# elif usr_1_choice == 1:
#   print("You chose Paper!")
#   print(paper)
# elif usr_1_choice == 2:
#   print("You chose Scissors!")
# else:
#   print("That is not a valid input. Please try again, with: 0, 1 or 2")

# cpu_choice = random.randint(0,2)
# if cpu_choice == 0:
#   print("CPU chose Rock!")
#   print(rock)
# elif cpu_choice == 1:
#   print("CPU chose Paper!")
#   print(paper)
# elif cpu_choice == 2:
#   print("CPU chose Scissors!")
#   print(scissors)

# if usr_1_choice == 0 and cpu_choice == 0:
#   print("It's a draw, you both chose Rock!")
# elif usr_1_choice == 1 and cpu_choice == 1:
#   print("It's a draw, you  both chose Paper!")
# elif usr_1_choice == 2 and cpu_choice == 2:
#   print("It's a draw, you both chose Scissors!")

# if usr_1_choice == 0 and cpu_choice == 1:
#   print("Paper beats Rock, CPU Wins!")
# elif usr_1_choice == 0 and cpu_choice == 2:
#   print("Rock beats Scissors, Player 1 Wins!")
# elif usr_1_choice == 1 and cpu_choice == 2:
#   print("Scissors beats Paper, CPU Wins!")
# elif usr_1_choice == 1 and cpu_choice == 0:
#   print("Paper beats Rock, Player 1 Wins!")
# elif usr_1_choice == 2 and cpu_choice == 0:
#   print("Rock beats Scissors, CPU Wins!")
# elif usr_1_choice == 2 and cpu_choice == 1:
#   print("Scissors beats Paper, Player 1 Wins!")

# Refactored Version v2.0

import random

# --- 1. ASSETS ---
# Storing assets at the top is a clean convention.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# --- 2. GAME SETUP ---
# Put game assets into a list. This is great data modeling.
# The index (0, 1, 2) directly maps to the game choices.
game_images = [rock, paper, scissors]

print("Welcome to Pepe's Rock, Paper, Scissors Game!")

# --- 3. STATE GATHERING ---
# Get user input and convert to integer immediately.
user_choice = int(input("What do you choose? Please type 0 for Rock, 1 for Paper, or 2 for Scissors!\n: "))

# --- 4. STATE DISPLAY & VALIDATION ---
# A single 'if' statement to handle both valid and invalid input.
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    # Use the list index to print the user's choice. This is efficient.
    print("\nYou chose:")
    print(game_images[user_choice])

    # Get computer's choice.
    computer_choice = random.randint(0, 2)
    
    # Use the list index to print the computer's choice.
    print("Computer chose:")
    print(game_images[computer_choice])

    # --- 5. STATE EVALUATION (GAME LOGIC) ---
    # This nested structure is clean and covers all cases logically.
    if user_choice == computer_choice:
        print("It's a draw.")
    # Check all user winning conditions together.
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 1 and computer_choice == 0):
        print("You win!")
    # If it's not a draw and the user didn't win, they must have lost.
    else:
        print("You lose.")
