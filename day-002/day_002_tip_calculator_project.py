# ## Daily Project: The Tip Calculator

# **Objective:** Create a command-line tool that calculates the split bill amount per person, including a user-defined tip.

# **1. Inputs (The "Knowns"):**
# - Total bill amount (`str` from `input()`, must be converted to `float`).
# - Tip percentage (`str` from `input()`, must be converted to `int`).
# - Number of people to split the bill (`str` from `input()`, must be converted to `int`).

# **2. Process (The "Bridge"):**
# - Greet the user with a welcome message.
# - Get the three inputs from the user, making sure to convert them to the correct numeric types.
# - Calculate the total amount with tip included.
#   - Formula: `total_bill * (1 + tip_percentage / 100)`
# - Calculate the final amount per person.
#   - Formula: `total_amount_with_tip / number_of_people`
# - Format the final amount to have exactly two decimal places.

# **3. Output (The "Unknown"):**
# - A single, formatted string that clearly states the amount each person should pay.
#   - Example: `"Each person should pay: $19.93"`

# Ticket ID: LCI-D02-P1
# Title: Build the Tip Calculator v1.0
# User Story: As a diner, I want to easily calculate how to split a bill with a tip among several people, so that I can avoid manual math and pay the correct amount.
# Acceptance Criteria(AC):
# 1. The program must start by printing the welcome message: "Welcome to the tip calculator".
# 2. It must prompt the user for the total bill (e.g. "What was the total bill $").
# 3. It must prompt the user for the disired tip percentage (e.g. "What percentage tip would you like to give? 10, 12, 15, 0r 20").
# 4. It must prompt the user fo rhte number of people splitting the bill (e.g. "How many people to split the bill? ").
# 5. All three user inputs must be correctly converted from str to their appropriate numeric types (float or int).
# 6. The program must calculate the correct amount each person should pay.
# 7. The final output must be formatted to exactly two decimal palces, even if the last digit is a zero (e.g., $33.60). Hint: the f-string format specifier we discussed is perfect for this!
# 8. The final output must be presented in a clear f-string: f"Each peson should pay: ${final_amount}".


print("Welcome to the Pepe's Tip Calculator!")
total_bill = float(input("What was the Total Bill? \n $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, 15, or 20?\n %"))
number_of_people = int(input("How many people to split the bill with?\n"))
total_amount_with_tip = total_bill * (1 + tip_percentage / 100)
final_amount_per_person = total_amount_with_tip / number_of_people
print(f"Each person should pay: ${final_amount_per_person:.2f}")

# # More professional version
# # Step 1: Calculate the tip multiplier (e.g., 12% -> 1.12)
# tip_multiplier = 1 + tip_percentage / 100

# # Step 2: Calculate the total bill including the tip
# total_bill_with_tip = total_bill * tip_multiplier

# # Step 3: Calculate the individual split
# bill_per_person = total_bill_with_tip / number_of_people

# # Step 4: Prepare the final, formatted amount for display
# final_amount = f"{bill_per_person:.2f}" 

# print(f"Each person should pay: ${final_amount}")

