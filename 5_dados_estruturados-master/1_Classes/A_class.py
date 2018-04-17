"""
Point
"""

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    
    p1 = Point(2, 3)
    p2 = Point(10, 20)

    print("Point 1: {}x{}".format(p1.x, p1.y))
    print("Point 2: {}x{}".format(p2.x, p2.y))
