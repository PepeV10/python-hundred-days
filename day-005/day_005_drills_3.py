# Ticket ID: [TICKET-R-02]
# Assigned To: Pepe Venegas
# Title: Feature: New User Onboarding - Username Generator
# Timebox Estimate: 30-45 Minutes
# 1. Business Context:
# To make the sign-up process easier for our new web application, we need a script that suggests a few unique usernames for a new user based on their name and a favorite keyword.
# 2. Technical Requirements:
# Prompt the user for two inputs:
# Their first name.
# Their favorite keyword.
# Generate 3 username suggestions and store them in a list.
# The logic for each suggestion is: (first three letters of name) + (the full keyword) + (a random 2-digit number).
# All usernames must be in lowercase.
# 3. Starter Code & Acceptance Criteria:

import random

print("Welcome to the Username Generator!")
first_name = input("What is your first name?\n").lower()
keyword = input("What is your favorite keyword?\n").lower()

suggested_usernames = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # Use this list

# --- YOUR IMPLEMENTATION GOES HERE ---

for usr_name in range(3):
  name_part = first_name[0:3]

  digit1 = random.choice(numbers)
  digit2 = random.choice(numbers)

  number_part = digit1 + digit2

  new_username = f"{name_part}{keyword}{number_part}"

  suggested_usernames.append(new_username)

print("Here are some username suggestions:")
print(suggested_usernames)

