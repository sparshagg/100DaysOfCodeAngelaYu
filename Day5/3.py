# Assignment - High Score
# Starting code and instructions - https://repl.it/@appbrewery/day-5-2-exercise

student_scores = input("Input a list of student scores \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

a = student_scores[0]
for i in range(1, len(student_scores)):
    if student_scores[i] > a:
        a = student_scores[i]
print(f"The highest score in the class is: {a}.")