class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self): # self is a reference to a current point object
        print(f"Point ({self.x}, {self.y})") 

point = Point(1,2)
point.draw()
