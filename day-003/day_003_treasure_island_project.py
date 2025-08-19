# Project Ticket: Treasure Island

# Ticket 012: Treasure Island - Choose Your Own Adventure Game
# Goal Logic:
# 1. Ask the user to choose "left" or "right". "Right" is a game over.
# 2. If "left", ask the user to "swim" or "wait". "Swim" is a game over.
# 3. If "wait", ask the user to choose a door. "red", "blue", or "yellow". "Red" and "Blue" are game overs. "Yellow" is a win.
# Technical Requirements:
# * Use nested if/elif/else statements to represent the choices.
# * Use the .lower() method on all user inputs to make the game case-sensitive.
# * Feel free to add your own story, ASCII art, and flavor text.

print("Welcome to Treasure Island!\nYour mission is to find the treasure!")
print("Remember to choose your options carefully!\nAfter all, you only have one life, so take care of it...")

crossroad = input("You are at a crossroad. Where do you want to go?\n\tType 'left' or 'right'\n: ").lower()
if crossroad == "left":

  lake = input("You've come to a huge lake. There is an Island in the middle of the lake.\n\tType 'wait' to wait for a boat or 'swim' to swim acrross to the Island\n: ").lower()
  if lake == 'wait':
    
    door = input("You arrive at the Island unharm. There is a house with three doors.\n\tOne 'red', one 'yellow', and one 'blue'. Which color do you choose?\n: ").lower()
    if door == 'yellow':
      print("Congratulations YOU WIN!")
    elif door == 'red':
      print("You walk into a room that catches fire and burn to death. GAME OVER!")
    elif door == 'blue':
      print("Huge beast get into the room and eat you alive. GAME OVER!")
  
  else:
    print("You are attacked by a giant trout. GAME OVER!")

else:
  print("You have fallen into a deep hole. GAME OVER!")
