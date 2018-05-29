"""
statistics
"""

import statistics

grades = {
    "student1": [10, 11, 12],
    "student2": [15, 14, 14],
    "student3": [10, 10, 12],
    "student4": [14, 14, 10]
}

for i in range(3):
    x = list(g[i] for s, g in grades.items())

    value = statistics.mean(x)
    print("Mean:", value)

    value = statistics.median(x)
    print("Median:", value)

    value = statistics.variance(x)
    print("Variance:", value)

#print(dir(statistics))
