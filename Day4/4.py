# Assignment - https://repl.it/@appbrewery/day-4-2-exercise#README.md
# Banker Roulette - Who will pay the bill?
# Hint - https://www.askpython.com/python/string/python-string-split-function


import random

names = input("Give me everybody's names, separated by comma.\n")
name_list = names.split(", ")
lenth_of_names_list = len(name_list)
random_number = random.randint(0, lenth_of_names_list-1)
print(f"{name_list[random_number]} will pay the bill today.")
