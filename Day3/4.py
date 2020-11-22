# Assignment
# BMI 2.0
# https://repl.it/@appbrewery/day-3-2-exercise#README.md

print("Welcome to the BMI calculator 2.0!")
input_height = float(input("What's your height in m?\n"))
input_weight = float(input("What's your weight in kg?\n"))
bmi = input_weight/(input_height**2)
bmi = round(bmi, 2)
if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
