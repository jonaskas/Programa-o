"""
Sets
- Allow operations based on set theory.
"""

set1 = {'a', 'b', 'c', 'a', 'd', 'e', 'f'}
set2 = set("aaaabcd")

print()

print("intersection:", set1 & set2) # same as print(set1.intersection(set2))
print("union:", set1 | set2) # same as print(set1.union(set2))
print("diference: ", set1 - set2) # same as print(set1.difference(set2))
print("symmetric_difference:", set1.symmetric_difference( set("xzabc") )) # not in both

print()
print("issuperset:", set1.issuperset(set2))
print("issubset:", set1.issubset(set2))
print("isdisjoint:", set2.isdisjoint(set("xz")))

print()
for item in set1 - set2:
    set2.add(item)
print(set2)
