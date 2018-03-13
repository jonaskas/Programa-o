"""
bool
"""

falsey1 = False
truthy1 = True
print(falsey1, truthy1)

falsey1 = bool(0)
falsey2 = bool(0.0)
falsey3 = bool("")
falsey4 = bool([])
print(falsey1, falsey2, falsey3, falsey4)

truthy1 = bool(1)
truthy2 = bool(0.1)
truthy3 = bool("a")
truthy4 = bool([1, 2])
truthy5 = bool("False")
truthy6 = bool(float("nan"))
print(truthy1, truthy2, truthy3, truthy4, truthy5, truthy6)
