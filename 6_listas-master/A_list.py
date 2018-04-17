"""
Lists
"""

# Empty list
student1_grades = []

# Append Values
student1_grades.append(16)
student1_grades.append(2)
student1_grades.append(10)
student1_grades.append(5)

# Change Value
student1_grades[0] = 20

# Slice
print("[:]:", student1_grades[:])
print("[0:2]:", student1_grades[0:2])
print("[-1:]:", student1_grades[-1:])

# remove first occurence 
student1_grades.remove(5)

# insert between 
student1_grades.insert(1, 5)
