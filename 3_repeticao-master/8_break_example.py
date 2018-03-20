"""
break
"""
import random

MIN = 0
MAX = 10
MAX_ATTEMPTS = 5

NUMBER = random.randint(MIN, MAX)

for attempt in range(MAX_ATTEMPTS):
    print("Attempt {}".format(attempt + 1))
    value = int(input("input a value between {} and {}: ".format(MIN, MAX)))
    if value == NUMBER:
        print("WINNER!!!!")
        break
    elif value > NUMBER:
        print("your number is greater")
    else:
        print("your number is lower")
