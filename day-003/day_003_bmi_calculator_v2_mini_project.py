print("Welcome to Pepe's BMI Calculator")
usr_height = float(input("Please enter your height in meters\n: "))
usr_weight = float(input("Please enter your weight in kilograms\n: "))

usr_bmi = usr_weight / (usr_height ** 2)

if usr_bmi < 18.5:
    print(f"Your BMI is {usr_bmi:.2f}. You are Underweight!")
elif usr_bmi < 25:
    print(f"Your BMI is {usr_bmi:.2f}. You are Normal!")
elif usr_bmi < 30:
    print(f"Your BMI is {usr_bmi:.2f}. You are Overweight.")
elif usr_bmi < 35:
    print(f"Your BMI is {usr_bmi:.2f}. You are Obese.")
else:
    print(f"Your BMI is {usr_bmi:.2f}. You are Clinically Obese.")


