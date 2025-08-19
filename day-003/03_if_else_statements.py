# Ticket 007: Odd or Even Checker
# Goal: Create a program that checks if a number enetered by the user is odd or even.
# Concepts: input(), int(), if/else, and the Modulo Operator(%).
# Hint: An even number is any number that can be divided by 2 with a remainder of 0.

print("Welcome to the Odd or Even Number Checker")
usr_number = int(input("Please enter a number\n: "))
if usr_number % 2 == 0:
  print("Your number is an Even number!")
else:
  print("Your number is an Odd number!")



# Ticket 009: Leap Year Checker (Simplified)
# Goal: Write a program that determines if a given year is a leap year.
# Simplified Rule: For this ticket, a leap year is any year that is evenly divisible by 4. (Note: The True rule is more complex, but we'll build up to that.)
# Concepts: input(), int(), %, if/else.

print("Welcome to Pepe's Leap Year Calculator!")
usr_year = int(input("Please enter the year you'd like to check:\n: "))

if usr_year % 4 == 0:
  print("It is a Leap Year!")
else:
  print("Not a Leap Year!")
  


# Ticket 011: Leap Year Checker (Full Project)
# Goal: Upgrade the Leap Year Checker from Ticket 009 to use the complete, official rules.
# The official Rules for a Leap Year:
# 1. A year is a leap year if its evenly divisible by 4...
# 2. Except if the year is also evenly divisible by 100...
# 3. Unless the year is also evenly divisible by 400...

print("Welcome to the Leap Year Calculator v2.0")
year = int(input("Please enter the year you want to check: "))

# Is the year divisible by 4? (The first big question)
if year % 4 == 0:
    # If yes, we need to check the exceptions.
    # Is it also divisible by 100? (The second question)
    if year % 100 == 0:
        # If yes, it's a century year. Now check the final exception.
        # Is it ALSO divisible by 400? (The third question)
        if year % 400 == 0:
            # This is the special case (like 2000).
            print("Leap year.")
        else:
            # This is a normal century year (like 1900, 2100).
            print("Not leap year.")
    else:
        # If it's divisible by 4 but not by 100 (like 1996).
        print("Leap year.")
else:
    # If it's not divisible by 4 at all.
    print("Not leap year.")
