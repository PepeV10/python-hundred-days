# Ticket ID: [TICKET-P-02]
# Assigned To: Pepe Venegas
# Title: HR Automation: Generate Formatted Team Roster
# Complexity: Blue Square (Synthesis Required)
# 1. Business Context:
# The HR department needs a script to generate a formatted roster for a new project team. They have two separate lists: one with employee names and one with their assigned roles. The script needs to combine them into a single, readable output.
# 2. Technical Requirements:
# You will be given two lists, employee_names and assigned_roles, which are guaranteed to be the same length.
# You must iterate a number of times equal to the number of people on the team. (Hint: a for loop with range() and len() would be perfect here).
# Inside the loop, for each iteration, you must access the employee at the current index from the employee_names list AND the role at the same index from the assigned_roles list.
# You will then combine this information into a formatted string and add it to a new list called roster.
# 3. Starter Code & Acceptance Criteria:

employee_names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
assigned_roles = ["Lead Developer", "UI/UX Designer", "Data Analyst", "Project Manager", "QA Engineer"]
roster = []

# --- YOUR IMPLEMENTATION GOES HERE ---
# Loop from 0 up to the number of employees.
# Inside the loop, use the loop's counter variable as an index for both lists.

num_employees = len(employee_names)

for i in range(num_employees):
  name = employee_names[i]
  role = assigned_roles[1]

  roster_entry = f"{i + 1}, {name} - {role}"

  roster.append(roster_entry)


print("--- Project Alpha Team Roster ---")
# After your first loop, write another simple loop to print each item in the 'roster' list.
# for item in roster:
#   print(item)
# WHEN the script is run,
# THEN the final printed output must be:
for item in roster:
  print(item)
# --- Project Alpha Team Roster ---
# 1. Angela - Lead Developer
# 2. Ben - UI/UX Designer
# 3. Jenny - Data Analyst
# 4. Michael - Project Manager
# 5. Chloe - QA Engineer
