class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x # instance attribute = these are attributes that belong to point instances
        self.y = y # instance attribute = these are attributes that belong to point instances

    def draw(self): # self is a reference to a current point object
        print(f"Point ({self.x}, {self.y})") 

Point.default_color = "yellow"
point = Point(1,2)
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3,4)
print(another.default_color)
another.draw()