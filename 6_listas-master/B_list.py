"""
Lists - functions
"""

student2_grades = [10, 8, 4, 17]

print("Grades:", student2_grades)
print("10 in grades?", 10 in student2_grades)
print("10 in grades?", 11 in student2_grades)

student2_grades.sort()
print("Sorted grades:", student2_grades)

student2_grades.sort(reverse=True)
print("Sorted grades:", student2_grades)

student2_grades.reverse()
print("Sorted grades:", student2_grades)

# Extend list
ext = [18, 9, 7]
student2_grades.extend(ext) # same as student2_grades += ext
print("extended:", student2_grades)
