# Ticket ID: [TICKET-R-01] (R for Review)
# Assigned To: Pepe Venegas
# Title: System Automation: Sanitize Marketing Contact Numbers
# Timebox Estimate: 20-30 Minutes
# 1. Business Context:
# The marketing department has a list of raw contact numbers from a registration form. Before they can be added to our new messaging system, they need to be categorized. The system requires each number to be labeled as "Email," "SMS," or "Voice" based on its format.
# 2. Technical Requirements:
# You will be given a list of numbers (integers).
# Your script must iterate through each number in the list using a for loop.
# Apply the following business logic using an if/elif/else structure:
# If the number is divisible by both 2 and 3, it's a high-priority "Email" contact.
# If the number is divisible by 2 (but not 3), it's a standard "SMS" contact.
# If the number is divisible by 3 (but not 2), it's a "Voice" call contact.
# If the number is divisible by neither, it's "Invalid Data."
# Instead of just printing the result, your script should create a new list that contains the string labels for each number.
# 3. Starter Code & Acceptance Criteria:

raw_contact_data = [12, 5, 6, 8, 9, 15, 10, 21, 4]
sanitized_list = [] # Your script will fill this list

# --- YOUR IMPLEMENTATION GOES HERE ---

for num in raw_contact_data:
  if num % 2 == 0 and num % 3 == 0:
    sanitized_list.append("High Priority Email Contact")
  elif num % 2 == 0:
    sanitized_list.append("Standard SMS Contact")
  elif num % 3 == 0:
    sanitized_list.append("Voice Call Contact")
  else:
    sanitized_list.append("Invalid Data")

# After your code runs, print the final list to verify.
print(sanitized_list)


