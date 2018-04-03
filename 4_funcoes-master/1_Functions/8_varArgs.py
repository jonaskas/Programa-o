"""
Variable number of arguments
"""

def sum(*numbers):
    value = 0
    for n in numbers:
        value += n
    print(value)

print()
sum(0)
sum(4, 3)
sum(0, 3, 5, 4)
