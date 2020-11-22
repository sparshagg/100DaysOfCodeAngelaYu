# Multiple if statements in succession
# Rollercoaster again with some modifications - https://bit.ly/2IYpePL

print("Welcome to the rollercoaster!")
input_height = int(input("What is your height in cm?\n"))
total_bill = 0
if input_height >= 120:
    print("You can ride the rollercoaster!")
    input_age = int(input("What's your age?\n"))
    if input_age >= 18:
        print("Adult tickets are for $12.")
        total_bill += 12
    elif input_age > 12 and input_age < 18:
        print("Youth tickets are for $7.")
        total_bill += 7
    else:
        print("Child tickets are for $5.")
        total_bill += 5
    input_photos = input("Do you want photos? Yes or No? \n")
    if input_photos.lower() == "yes":
        total_bill += 3
        print(f"Your final bill is ${total_bill}.")
    elif input_photos.lower() == "no":
        print(f"Your final bill is ${total_bill}.")
else:
    print("Sorry, you can't ride the rollercoaster.")
