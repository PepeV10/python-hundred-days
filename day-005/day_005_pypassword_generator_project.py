# Ticket ID: [TICKET-05-04]
# Assigned To: Pepe Venegas
# Sprint: Day 5 - Project Implementation
# Title: Feature: PyPassword Generator

# 1. Business Context & User Story:
# In an era of increasing digital threats, users need a tool to generate strong, unpredictable passwords that are difficult for attackers to guess or brute-force. This tool will provide that service directly from the command line.
# User Story: "As a security-conscious user, I want to specify the desired number of letters, symbols, and numbers, so that I can generate a strong, randomized password to protect my online accounts."

# 2. Technical Requirements & Constraints:
# Input: The program must prompt the user for three integers:
# The number of letters.
# The number of symbols.
# The number of numbers.
# Provided Assets: Use the following lists as the source for characters:

# letters = ['a', 'b', 'c', ... 'Z'] # (The full list)
# numbers = ['0', '1', '2', ... '9']
# symbols = ['!', '#', '$', ... '+']

# Output: A single string representing the generated password.

# Implementation Tiers:
# Easy Level: The generated password string should have all letters first, followed by all symbols, followed by all numbers.

# Hard Level: The characters in the generated password string should be in a completely random order.

# 3. Acceptance Criteria (Definition of "Done"):
# WHEN a user requests 4 letters, 2 symbols, and 2 numbers,
# THEN the Easy Level output will be a string with 8 characters, structured like llllssnn (e.g., "gHkP&!52").
# AND the Hard Level output will be a string with 8 characters, with the character types mixed (e.g., "g!5P&k2H").

# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# symbols = ['!', '#', '$', '%','(', ')', '*', '+', '^', '_', '-', '=', '{', '}', '[', ']', ':', ';','.', '?', '/']

# print("Welcome to Pepe's Super Password Generator")

# char_length = int(input("How many characters long do you want your password to be?\n: "))
# possible_char = [letters, numbers, symbols]
# final_password = ""
# for char in range(char_length):
#   random_category = random.choice(possible_char)
#   random_character = random.choice(random_category)
#   final_password += random_character
# print(f"Congratulations, your final password is: {final_password}")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '*', '+', '-', '.', '_', '?', '@', '^']

print("Welcome to Pepe's Super Password Generator V2.0")

n_letters = int(input("How many letters do you want your Password to contain?\n: "))
n_numbers = int(input("How many numbers do you want your Password to contain?\n: "))
n_symbols = int(input("How many symbols do you want your Password to contain?\n: "))

password_list = []

for letter in range(0, n_letters):
  password_list.append(random.choice(letters))
for number in range(0, n_numbers):
  password_list.append(random.choice(numbers))
for symbol in range(0, n_symbols):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

final_password = ""
for char in password_list:
  final_password += char


print(f"Here's your brand new Super Password: {final_password}")

# # Angela Yu's Easy Solution

# print("Welcome to the PyPassword Generator!")

# nr_letters = int(input("How many letters would you like in your password\n"))
# nr_symbols = int(input("How many symbols would you like\n"))
# nr_numbers = int(input("How many numbers would you like\n"))

# password = ""

# for char in range(0, nr_letters):
#   password += random.choice(letters)

# for char in range(0, nr_symbols):
#   password += random.choice(symbols)

# for char in range(0, nr_numbers):
#   password += random.choice(numbers)

# # Angela Yu's Hard Solution

# password_list = []
# for char in range(0, nr_letters):
#   password_list.append(random.choice(letters))

# for char in range(0, nr_symbols):
#   password_list.append(random.choice(symbols))

# for char in range(0, nr_numbers):
#   password_list.append(random.choice(numbers))

# random.shuffle(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your Password is: {password}")

