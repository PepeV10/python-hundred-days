# Ticket 205: Basic Operations (Easy)
# Task: Use variables and basic mathtematics to solve the following.
# Acceptance Criteria:
# 1. A server has 100 users and 25 are active. Calculate the percentage of active users. (Hint: active_uers / total_users * 100)
# 2. Calculate how many tasks remain if a team starts with 50 tasks and finishes 12.
# 3. A backup system has 5 GB of data storage, and you need to back up 2.5 GB. How much space is left?

total_users = 100
active_users = 25
percentage_users = (active_users / total_users) * 100
print(f"The percentage of active users is: {percentage_users}%")

starting_tasks = 50
finished_tasks = 12
remaining_tasks = starting_tasks - finished_tasks
print(f"The remaining tasks are: {remaining_tasks}")

total_data_storage = 5
backup_data_storage_needed = 2.5
space_data_storage_after_backup = total_data_storage - backup_data_storage_needed
print(f"Remaining data storage: {space_data_storage_after_backup} GB")



# Ticket 206: The Division Problem(Medium)
# Task: Use the correct division operator for the following scenarios and print the result.
# Acceptance Criteria:
# 1. Calculate the exact cost per item if a bulk purchase of 7 items cost $40.
# 2. Calculate how many complete pages of search results you can display if you have 30 results and your page size is 7 results per page.

bulk_purchase_items = 7
bulk_purchase_cost = 40
cost_per_item = bulk_purchase_cost / bulk_purchase_items
print(f"The exact cost per item is: ${cost_per_item}")

total_results = 30
page_size = 7
complete_pages = total_results // page_size
print(f"You can display {complete_pages} complete pages of research results.")


# Ticket 207: PEMDAS DRILL(Medium)
# Task: Calculate the result of the following complex expression using Python first, then use Python to verify your answer.
# Expression: 10 + 5 * 2 ** 3 / 4
# Acceptance Criteria:
# 1. Print the Python code and it's result
# 2. Add a comment explaining the steps of calculation according to PEMDAS

expression_result = 10 + 5 * 2 ** 3 / 4
print(f"The result of the expression 10 + 5 * 2 ** 3 / 4 is: {expression_result}")

# According to PEMDAS:
# 1. Parentheses: There are no parentheses to evaluate first.
# 2. Exponents: 2 ** 3 is evaluated first, resulting in 8.
# 3. Multiplication and Division: Next, 5 * 8 is evaluated, resulting in 40. Then, 40 / 4 is evaluated, resulting in 10.
# 4. Addition: Finally, 10 + 10 is evaluated, resulting in 20.



# Ticket 208: Mini-Project-Data Transfer Rate(Hard)
# Task: Calculate the total time in minutes required to transfer a file.
# Acceptance Criteria: 
# 1. A variable file_size_mb set to 1200.
# 2. A variable transfer_rate_mb_per_min set to 50.
# 3. Calculate the total transfer time in minutes.
# 4. Calculate the transfer time in seconds.

file_size_mb = 1200
transfer_rate_mb_per_min = 50
total_transfer_time_min = file_size_mb / transfer_rate_mb_per_min
total_transfer_time_sec = total_transfer_time_min * 60
print(f"The total transfer time in minutes is: {total_transfer_time_min} minutes")

