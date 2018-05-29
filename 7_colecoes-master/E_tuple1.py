"""
Tuple
"""

grades = ()
singleton_tuple = (2, ) # (2) is integer 2

first_year = (15, 20)
second_year = (15, 20)
third_year = (10, ) * 3 # (10, 10, 10)

grades += first_year + second_year + third_year # concatenation
grades2 = (first_year, second_year, third_year) # tuple of tuples

print()
print(grades, len(grades))
print(grades2, len(grades2))

print()
print("First year First grade: ", grades2[0][0])
