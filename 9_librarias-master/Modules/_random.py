"""
random
"""

import random

start = 0
end = 100
seed = 123

rnd = random.Random(seed) # random object with seed
print(rnd.random())
print(random.random())

print(random.randint(start, end))
print(random.randrange(end))
print(random.randrange(start+2, end))
print(random.randrange(start+2, end, step=2))

students = [
    ["student 1", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
    ["student 2", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
    ["student 3", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
    ["student 4", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)]
]

print(students)
random.shuffle(students)
print(students)
