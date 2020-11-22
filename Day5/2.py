# Assignment - Average Height
# Starting code and tips - https://repl.it/@appbrewery/day-5-1-exercise#README.md

student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
sum_of_student_heights = 0
for i in range(len(student_heights)):
    sum_of_student_heights += student_heights[i]
average_height = sum_of_student_heights / len(student_heights)
print(average_height)
