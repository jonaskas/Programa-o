"""
Integer
- Integers are only limited by available memory
"""

value = 10
print(value)

value = 0b10 # binary
print(value)
value = 0o10 # octal
print(value)
value = 0x10 # hexadecimal
print(value)

# Using constructors
print()
value = int(2.5)
print(value)
value = int(-2.5)
print(value)

# Using constructors with base
print()
value = int("10")
print(value)
value = int("10", 2) # binary
print(value)
value = int("10", 8) # octal
print(value)
value = int("10", 16) # hexadecimal
print(value)
