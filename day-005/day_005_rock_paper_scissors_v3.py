# Ticket ID: [TICKET-05-03]
# Assigned To: Pepe Venegas
# Sprint: Day 5 - Knowledge Consolidation
# Title: Refactor & Enhance: "Rock, Paper, Scissors" Game Logic

# 1. Business Context & User Story:
# Our "Rock, Paper, Scissors" game from Day 4 was a success. However, user feedback indicates the game feels a bit repetitive. The product team wants to enhance the game by introducing a "Best of 3" series to increase user engagement. Additionally, code review has flagged an opportunity to make the logic cleaner by incorporating our new for loop skills.
# User Story: "As a player, I want to play a 'Best of 3' match of Rock, Paper, Scissors, so that a single lucky round doesn't determine the winner and the game feels more substantial."

# 2. Technical Requirements & Enhancements:
# This ticket has three distinct parts. I want you to tackle them one by one.
# Part 1: Track Scores (Integrate Day 5 Concepts)
# Goal: Add a scoring system.
# Implementation:
# Before the game starts, create two variables: player_score = 0 and computer_score = 0.
# Inside your existing if/elif/else logic that determines the winner of a round, add code to increment the correct player's score by 1. For example, if the player wins, you'll add player_score += 1. Don't worry about ties.
# Part 2: Implement "Best of 3" Logic (Integrate Day 5 Concepts)
# Goal: Make the game run for exactly 3 rounds.
# Implementation:
# You will wrap your entire game logic for a single round inside a for loop.
# New Concept Introduction: To make a loop run a specific number of times, we use the range() function. The syntax for round_number in range(3): will run the indented code exactly 3 times. We will cover range() in detail tomorrow, but for this exercise, you just need to know that this line creates the "Best of 3" structure.
# Part 3: Announce the Final Winner (Integrate Day 3 Concepts)
# Goal: After the 3 rounds are over, declare an overall winner.
# Implementation:
# Outside and after your for loop, you will write a final if/elif/else block.
# This block will compare the final player_score and computer_score.
# Print a message declaring the overall winner (e.g., "You won the series!", "The computer won the series!", or "It's a tie!").

# 3. Starter Code (Your Day 4 Project):
# Find your "Rock, Paper, Scissors" project code from yesterday. You will be adding to and modifying that code. It should look something like this:

# Your Day 4 Rock, Paper, Scissors code
import random

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

game_images = [rock, paper, scissors]

user_score = 0
cpu_score = 0

print("Welcome to Pepe's Rock Paper Scissors Game v3.0")
# ... your logic for getting user choice ...

for round_number in range(3):

  user_choice = int(input("What do you choose? Please type 0 for Rock, 1 for Paper, or 2 for Scissors!\n: "))

  if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
  else:
    # Use the list index to print the user's choice. This is efficient.
    print("\nYou chose:")
    print(game_images[user_choice])
  # ... your logic for generating computer choice ...
  # Get computer's choice.
    computer_choice = random.randint(0, 2)
      
    # Use the list index to print the computer's choice.
    print("Computer chose:")
    print(game_images[computer_choice])


  # ... your big if/elif/else block for determining the winner of one round ...

  # --- 5. STATE EVALUATION (GAME LOGIC) ---
  # This nested structure is clean and covers all cases logically.
    if user_choice == computer_choice:
      print("It's a draw.")
    # Check all user winning conditions together.
    elif (user_choice == 0 and computer_choice == 2) or \
          (user_choice == 2 and computer_choice == 1) or \
          (user_choice == 1 and computer_choice == 0):
          print("You win!")
          user_score += 1
    # If it's not a draw and the user didn't win, they must have lost.
    else:
      print("You lose.")
      cpu_score += 1

print(f"\n --- Final Score ---")
print(f"Your Score is: {user_score} | The CPU's Score is: {cpu_score}")

if user_score > cpu_score:
   print("Congratulations, you have bested the CPU and WON!")
elif cpu_score > user_score:
   print("I am sorry but you have lost! CPU Wins")
else:
   print("This game has ended in a Tie!")
