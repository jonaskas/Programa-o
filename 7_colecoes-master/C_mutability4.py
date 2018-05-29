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
print()
my_list = []
print_memory(my_list)
my_list += [11, 22]
print_memory(my_list)

my_list.append(33)
print_memory(my_list)

my_list.remove(11)
print_memory(my_list)

print()
list1 = [1, 2, 3] 
list2 = [1, 2, 3] 
list3 = list1
print(list1 == list2)
print(list1 is list2)
print(list1 is list3)
