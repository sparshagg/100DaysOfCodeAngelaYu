# Assignment - Tough one
# Love Calculator -> https://repl.it/@appbrewery/day-3-5-exercise#README.md

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = (name1 + name2).lower()
t = name.count("t")
r = name.count("r")
u = name.count("u")
e= name.count("e")
l= name.count("l")
o= name.count("o")
v= name.count("v")
true = t+r+u+e
love = l+o+v+e
number = str(true) + str(love)
number = int(number)
if number < 10 or number > 90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif number>=40 and number<=50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"Your score is {number}.")