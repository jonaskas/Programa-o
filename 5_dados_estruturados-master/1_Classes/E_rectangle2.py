"""
Example
"""

from C_point import Point

class Rectangle():

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
         
    def get_size(self):
        """
        returns the rectangle size as the distance from origin  
        """
        return Point(abs(self.point2.x - self.point1.x), abs(self.point2.y - self.point1.y) )

    def __str__(self):
        return "Rectangle corners:\n{}\n{}".format(self.point1, self.point2)

if __name__ == "__main__":
    
    p1 = Point(2, 3, "red")
    p2 = Point(10, 20)

    rectangle = Rectangle(p2, p1)
    
    print(rectangle)

    print(rectangle.get_size())
