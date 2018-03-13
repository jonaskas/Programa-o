"""
Logical
"""

a = 10
b = 11
c = a

print("a < b = {}".format(a < b))
print("a > b = {}".format(a > b))
print("a <= b = {}".format(a <= b))
print("a >= c = {}".format(a <= c))

print()
print("a == c = {}".format(a == c))
print("not(a != c) = {}".format(not(a != c)))

print()
print("a != c = {}".format((a != c)))
print("not(a == c) = {}".format(not(a == c)))

print()
print("(a < b) and (c > b) = {}".format((a < b) and (c > b)))
# 1 1 1
# 1 0 0
# 0 1 0
# 0 0 0

print()
print("(a < b) or (c > b) = {}".format((a < b) or (c > b)))
# 1 1 1
# 1 0 1
# 0 1 1
# 0 0 0

print()
a = [1, 2, 3]
b = a        
print(b is a) # is checks if variables refer to the same object
print(b == a) # == checks if the objects pointed to have the same values
b = [1, 2, 3] 
print(b is a)
print(b == a)
