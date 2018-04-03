"""
Parameters
"""

def write_names(value1, value2):
    print("{} : {}".format(value1, value2))

def print_max(value1, value2):
    if value1 >= value2:
        print(value1)
    else:
        print(value2)

write_names("Student1", "123")
write_names("Student2", "456")
write_names("Student3", "789")

print()
value1, value2 = 10, 12
print("Max ({}, {}): ".format(value1, value2))
print_max(value1, value2)
