fruits = ["strawberry", "raspberry", "blueberry", "blackberry", "cherry", "apple", "banana", "kiwi", "pineapple", "pear"]

for fruit in fruits:
  if fruit == "apple":
    print(f"We found the {fruit}, now we can make tasty {fruit} pies!")


laundry_basket = ["shirt", "sock", "pants", "sock", "towel", "sock", "tie", "sock"]

for item in laundry_basket:
  if item == "sock":
    print("Found a sock!")
  else:
    print(f"This is not a sock, it's a {item}")
  
blocks = ["red", "green", "blue", "yellow", "blue", "red", "purple", "white", "black", "pink"]
for block in blocks:
  if block == "red":
    print("This goes in the Red Pile!")
  elif block == "blue":
    print("This goes in the Blue Pile!")
  elif block == "white":
    print("This goes in the White Pile!")
  else:
    print(f"This block is {block} and goes in this pile with the rest of the blocks that are not Red, Blue or White")


coins = ["quarter", "penny", "dime", "penny", "penny", "dime", "quarter", "quarter", "dime", "penny"]
penny_count = 0

print(f"Starting count: {penny_count}")

for coin in coins:
  if coin == "penny":
    penny_count += 1

print(f"Final Count: {penny_count}")