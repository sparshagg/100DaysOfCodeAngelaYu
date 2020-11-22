# Number manipulation and f strings in python

print(round(8/3))
print(round(8/3, 2))
print(round(2.66666666, 2))
print(8//3)
print(type(8//3))

score = 0
# Everytime user scores 2 points
# score = score + 2 -> Instead of this we can use:
score += 2 # Valid for other operators as well.

# f strings
print(f"Your score is {score}")