"""
Chip class
"""

class Chip:

    def __init__(self, chipNumber=None):
        
        self.chip = chipNumber
       
        if chipNumber != None and len(chipNumber) == 11:  
            self.valid = True
        else:    
            self.valid = False

    def __str__(self):
        return "Chip: {}\nValid: {}".format(self.chip, self.valid)

if __name__ == "__main__":
    chip1 = Chip("123-1234-12")
    print(chip1)

    chip2 = Chip("123-123-12")
    print(chip2)
    
    chip3 = Chip()
    print(chip3)
    