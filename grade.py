#ifelse_grade.py

score = eval(input("Enter score: "))
#score = 71.0

if score >= 90.0:
    grade = "A"

elif score >= 80.0:
    grade = "B"

elif score >= 70.0:
    grade = "C"

elif score >= 60.0:
    grade = "D"

else:
    grade = "F"

print(grade)
print('Bye')
