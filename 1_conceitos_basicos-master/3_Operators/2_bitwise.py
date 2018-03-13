"""
Bitwise
"""

a = 2 # "0010"
print("a = {0} - {0:04b}".format(a))

# left shift
print("a << 1 = {0} {0:04b}".format(a << 1)) #0100
print("a << 2 = {0} {0:04b}".format(a << 2)) #1000

# right shift
print("a >> 1 = {0} {0:04b}".format(a >> 1)) #0001
print("a >> 2 = {0} {0:04b}".format(a >> 2)) #0000

# and
print("5 & 3 = {0} {0:04b}".format(5 & 3)) # 0001
#   0101
#   0011
# = 0001

# or
print("5 | 3 = {0} {0:04b}".format(5 | 3)) # 0111
#   0101
#   0011
# = 0111

# xor
print("5 ^ 3 = {0} {0:04b}".format(5 ^ 3)) # 0110
#   0101
#   0011
# = 0110

# ~ invert same as: -(x+1)
print("~5 = {0} {1}".format(~5, bin(~5)))
# 0 0101 = 5
# 0 0110 = 5 + 1
# 1 0110 = - (5 + 1)
