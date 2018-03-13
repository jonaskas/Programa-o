"""
Example 1
"""

grade1 = 15
grade2 = 6
avg_grade = (grade1 + grade2) / 2

if avg_grade >= 9.5 and grade1 >= 9.5 and grade2 >= 9.5:
    print("Student is aproved")
    if avg_grade >= 17:
        print("Give him a little start!!")
elif avg_grade >= 7.5 and grade1 >= 7.5 and grade2 >= 7.5:
    print("Exam")
elif avg_grade >= 5.5 and (grade1 >= 15 or grade2 >= 15):
    print("Assigment")
else:
    print("Student is not aproved")
