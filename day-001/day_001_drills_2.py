# Welcome Banner
# by Pepe Venegas - 08/10/2025
print("--- Welcome to the ProfileGen Tool ---\n")

# Gather User Vitals
first_name = input("What is your first name?\n: ")
last_name = input("What is your last name?\n: ")
fav_food = input("What is your favorite food?\n: ")

# Generate Full Name
full_name = first_name + " " + last_name
print(f"User profile created for: {first_name} {last_name}")

#Password Field Validation
password = input("Please enter what would be your dream password\n: ")
password_length = len(password)
print(f"Your password is {password_length} characters long")

# Multi-line Profile Summary
print(f"--- USER PROFILE ---\nName: {full_name}\nFavorite Food: {fav_food}\n--------------------")

