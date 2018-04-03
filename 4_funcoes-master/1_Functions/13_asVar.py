"""
Function variable
"""

def One():
    print("First function")

def Two():
    print("Second function")

a = 2

option = One if a == 1 else Two
option()