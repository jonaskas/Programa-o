"""
Example
"""

from random import randint

from A_Owner import Owner
from B_Chip import Chip
from C_Animal import Animal

RACE_LENGTH = 100
RUN_STEPS_MAX = 10

def GenerateChip():
    return "{}-{}-{}".format(randint(100, 999), randint(1000, 9999), randint(10, 99))

def Winner(dog):
    if (dog.walked >= RACE_LENGTH):
        return True
    return False

def Run(dog):
    dog.walked += randint(0, RUN_STEPS_MAX)
    dog.get_walked()

owner1 = Owner("Jack")
owner2 = Owner("John")

dog1 = Animal("Bobby", owner1, Chip(GenerateChip()), 0)
dog2 = Animal("Rufus", owner1, Chip(GenerateChip()), 0)
dog3 = Animal("Lady", owner2, Chip(GenerateChip()), 3)
dog4 = Animal("Black", owner2, Chip(GenerateChip()), 1)

print("-" * 30)
print("Racers")
print("-" * 30)

print(dog1)
print(dog2)
print(dog3)
print(dog4)

print("-" * 30)
print("Race")
print("-" * 30)

winner = None
while winner is None:
        
    Run(dog1)
    if Winner(dog1):
        winner = dog1

    Run(dog2)
    if winner is None and Winner(dog2):
        winner = dog2

    Run(dog3)
    if winner is None and Winner(dog3):
        winner = dog3
    
    Run(dog4)
    if winner is None and Winner(dog4):
        winner = dog4

print("-" * 30)
print("Winner")
print("-" * 30)
print(winner)
print("-" * 30)
print("-" * 30)