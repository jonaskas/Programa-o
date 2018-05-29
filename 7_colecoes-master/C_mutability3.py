"""
Mutability
- Python is strongly object-oriented in the sense that everything
    is an object including numbers, strings and functions
- Immutable objects: int, float, decimal, complex, bool, string,
    tuple, range, frozenset, bytes
- Mutable objects: list, dict, set, bytearray,user-defined classes
"""

def print_memory(obj):
    print(hex(id(obj)), ":", obj)

# tuples are immutable
tuple_ = (1, 2, 3)
print_memory(tuple_)

tuple_ += (4, 5, 6)
print_memory(tuple_)
