"""
Slicing
"""

students = ["student1", "student2", "student3", "student4", "student5"]

print()
backupList = students # refers to the same object
print(students)
print(backupList)
students[0] = "XXX"
print(students)
print(backupList)

print()
backupList = students[:] # slicing creates a copy
print(students)
print(backupList)
students[0] = "YYY"
print(students)
print(backupList)
