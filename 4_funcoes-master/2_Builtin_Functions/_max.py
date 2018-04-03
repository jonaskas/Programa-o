"""
max
"""

values = [10, 11, 15, 36]
print(max(values))

values = ["a", "ab", "AB", "_1", "0", "-1", "-"]
print(max(values))

print()
for i in values:
    print(i, ord(i[0]))
    