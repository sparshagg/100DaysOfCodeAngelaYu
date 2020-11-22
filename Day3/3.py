# Nested if statements and elif statements

# https://bit.ly/332UYdu
# print("Welcome to the rollercoaster!")
# input_height = int(input("What is your height in cm?\n"))
# if input_height >= 120:
#     print("You can ride the rollercoaster!")
#     input_age = int(input("What's your age?\n"))
#     if input_age >= 18:
#         print("You have to pay $12.")
#     else:
#         print("You have to pay $7.")
# else:
#     print("Sorry, you can't ride the rollercoaster.")

# https://bit.ly/2IXPOIK
# elif --> else + if
print("Welcome to the rollercoaster!")
input_height = int(input("What is your height in cm?\n"))
if input_height >= 120:
    print("You can ride the rollercoaster!")
    input_age = int(input("What's your age?\n"))
    if input_age >= 18:
        print("You have to pay $12.")
    elif input_age > 12 and input_age < 18:
        print("You have to pay $7.")
    else:
        print("You have to pay $5.")
else:
    print("Sorry, you can't ride the rollercoaster.")
