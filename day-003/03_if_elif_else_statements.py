# Ticket 008: Roller Coaster Ticketing 1.0
# Goal: Modify the roller coaster code from the lesson. In addition to the existing height check, add a new condidtion to check if the person's height is exactly 120cm print a special message for them.
# Concepts: Nested if/else (or a simple modification, depending on your approach), == operator

# print("Welcome to Pepe's Roller Coaster!")
# height = int(input("What is your height in cm?\n: "))
# if height >= 120:
#   print("You can ride the roller coaster!")
#   if height == 120:
#     print("Congratulations, you barely made it!")
#   else:
#     print("You had no problem making the required height!")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# # Roller Coaster v2.0
# print("Welcome to Pepe's Roller Coaster!")
# usr_height = int(input("Please enter your height in cm\n: "))

# if usr_height >= 120:
#   print("Congratulations, you can ride the rollercoaster!")
#   age = int(input("Please enter your age\n: "))
#   if age <= 12:
#     print("Please pay $5.00")
#   elif age <= 18:
#     print("Please pay $7.00")
#   else:
#     print("Please pay $12.00")
# else:
#   print("Sorry, you have to grow taller before you can ride it!")

# # Rollercoaster v3.0
# print("Welcome to Pepe's Roller Coaster!")
# usr_height = int(input("Please enter your height in cm\n: "))
# bill = 0

# if usr_height >= 120:
#   print("Congratulations, you can ride the rollercoaster!")
#   age = int(input("Please enter your age\n: "))
#   if age <= 12:
#     bill = 5
#     print("Child tickets are $5.00")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.00")
#   else:
#     bill = 12
#     print("Adult tickets are $12.00")

#   wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
#   if wants_photo == "y":
#     bill += 3
#     print("You have to pay an extra $3.00")

#   print(f"Your final bill is:{bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride it!")



# Rollercoaster v4.0
print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the Rollercoaster!")
  age = int(input("What is your age? "))

  if age < 12:
    bill = 5
    print("Child tickets are $5.00")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.00")
  elif age >= 45 and <= 55:
    print("Congratulations, because of your mid-life crisis, you get in for free!")
  else:
    bill = 12
    print("Adult tickets are $12.00")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print("Your final bill is ${bill:.2f}")

else:
  print("You must grow taller first in order to ride the Rollercoaster!")


  # Ticket 010: Pizza Order Practice
# Goal: Build an automatic pizza order program
# Business rules:
# 1. Based on a user's order, work out their final bill.
# 2. Small Pizza: $15
# 3. Medium Pizza: $20
# 4. Large Pizza: $25
# 5. Pepperoni for Small Pizza: +$2
# 6. Pepperoni for Meidum or Large Pizza: +$3
# 7. Extra Cheese for any size pizza: +$1

# print("Welcome to Pepe's Pizzeria!")
# bill = 0
# usr_pizza_size = input("What size Pizza do you choose? 's' for Small, 'm' for Medium, 'l' for Large\n: ")
# if usr_pizza_size == 's':
#   bill += 15
# elif usr_pizza_size == 'm':
#   bill += 20
# else:
#   bill +=25

# extra_pepperoni = input("Would you like some extra Pepperoni on your Pizza? 'y' for Yes, 'n' for No\n: ")
# if extra_pepperoni == 'y':
#   if usr_pizza_size == 's':
#     bill += 2
#   else:
#     bill += 3

# extra_cheese = input("Would you like some extra cheese? 'y' for Yes, 'n' for No\n: ")
# if extra_cheese == 'y':
#   bill += 1

# print(f"Your order is complete! Please pay: ${bill:.2f} Thank you!")



# Refactored Code with Dynamic Order Summary

print("Welcome to Pepe's Pizzeria!")
bill = 0
# 1. Initialize a string to hold the order details.
order_details = "" 

usr_pizza_size = input("What size Pizza do you choose? 's' for Small, 'm' for Medium, 'l' for Large\n: ")

# Block 1: Set the base price AND the base description.
if usr_pizza_size == 's':
  bill = 15
  order_details = "a Small Pizza"
elif usr_pizza_size == 'm':
  bill = 20
  order_details = "a Medium Pizza"
else:
  bill = 25
  order_details = "a Large Pizza"

# Block 2: Add pepperoni cost AND update the description.
extra_pepperoni = input("Would you like some extra Pepperoni on your Pizza? 'y' for Yes, 'n' for No\n: ")
if extra_pepperoni == 'y':
  if usr_pizza_size == 's':
    bill += 2
  else:
    bill += 3
  # 2. Append to the existing string.
  order_details += " with extra pepperoni" 

# Block 3: Add cheese cost AND update the description.
extra_cheese = input("Would you like some extra cheese? 'y' for Yes, 'n' for No\n: ")
if extra_cheese == 'y':
  bill += 1
  # 3. Append again. This handles all cases (with/without pepperoni).
  if extra_pepperoni == 'y':
      order_details += " and extra cheese"
  else:
      order_details += " with extra cheese"

# Final Output: Combine our two generated variables.
print(f"\nYour order: {order_details}.")
print(f"Your final bill is: ${bill:.2f}. Thank you!")



# # Angela's Solution
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size Pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# elif size == "L":
#   bill += 25
# else:
#   print("You typed the wrong inputs.")

# if pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your final bill is: {bill:.2f}.")
