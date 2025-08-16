# Ticket 209: Score Average (Easy)
# Task: Calculate and display an average score.
# Acceptance Criteria:
# 1. Create three variables: score1 = 8.5, score2 = 9.2, score3 = 7.8.
# 2. Calculate the total_score and the number_of_scores.
# 3. Calculate the average_score.
# 4. Print the average_score rounded to the nearest whole number
# 5. Print the average_score rounded to one decimal place

score1 = 8.5
score2 = 9.2
score3 = 7.8

total_score = score1 + score2 + score3
number_of_scores = 3
average_score = total_score / number_of_scores
whole_number_round = round(average_score)
one_decimal_round = round(average_score, 1)

print(f"The average score rounded to the nearest whole number is {whole_number_round}")
print(f"The average score rounded to one decimal place is {one_decimal_round}")

# Ticket 210: Game State Tracker (Easy)
# Task: Use augmented assignment operators to track a players' game state
# Acceptance Criteria:
# 1. Create a variable player_score initialized to 0.
# 2. Create a variable lives_remaining initialized to 3
# 3. The player finds a coin. Add 10 to player_score.
# 4. The player falls into a pit. Subtract 1 from lives_remaining.
# 5. Print the final score and lives remaining in a user-friendly f-string.

player_score = 0
lives_remaining = 3
player_score += 10
lives_remaining -= 1
print(f"Your final score is {player_score} and you were left with {lives_remaining} lives")

# Ticket 211: Simple Currency Converter(Medium)
# Task: Convert a USD amount to EUR and display it cleanly.
# Acceptance Criteria:
# 1. Create a variable usd_amount = 125.50.
# 2. Create a variable usd_to_eur_rate = 0.93.
# 3. Calculate the eur_amount.
# 4. Use an f-string and the round() function to print the result in the format: $125.50 USD is equal to €116.71 EUR. (The result must be rounded to two decimal places).

usd_amount = 125.50
usd_to_eur_rate = 0.93
eur_amount = usd_amount * usd_to_eur_rate
final_amount = round(eur_amount, 2)
print(f"The result from the convertion of ${usd_amount} USD to Euros is: €{final_amount} EUR")

