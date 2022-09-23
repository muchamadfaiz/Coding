class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    @classmethod # decorator for extend the behaviour of a method or function
    def zero(cls): #whenever we define a class method we call its first parameter "cls"
        return cls(0, 0) # exactly the same as calling Point(0,0)

    def draw(self): 
        print(f"Point ({self.x}, {self.y})") 

point = Point.zero() # different from point = Point(1,2)
point.draw()

