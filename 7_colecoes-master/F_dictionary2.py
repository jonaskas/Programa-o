"""
Dictionary - For
"""

#Add
students = {}
students["john"] = "john@python.org"
students["Cecil"] = "student2@email.com"

print()
for name, email in students.items():
    print("Name: {} | email: {}".format(name, email))

print()
for name, email in sorted(students.items()):
    print("Name: {} | email: {}".format(name, email))

print()
for k in students.keys():
    print("keys: {}".format(k))

print()
for v in students.values():
    print("Values: {}".format(v))

print()
for k in students.keys():
    print("Values: {}".format(students[k]))



