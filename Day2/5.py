# Assignment
# What is BMI? https://en.wikipedia.org/wiki/Body_mass_index
# https://repl.it/@appbrewery/day-2-2-exercise#README.md

input_height = float(input("Enter your height: \n"))
input_weight = float(input("Enter your weight: \n"))
weight_square = input_weight ** 2
bmi = input_height/weight_square 
print(bmi)