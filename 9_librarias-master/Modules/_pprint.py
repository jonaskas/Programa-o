"""
pprint (Pretty Print)
"""

import pprint

grades = {
    "student1" : [10, 11, 12],
    "student2" : [15, 14, 14],
    "student3" : [10, 10, 12],
    "student4" : [14, 14, 10]
}

print(grades)
print()
pprint.pprint(grades)
