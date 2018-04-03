"""
min
"""

values = [10, 11, 15, 36]
print(min(values))

values = ["a", "ab", "AB", "_1", "0", "-1", "-"]
print(min(values))

print()
for i in values:
    print(i, ord(i[0]))
