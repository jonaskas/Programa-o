"""
Rules
"""

# ***************************************************************
# 1. One statement per line
# ***************************************************************

print("Student 1")
print("Student 2")

print("Student 1"); print("Student 2") # valid but bad practice

"""
print("Student 1") print("Student 2") # Error
"""

# ***************************************************************
# 2. Leading whitespaces (spaces and tabs) are used to
#    define the level and the grouping of statements
# ***************************************************************

"""
 print("Student 1") # Error: starts with a space
"""

for i in range(2):
    print(i)

"""
for i in range(2):
    print(i) 
     print(i * 2) # Error: Insconsistent identation
"""

# ***************************************************************
# 3. Split code with \
# ***************************************************************

print("Laborum reprehenderit voluptate dolore adipisicing \
dolore aliqua magna voluptate commodo reprehenderit sit.")

# ***************************************************************
# 4. Naming: ^[a-zA-Z_$][a-zA-Z_$0-9]*$
# ***************************************************************

student_1 = "" # valid
_student_1 = "" # valid, can start with underscore

"""
2Count = 0 # Error: cannot start with numbers
"""

# ***************************************************************
# 5. Case Sensitive
# ***************************************************************

print("I´m case sensitive!") # OK

"""
Print("I´m case sensitive!") # Error: Python is case sensitive!
a = 0
print(A) # Error: Python is case sensitive!
"""
