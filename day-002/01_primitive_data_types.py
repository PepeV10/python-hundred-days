# Ticket 201: String Subscripting Practice (Easy)
# Task: Create a string variable containing the word "Cybersecurity".
# Acceptance Criteria:
# 1. Print the first character of the string.
# 2. Print the third character of the string.
# 3. Print the last character of the string using negative indexing.

future_career = "Cybersecurity"
print(future_career[0])
print(future_career[2])
print(future_career[-1])



# Ticket 202: Data Type Exploration (Easy)
# Task: Create four variables, one for each new data type we learned (Integer, Float, Boolean, String)
# Acceptance Criteria:
# 1. Create an integer variable num_users and assign it a large number underscores for redability (e.g.25 million).
# 2. Create a float variable network_latency and assign it a value like 0.54.
# 3. Create a boolean variable is_logged_in and set it to True.
# 4. Create a string variable server_status_code and assign it the value "200".
# Print each variable

num_users = 25_000_000
network_latency = 0.54
is_logged_in = True
server_status_code = "200"

print(f"Number of Users: {num_users}\n"
      f"Network Latency: {network_latency}\n"
      f"Is Logged In: {is_logged_in}\n"
      f"Server Status Code: {server_status_code}")



# Ticket 203: Spot the Bug (Medium)
# Code:
# zip_code = 90210
# print("The second digit is:", zip_code[1]) # This line will cause a TypeError
# Acceptance Criteria: 
# 1. Add a comment explaining why the original code fails.
# 2. Write a corrected version of the code that sucessfully prints the second digit(0).
# 3. Hint: How can you treat the zip code as a sequence of characters instead of a number?

zip_code = "90210" #The original code fails because you cannot use indexing on an integer type, only on strings.
print("The second digit from the zipcode is:", zip_code[1])



# Ticket 204: Mini-Project User Profile Snippet (Medium)
# Task: Create a small script that stores and prints a user's basic profile information
# Acceptance Criteria:
# 1. Create variables for a username(string), age(integer), subscription price(float), and active status(boolean).
# 2. Use an f-string to print a summary sentence, for example:
# - user 'code_master' (Age: 30) has an active subscription costing $9.99
# 3. Use subscripting to print the user's initial (the first letter of their username).

username = "master_coder"
age = 35
subscription_price = 9.99
is_active = True
user_initial = username[0]

print(f"User '{username}' (Age: {age}) has an active subscription (Status: {is_active}) costing ${subscription_price}.")

print(f"User's initial is: {user_initial}")
