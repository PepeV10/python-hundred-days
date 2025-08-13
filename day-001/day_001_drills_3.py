# Ticket ID: CPG-07
# Title: Capture and Store User's Full Name
# User Story: As a user, I want to provide my full name so it can be used later in my profile
#Acceptance Criteria:
# * Ask the user for their full name.
# * Store the result in a well-named variable(e.g., full_name).
# * To confirm it was captured, print the variable back to the user.

full_name = input("What is your full name?\n: ")
print(f"Your full name is: {full_name}")



# Ticket ID: CPG-08
# Title: Capture and Store User's Location
# User Story: As a user, I want to provide my city and country so the profile can show my location.
# Acceptance Criteria:
# * Ask the user fo rhte city they live in. Store it in a variable.
# * Ask the user for the country they live in. Store it in another variable.
# * Using an f-string, print a confirmation message: Location Captured: [City], [Country]

user_city = input("What City do you currently live in?\n: ")
user_country = input("What Country do you currently live in?\n: ")
print(f"Location Captured: {user_city}, {user_country}")



# Ticket ID: CPG-09
# Title: Capture and Analyze Personal Motto
# User Story: As a user, I want to provide a personal motto and know how long it is.
# Acceptance Criteria:
# * Ask the user for their favorite quote or personal motto.
# * Store the motto in a variable.
# * Create a second variable that stores the length of the motto.
# * Print a message: Your motto has [length] characters.

fav_quote = input("What is your favorite quote or personal motto?\n: ")
length_fav_quote = len(fav_quote)
print(f"Your motto has {length_fav_quote} characters")



# Ticket ID: CPG-10
# Title: Generate a Suggested Username
# User Story: As a user, I want the system to suggest a username for me based on my information.
# Acceptance Criteria:
# * Ask the user for hteir favorite animal.
# * Ask the user for the year they waere born.
# * Combine these two inputs to create a username (e.g., panther1990)
# * Print the suggested username to the user.

fav_animal = input("What is your favorite animal?\n: ")
birth_year = input("What year were you born?\n: ")
# Remove ALL spaces from the animal name
clean_animal = ''.join(fav_animal.split())
potential_username = clean_animal + "_" + birth_year
print(f"Your suggested Username is: {potential_username}")