"""
chr
See: https://www.asciitable.com/
"""

chrs = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 71, 114, 101, 97, 116, 33]

chr(65)

chr(chrs[0])

print()
for c in chrs:
    print(chr(c), end="")    

print()
print("".join(chr(x) for x in chrs))
