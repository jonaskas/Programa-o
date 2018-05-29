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

# list are mutable

my_list = [10, 11, 15, 16]
print_memory(my_list)

print()
print(type(my_list[0])) # int are imutables

print()
for i in my_list:
    print_memory(i) 

my_list[0] = 123

print()
for i in my_list:
    print_memory(i)

print()
print_memory(my_list)
