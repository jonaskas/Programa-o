"""
return
"""

def sum(*numbers):
    value = 0
    for n in numbers:
        value += n
    return value

a = sum(0)
print(a)
print(sum(4, 3))
print(sum(0, 3, 5, 4))
