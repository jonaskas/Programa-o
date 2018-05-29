"""
Dictionary
- key:value pair.
- keys are uniques and must be immutables.
"""

#Add
students = {}
students["john"] = "student1@email.com"
students["Cecil"] = "student2@email.com"

print("Number of students:", len(students))

print()
students["john"] = "john@python.org"
print(students)

print()
print(students.get("john")) # john@python.org
print(students.get("ford")) # None
print(students.get("john", -1)) # john@python.org
print(students.get("ford", -1)) # -1

print()
if "john" in students:
    print("John exit!!")
