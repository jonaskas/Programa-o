"""
Inner functions
"""

def outer():

    value1 = "Outer1"
    value2 = "Outer2"

    def inner():
        value1 = "Inner 1"
        nonlocal value2
        value2 = "inner 2"
        print("value1:", value1)
        print("value2:", value2)

    print("value1:", value1)
    print("value2:", value2)

    inner()
    
    print("value1:", value1)
    print("value2:", value2)

outer()
