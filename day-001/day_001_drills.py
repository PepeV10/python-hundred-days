# Ticket ID: CPG-01
# Title: Create Static Program Header
# User Story: As a user, I want to see a clear, static header when I run any script, so I know what program I'm using.
# Acceptance Criteria:
# * Write a single line of Python code that prints the following exact text: --- CLI Profile Generator v0.1 ---

print("--- CLI Profile Generator v0.1 ---")



# Ticket ID: CPG-02
# Title: Format Multi-Line Address Block
# User Story: As a developer, I need to be able to print a formatted address block using a single print statement to save spac ein teh code.
# Acceptance Criteria:
# * Using only one print() statement and the \n newline character, produce the following output:
### LearnCode Inc.
### 123 Syntax Street
### Programmer City, PY 12345

print("LearnCode Inc.\n123 Syntax Street\nProgrammer City, PY 12345")



# Ticket ID: CPG-03
# Title: Calculate String Length of Company Motto
# User Story: As a user, I want to know the character count of the company motto to see if it fits on the name badge.
# Acceptance Criteria:
# * The program must calculate the number of characters in the string "Code. Learn. Repeat." (Including the spaces and period).
# * The program must print only the final number (e.g. 18)

company_motto = "Code. Learn. Repeat."
print(len(company_motto))



# Ticket ID: CPG-04
# Basic User Greeting (Concatenation)
# User Story: As a user, I want the program to ask for my first name and greet me personally.
# Acceptance Criteria:
# * Ask the user for their first name.
# * Using only + concatenation, print the message: Welcome, [FirstName]!

first_name = input("What is your first name?\n: ")
print("Welcome " + first_name + "!")



# Ticket ID: CPG-05
# Titlte: Modern User Greeting(F-String)
# User Story: As a developer, I want to refactor the user greeting to use modern, readable f-strings.
# Acceptance Criteria:
# * Ask the user for their last name
# * Using an f-string, print the message: Analyzing profile user: [LastName].

last_name = input("What is your last name?\n: ")
print(f"Analyzing profile user: {last_name}")



# Ticket ID: CPG-06
# Title: Data Swap Utility
# User Story: As a developer, I need ta reliable way to swap the contents of two variables.
# Acceptance Criteria:
# * Create a variable data1 with the value "first".
# * Create a variable data2 with the value "second".
# Write code to swap their values
# Print data1 and data2 to confirm that their contents have been swapped.

data1 = "first"
data2 = "second"

data3 = data1
data1 = data2
data2 = data3

print(data1)
print(data2)
