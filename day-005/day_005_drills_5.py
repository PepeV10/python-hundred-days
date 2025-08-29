# Ticket ID: [TICKET-P-01] (P for Practice)
# Assigned To: Pepe Venegas
# Title: Data Analysis: Count Vowels in User Feedback
# Complexity: Green Circle (Straightforward)
# 1. Business Context:
# The product team wants to run a simple analysis on user feedback comments to gauge the "readability" of the text. The first step is to count the number of vowels in a given piece of text.
# 2. Technical Requirements:
# You will be given a string of text.
# Your script must iterate through each character of the string using a for loop.
# You must use a variable to keep a running count of the vowels.
# For each character, check if it is a vowel (a, e, i, o, u). The check should be case-insensitive (i.e., A counts as a vowel).
# After the loop finishes, print the final count in a formatted string.
# 3. Starter Code & Acceptance Criteria:

feedback_text = "This is a sample sentence for our analysis. It is excellent!"
vowel_count = 0

# --- YOUR IMPLEMENTATION GOES HERE ---
# Hint: To make the check case-insensitive, you can convert each
# character to lowercase before you check it.

vowels = "aeiou"

for char in feedback_text.lower():
  if char in vowels:
    vowel_count += 1

print(f"The total number of vowels is: {vowel_count}")
