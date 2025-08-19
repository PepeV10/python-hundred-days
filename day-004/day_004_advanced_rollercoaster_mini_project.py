# Advanced Rollercoaster Pass
# Systems & Architechture Overview: This kind of multi-condition logic is the bread and butter of systems that handle permissions, pricing tiers, or validation. Think about a movie ticketing website. It checks your age, the time of day (matinee pricing), and if yuou have a loyalty membership. This ticket simulates a simple version fo that logic.
# Problem Statement: Our theme park needs to update it's rollercoaster access logic. Write a program that first asks for a user's height in cm and their age. Then, it checks if they ahave a VIP Pass (a simple 'yes' or 'no' input).
# Rules:
# 1. Base requirement: Must be over 120cm tall to ride. If not, they can't ride at all.
# 2. If they are tall enough, the ticket price is determined by age:
# * Anyone 18 or older pays $12
# * Anyone between 12 and 17 (inclusive) pays $7
# * Anyone under 12 pays $5
# 3. If a rider of any age has a VIP Pass (answered 'yes'), they get to ride for free, regardless of their age-based price.
# 4. The program should print a clear message indicating the price they have to pya or if they are not tall enough to ride. 

print("Welcome to Pepe's Rollercoaster!")
# Get height first, as it's the primary gatekeeper for riding.
usr_height = int(input("What is your height in centimeters?\n: "))

# Initialize the bill to 0. We will only change it if the user has to pay.
bill = 0

# --- The Main Gatekeeper Check ---
# This first 'if' checks the one condition that can disqualify anyone.
if usr_height > 120:
  print("Congratulations, you are tall enough to ride the rollercoaster.")
  
  # Get the rest of the information only if they are tall enough.
  usr_age = int(input("What is your age?\n: "))
  is_vip = input("Do you have a VIP Pass? 'yes', or 'no'. ").lower() # Added .lower() for robustness

  # --- The VIP Check ---
  # This is the primary logic fork. Are they a VIP or not?
  if is_vip == 'yes':
    # VIPs are a special case. They ride free. We handle their entire journey here.
    # Notice the bill is already 0, so we don't even need to set it.
    print("Welcome, VIP! You ride for free. Enjoy the ride!")
  
  else:
    # --- The Pricing Logic (for Non-VIPs only) ---
    # This entire block ONLY runs if they are NOT a VIP.
    if usr_age < 12:
      bill = 5
      print("Your child ticket is $5.00.")
    elif usr_age <= 17: # You can also write this as: 12 <= usr_age <= 17
      bill = 7
      print("Your youth ticket is $7.00.")
    else: # This covers anyone 18 and older.
      bill = 12
      print("Your adult ticket is $12.00.")
      
    # --- Final Bill Print (for Non-VIPs only) ---
    # Because this is inside the 'else' for non-VIPs, a VIP will never see it.
    # This solves the "Your final bill is $0.00" issue for VIPs.
    print(f"Your final bill is ${bill:.2f} USD.")

# --- The "Too Short" Case ---
# This 'else' pairs with the very first 'if'. If they fail the height check,
# this is the only other message they will see.
else:
  print("Sorry, but for your safety, you must grow to at least 120cm before you can ride the rollercoaster.")
