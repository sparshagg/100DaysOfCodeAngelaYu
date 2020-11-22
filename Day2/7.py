# Assignment
# https://repl.it/@appbrewery/day-2-3-exercise#README.md
# Article is https://waitbutwhy.com/2014/05/life-weeks.html

input_age = int(input("Enter your current age: \n"))
average_lifetime = 90
age_left_in_years = average_lifetime - input_age
age_left_in_months = age_left_in_years * 12
age_left_in_weeks = age_left_in_years * 52
age_left_in_days = age_left_in_years * 365
print(f"You have {age_left_in_days} days, {age_left_in_weeks} weeks, and {age_left_in_months} months left.")