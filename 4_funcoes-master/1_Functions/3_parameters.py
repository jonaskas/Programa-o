"""
Parameters
"""

MAX = 4

def print_line(character):
    print(character * 30)

print_line("-")
print_line("*")
print_line("/")
print_line("\\")

for _ in range(MAX):
    print_line("o")
