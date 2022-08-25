class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        # return True

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


point = Point(5, 2)
other = Point(5, 2)
print("gt hasilnya: {}".format(point > other))  # membandingkan objek
print("eq hasilnya: {}".format(point == other))  # membandingkan objek
print("lt hasilnya: {}".format(point < other))  # membandingkan objek
