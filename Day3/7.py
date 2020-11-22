# Assignment
# https://repl.it/@appbrewery/day-3-4-exercise#README.md

print("Welcome to the Python Pizza Deliveries!")
total_bill = 0
pizza_size = input("What size Pizza do you want? S, M, or L? \n")
pepperoni = input("Do you want pepperoni? Y or N? \n")
extra_cheese = input("Do you want extra cheese? Y or N? \n")
if pizza_size.lower() == "s":
    total_bill += 15
    if pepperoni.lower() == "y":
        total_bill +=2
elif pizza_size.lower() == "m":
    total_bill += 20
    if pepperoni.lower() == "y":
        total_bill +=3
elif pizza_size.lower() == "l":
    total_bill +=25
    if pepperoni.lower() == "y":
        total_bill +=3
if extra_cheese.lower() == "y":
    total_bill += 1
print(f"Your final bill is: ${total_bill}.")