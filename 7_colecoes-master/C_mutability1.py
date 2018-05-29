"""
Mutability
- Python is strongly object-oriented in the sense that everything
    is an object including numbers, strings and functions
- Immutable objects: int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes
- Mutable objects: list, dict, set, bytearray,user-defined classes
"""

def print_memory(obj):
    print(hex(id(obj)), ":", obj)

a = 5

print_memory(print_memory)
print_memory(a)
