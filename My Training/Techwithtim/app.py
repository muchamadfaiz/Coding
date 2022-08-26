class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("i dont know what to say")

    def show(self):
        print(" nama saya {}, umur saya {}".format(self.name, self.age))


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("meow")

    def show(self):
        print(" nama saya {}, umur saya {}, warna saya {}".format(
            self.name, self.age, self.color))


class Dog(Pet):
    def speak(self):
        print("bark")


class Fish(Pet):
    def speak(self):
        print("lalalal")


c1 = Cat("pawpaw", 20, "orange")
# print(c1.name)
# print(c1.age)
c1.show()

c2 = Cat("bilbil", 18, "brown")
# print(c2.name)
# print(c2.age)
c2.show()

d = Dog("Fury", 19)
# print(d.name)
# print(d.age)
d.show()

f = Fish("asasi", 10)
# print(f.name)
# print(f.age)
# f.speak()
f.show()
