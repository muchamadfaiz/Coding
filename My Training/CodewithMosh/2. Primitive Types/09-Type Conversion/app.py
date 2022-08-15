x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# Falsey Value
"""
1. " " (Empty Space)
2. 0 (Zero)
3. None
"""
y1 = bool("")
y2 = bool(0)
y3 = bool(None)
y4 = bool(-1)
y5 = bool(2)
y6 = bool("False")

print(y1)
print(y2)
print(y3)
print(y4)
print(y5)
print(y6)