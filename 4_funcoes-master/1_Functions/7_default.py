"""
Default values and named parameters
"""

def multiply(value, times=1):
    print(value * times)

def sum_and_multiply(value1, value2=0, times=1):
    val = value1 + value2
    multiply(times=times, value=val)

multiply("Python")
multiply("Python", 3)
multiply(3)
multiply(3, 3)

print()
sum_and_multiply(10, 2)
sum_and_multiply(10, 1, 2)
sum_and_multiply(10, times=2)
sum_and_multiply(times=2, value2=2, value1=3)
