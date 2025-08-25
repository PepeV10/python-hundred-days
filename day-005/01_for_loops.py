# Ticket ID: [05-01]
# Assigned To: Pepe Venegas
# Day 5 - Loops & Data Aggregation
# Title: Feature: Calculate Average Student Height for Annual Health Report

# 1. Business Context & User Story:
# The data entry team has provided us with a list of student heights for the annual school health report. The data comes in as a single string of text from a legacy system, with each height separated by a aspace. Our system needs a script to process this string, calculate the average height, and prepare it for the report.

# User Story: "Aas a school administrator, I need to automatically calculate the average height from a list of manually entered heights, so that I can efficiently generate our annual health and wellness report without manual calculation errors."

# Technical Requirements & Constraints:
# Input: The script will receive a string of space-separated numbers (e.g., 156 178 165 171 187).
# Processing:
# * The provided started code will handle the initial conversion from a single string to a list of integers. Your work begins after that point.
# * To build foundational skills, the solution must use a for loop to process teh list.
# * The use of the buil-in sum() and len() functions for the primary calculation is prohibited for this ticket. The goal is to manually implement the logic of summing and counting using a loop.
# Output: The final calculated average height, rounded to the nearest whole number. 

# 3. Acceptance Criteria (Definitio of "Done"):
# * WHEN the user inputs "156 178 165 171 187".
# * THEN the script must output 171.
# * AND the code must correctly handle inputs with a different number of heights.
# * AND the core logic must be implemented using a for loop.

# STARTER CODE

# [DO NOT MODIFY] - This block simulates receiving data from the legacy system.
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# [YOUR IMPLEMENTATION] - Write your code below this line to resolve the ticket.
# =========================================================================#

total_height = 0
number_of_students = 0
for height in student_heights:
  total_height += height
  number_of_students += 1

average_height = total_height / number_of_students
rounded_average = round(average_height)
print(rounded_average)





# Ticket ID: [TICKET-05-02]
# Assigned To: Pepe Venegas
# Sprint: Day 5 - Loops & Data Aggregation
# Title: Feature: Find Highest Student Score

# 1. Business Context & User Story:
# Following the successful deployment of the height calculator, the academic department has a similar request. They have a list of student scores from a recent exam and need a script to quickly identify the highest score in the set without manually sorting or scanning the list.
# User Story: "As a teacher, I want to input a list of student scores and have the program tell me the maximum score, so I can establish the grading curve for my class."

# 2. Technical Requirements & Constraints:
# Input: The script will receive a string of space-separated numbers (e.g., "78 65 89 86 55 91 64 89").
# Processing:
# The provided starter code will handle the conversion from a string to a list of integers.
# The solution must use a for loop to process the list.
# The use of the built-in max() function is prohibited. You must implement the logic to find the maximum value yourself.
# Output: A formatted f-string: "The highest score in the class is: X", where X is the highest score.

# 3. Acceptance Criteria (Definition of "Done"):
# WHEN the user inputs "78 65 89 86 55 91 64 89"
# THEN the script must output "The highest score in the class is: 91".
# AND the core logic must be implemented using a for loop.

# [DO NOT MODIFY] - This block simulates receiving data from the academic system.
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# [YOUR IMPLEMENTATION] - Write your code below this line to resolve the ticket.
# =========================================================================

highest_so_far = student_scores[0]
for max in student_scores:
  if max > highest_so_far:
    highest_so_far = max

print(f"The highest score is: {highest_so_far}")





# Angela Yu's Solution
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

max_score = 0
for score in student_scores:
  if score > max_score:
    max_score = score

print(max_score)