"""
Example
"""

class Point():

    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.Color = color
         
    def __str__(self):
        return "Point: {}x{} {}".format(self.x, self.y, self.Color if self.Color != None else "" )

if __name__ == "__main__":
    
    p1 = Point(2, 3, "red")
    p2 = Point(10, 20)

    print(p1)
    print(p2)
