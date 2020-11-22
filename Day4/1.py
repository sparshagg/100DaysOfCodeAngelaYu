# Random Module For python related information we can also use - https://www.askpython.com/ More information on
# Random Module can be found on - https://www.askpython.com/python-modules/python-random-module-generate-random
# -numbers-sequences For the curious - https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v
# /random-vs-pseudorandom-number-generators
# For the curious - https://en.wikipedia.org/wiki/Mersenne_Twister


# Imported Random Module
import random

# Randint(x, y) generates random number between x and u including them.
random_integer = random.randint(1, 10) 
print(random_integer)

random_float = random.random() # Generates a random float between 0 and 1
print(random_float)

love_score = random.randint(1, 100) # Generates random numbers between 1 and 100
print(f"Your love score is {love_score}")