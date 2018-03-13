"""
Strings
"""

# Using constructors
print()
print(str(100))
print(str(3.04))

print('Single quotes')
print("double quotes")

# print('Quotes must match.") # Error: quotes must match

print()
print('"Mixed" quotes')
print("'Mixed' quotes")

print()
# Triple quotes - multiline string
message = '''Laborum reprehenderit voluptate dolore adipisicing
dolore aliqua magna voluptate commodo reprehenderit sit.'''
print(message)
message = """Laborum reprehenderit voluptate dolore adipisicing
dolore aliqua magna voluptate commodo reprehenderit sit."""
print(message)

print()
print(message[0])
