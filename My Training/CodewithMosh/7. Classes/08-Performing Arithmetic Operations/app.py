class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): # if we not define this function when we call print(point + other) it will return reference object (__main__.Point object at 0x----)
        return f"({self.x},{self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        # return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


point = Point(10, 20)
other = Point(1, 2)
print(point + other)
# combined = point + other
# sub = point - other
# print(combined.__dict__)
# print(sub.__dict__)
# print("=" * 10)
# print(combined.x)
# print(sub.x)
