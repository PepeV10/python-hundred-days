# Ticket ID: [TICKET-MD-01] (MD for Micro-Drill)
# Assigned To: Pepe Venegas
# Title: Data Extraction: Isolate User ID from Log Entry
# Timebox Estimate: 5 Minutes
# 1. Business Context:
# Our system logs generate entries that combine a timestamp with a user ID, like "LOG:1692987483-USERID_pep". We need a quick way to slice out just the user ID part for our reporting tools.
# 2. Technical Requirements:
# You are given a log entry string.
# The user ID always starts at the 20th character.
# The user ID is always 3 characters long.
# You must use string slicing to extract the user ID.
# The extracted ID must be converted to all uppercase letters.
# 3. Starter Code & Acceptance Criteria:

log_entry = "LOG:1692987483-USERID_pep"

# --- YOUR IMPLEMENTATION GOES HERE ---
# 1. Slice the log_entry string to get just "pep"
# 2. Convert the sliced part to uppercase.
# 3. Store it in a variable called user_id.

user_id = log_entry[22:25].upper()    

# This print statement should output: "PEP"
print(user_id)

import random

secret_number = random.randint(1, 100)
ATTEMPTS = 7

print("Welcome to the High-Low Guessing Game!")
print(f"I'm thinking of a number between 1 and 100. You have {ATTEMPTS} attempts.")

for attempt_number in range(ATTEMPTS, 0, -1):
  print(f"\n--- You have {attempt_number} attempts remaining. ---")

  usr_guess = int(input("Make a guess: "))

  if usr_guess > secret_number:
    print("Too high.")
  elif usr_guess < secret_number:
    print("Too low.")
  else:
    print(f"You got it! The answer was {secret_number}. Congratulations")

    break

else:
  print("\n--- Game Over ---")
  print(f"You've run out of attempts. The secret number was {secret_number}.")
  print("You lose.")


