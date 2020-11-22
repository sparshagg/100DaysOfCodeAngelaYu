# Project
# Tip Calculator
# https://repl.it/@appbrewery/tip-calculator-start#main.py

import math

print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? \n₹ "))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15? \n"))
number_of_people = int(input("How many people to split the bill? \n"))
total_amount_to_be_paid = total_bill + ((percentage_tip/100) * total_bill)
split_amount = total_amount_to_be_paid/number_of_people
print(f"Each person should pay: ₹{math.ceil(split_amount)}")