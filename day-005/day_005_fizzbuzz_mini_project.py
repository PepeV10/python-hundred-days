for number in range(1, 101):
  # 1. Check for the most specific condition FIRST: divisible by both 3 and 5.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # 2. Check for the next condition: divisible by 3.
  elif number % 3 == 0:
    print("Fizz")
  # 3. Check for the final condition: divisible by 5.
  elif number % 5 == 0:
    print("Buzz")
  # 4. If none of the above were true, just print the number.
  else:
    print(number)