# Assignment Not Easy on Leap Year
# https://repl.it/@appbrewery/day-3-3-exercise#README.md
# What is a leap year? https://www.youtube.com/watch?v=xX96xng7sAE
# Leap Year Flow chart https://bit.ly/36S1PHK

year = int(input("Which year do you want to check? "))
if year%100==0:
    if year%400==0:
        print("Leap year.")
    else:
        print("Not leap year.")
elif year%4==0 and year%100!=0:
    print("Leap year.")
else:
    print("Not leap year.")