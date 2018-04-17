"""
Animal Class 
"""

from A_Owner import Owner
from B_Chip import Chip

class Animal():
    """Animal Class"""

    # initializer
    def __init__(self, name, owner, chip, age=0):
        self.name = name
        self.owner = owner
        self.chip = chip
        self.age = age
        self.walked = 0

    def speak(self):
        print("UF, UF!!!!")

    def walk(self, steps):
        self.walked += steps
       
    def get_walked(self):
        print(self.name, "walked", self.walked, "steps")

    def __str__(self):
        return "My name is {} and I walked {} steps. My owner is {} and my chip number is {}".format(self.name, self.walked, self.owner.name, self.chip.chip)

if __name__ == "__main__":
    
    owner = Owner("Jack")
    chip = Chip("999-8888-77")

    a1 = Animal("Rufus", owner, chip, 1)
    
    a1.speak()
    a1.speak()

    a1.walk(10)
    a1.walk(20)
    a1.walk(30)

    a1.get_walked()

    print(a1)
