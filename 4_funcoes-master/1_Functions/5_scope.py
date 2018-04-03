"""
Scope
"""

value = "Global Scope"

def write_v1():
    value = "Inner Scope"
    print("in v1:", value)

def write_v2(value): # 1) by Value, 2) Overloading is not allowed
    print("in v2 before:", value)
    value = "Inner Scope"
    print("in v2 after:", value)

def write_v3():
    global value
    print("in v3 before:", value)
    value = "Inner Scope"
    print("in v3 after:", value)

print("main:", value)
print("-" * 30)

print("Call to v1")
write_v1()
print("main:", value)
print("-" * 30)

print("Call to v2")
write_v2(value)
print("main:", value)
print("-" * 30)

print("Call to v3")
write_v3()
print("main:", value)
print("-" * 30)