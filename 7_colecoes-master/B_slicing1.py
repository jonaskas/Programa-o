"""
Slicing
"""

students = ["student1", "student2", "student3", "student4", "student5"]

print("Last element:", students[-1])
print("First student first character:", students[0][0]) 

print()
print(students[ 0 : 2 ])  
print(students[ 1 : len(students) - 1 ]) 
print(students[ 1 : -2 ]) 
print(students[ 3 : ]) # 3 to the end
print(students[ : 3 ]) # start to 3
print(students[ : -2 ]) # start to -2
print(students[ : ]) 

print()
print(students[ : 4 : 2]) # increment of 2
print(students[ : -1 : 2])
print(students[::2])
print(students[::-1])
print(students[::-2])
