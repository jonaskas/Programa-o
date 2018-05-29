"""
Dictionary - Copy
"""

students = {}
students["john"] = "john@python.org"
students["Cecil"] = "student2@email.com"

backup_student = students.copy() # copy() perform a shallow copy
backup_student["john"] = "otherJohn@python.org"

print(students)
print(backup_student)