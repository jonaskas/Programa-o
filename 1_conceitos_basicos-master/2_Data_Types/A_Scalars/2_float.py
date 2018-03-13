"""
Float
"""

import sys

value = 2.123
print(value)

# Using constructors
print()
value = float(5)
print(value)
value = float("5")
print(value)

# Scientific notation
print()
value = 2e6
print(value)
value = 1.136e-25
print(value)
print("{0:.28f}".format(value))

# Max. Value
print()
print("{0}".format(sys.float_info.max)) # presents most readable 
print("{0:f}".format(sys.float_info.max)) # as a long float value

# Promotion to float
print()
value = (2 + 1) * 3 + 1 # value will be integer
print(value)
value = (2 + 1) * 3 + 1.0 # value will be float
print(value)
