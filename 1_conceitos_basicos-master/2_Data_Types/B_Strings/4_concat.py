"""
Concatenation
"""

# concatenation of adjacent literal strings
message = "Python" " is " "Great"
print(message)

print()
message = ("SELECT * "
           "FROM students "
           "WHERE id > 0")
print(message)
message = "SELECT * " \
          "FROM students " \
          "WHERE id > 0"
print(message)

print()
message = "Python"
message = message + " is great!"
print(message)

print()
str1 = "SELECT * " 
str2 = "FROM students "
str3 = "WHERE id > 0"
message = str1 + \
          str2 + \
          str3
print(message)

print()
message = "{0}{1}{2}".format(str1, str2, str3)
print(message)
