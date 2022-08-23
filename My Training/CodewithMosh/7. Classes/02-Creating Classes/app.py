class Point: # use Pascal naming convention (First letter uppercase, no underscore to separate multiple word)
    def draw(self):
        print("draw") # all functions in our classes should have at least one parameter, and by convention we call that parameter "self"

point = Point()
print(type(point))
print(isinstance(point, Point))
