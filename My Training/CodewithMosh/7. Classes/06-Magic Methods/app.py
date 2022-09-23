class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # convert an object class to a string class
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)
