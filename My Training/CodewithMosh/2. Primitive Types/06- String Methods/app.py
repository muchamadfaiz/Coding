# String Methods (function availabe on string)
# Everything in Python is an objects and object have function we call method
# and can accesed using the dot notation(.)

# self.upper()-> upper the string
course = "     Python programming    "
course_capital = print(course.upper())

# self.lower()-> lower the string
course_lower = print(course.lower())

# self.title()-> capitalize the string
course_title = print(course.title())

# self.strip()-> Capitalize the string
course_strip = print(course.strip())

# self.find()-> find any string
course_find = print(course.find("pro"))

# self.replace()-> replace any string
course_replace = print(course.replace("p", "j"))

# in operator -> checking the existence of a character on string (Boolean)
print("pro" in course)

# not in operator -> checking the existence of a character on string (Boolean)
print("swift" not in course)

