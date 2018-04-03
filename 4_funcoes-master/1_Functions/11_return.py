"""
return
"""

def my_max(*numbers):
    max = None
    for value in numbers:
        if max is None or max < value:
            max = value
    return max

def is_greater_v1(value1, value2):
    if value1 > value2:
        return True
    else:
        return False

def is_greater_v2(value1, value2):
    if value1 > value2:
        return True
    return False

def my_sqrt(value):
    if value > 0:
        result = value ** 0.5
        print("Square root of {} is {}".format(value, result))
        return
    print("value must be > 0")

def adder(x):
    def inside_adder(y):
        return x + y
    return inside_adder

print(my_max(1, 17, 5, 2, 50, -75, 1))

print()
print(is_greater_v1(10, 5))
print(is_greater_v1(10, 11))

print()
print(is_greater_v2(10, 5))
print(is_greater_v2(10, 11))

print()
my_sqrt(2)
my_sqrt(-2)

add = adder(5)
print(add(3))
print(add(5))
