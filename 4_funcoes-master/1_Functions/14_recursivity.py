"""
Recursivity
"""

"""
5! = 5 * 4!
        4! = 4 * 3!
                 3! = 3 * 2!
                          2! = 2 * 1!
                                   1! = 1 
                          2! = 2 * 1
                 3! = 3 * 2
        4! = 4 * 6
5! = 4 * 24
                    
"""

def fact(n):
    
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))

print(fact(6))
