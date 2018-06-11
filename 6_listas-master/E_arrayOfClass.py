"""
Array as Data structure
"""

students = ["Student 1", "Student 2", "Student 3", "Student 4"]
grades   = [10, 15, 12, 1] 

for i in range(len(students)):
    print(students[i], ":", grades[i])

students.append("Student 5")
grades.append(3)
for i in range(len(students)):
    print(students[i], ":", grades[i])
"""
result of: 

for i in range(len(students)):
    print(students[i], ":", grades[i])
"""