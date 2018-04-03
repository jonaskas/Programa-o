"""
Module example
"""

some_value = 10

def my_sum(value1, value2):
    return value1 + value2

def daddy():
    return "Running from: " + __name__

if __name__ == "__main__":
    print(daddy())
    print(my_sum(some_value, some_value))
