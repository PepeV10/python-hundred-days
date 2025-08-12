fav_city = input("What is your favorite city?\n")
print(f"Oh, I've always wanted to visit {fav_city}!\n")

name_and_pet = input("Ener Your name, then a comma, then your pet's name: ").split(",")
print(f"{name_and_pet[0].strip()}'s best friend is {name_and_pet[1].strip()}")

noun = input("Give me a noun(any noun that you want)\n")
verb = input("Give me a verb(any verb that you want)\n")
adjective = input("Give me an adjective(any adjective that you want)\n")
print(f"The {adjective} {noun} decided to {verb} over the lazy dog.")