# Ticket ID: CPG-11
# Title: EPIC - Integrate All Components into a Final Profile Card
# User Story: As a user, I want to answer all the profile questions in sequence and see a single, beautifully formatted profile card at the end.
# Acceptance Criteria:
# * The program must start with a welcome message.
# * The program must ask for:
# 1. Full Name
# 2. City
# 3. Country
# 4. Personal Motto
# 5. Favorite Animal
# 6. Birth Year
# After all questions are answered, the program must print a final, formatted "Profile Card" that looks like this, using the variables you've collected:
# ========================================
#           CLI User Profile Card
# ========================================

# Name: [User's Full Name]
# Location: [City], [Country]

# Motto: "[User's Motto]"
# (Motto contains [length] characters)

# Suggested Username: [animal][year]

# ========================================

full_name = input("What is your full name?\n: ")
user_city = input("What City do you currently live in?\n: ")
user_country = input("What Country do you currently live in?\n: ")
user_motto = input("What is your favorite quote or motto?\n: ")
length_motto = len(user_motto)
fav_animal = input("What is your favorite animal?\n: ")
birthyear = input("What year were you born in?\n: ")
# Remove ALL spaces from the animal name
clean_animal = ''.join(fav_animal.split())
potential_username = clean_animal + "_" + birthyear

print("==================================================")
print("           CLI User Profile Card       ")
print("==================================================")
print(f"Name: {full_name}")
print(f"Location: {user_city}, {user_country}")
print(f"Motto: {user_motto}")
print(f"Your favorite Motto or Quote contains {length_motto} characters")
print(f"Suggested Username: {potential_username}")
print("===================================================")

# A more advanced, single-print way:
profile_card = f"""
========================================
       CLI USER PROFILE CARD
========================================

Name: {full_name}
Location: {user_city}, {user_country}

Motto: "{user_motto}"
(Motto contains {length_motto} characters)

Suggested Username: {potential_username}

========================================
"""
print(profile_card)