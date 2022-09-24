# Data Classes
# if we have class that is only have a data we can use method "namedtuple" on collections module
# for ex if we want to compare object we dont need to call magic method __eq__
# note: this namedtuple is immutable we cant edit/modify when its created
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

print(p1==p2)
print(p1.x)
print(p2.y)