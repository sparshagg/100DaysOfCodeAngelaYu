# Assignment
# Heads or Tails - https://repl.it/@appbrewery/day-4-1-exercise#README.md

# Seed number is used to generate only one combination of random number. We don't need it.
# It's just given in the repl to test our code.

import random

random_number = random.randint(0,1)
if random_number == 1:
    print("Heads")
else:
    print("Tails")