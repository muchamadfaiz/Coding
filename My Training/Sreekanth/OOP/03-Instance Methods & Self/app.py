# Function = callable attribute
# 1. Interoduction
class MyClass:
    # a,b dan fungsi say_hello adalah atribut class
    a = 10  # is an integer object

    def say_hello(self):  # is a function object
        print("Hello World")

    def set_name(self,name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")

#     b = "some string"  # is a string object


# print(MyClass.__dict__)
# # 2. Comparing class to module
# print("=" * 8, "comparing class", "=" * 8)
# # say_hello() # tidak bisa dilakukan karena semua atribut di dalam
# # class tidak bisa di panggil langsung diluar class
# MyClass.say_hello  # sama seperti saat panggil module
# # --> import socket
# # --> socket.ghostname()

# # 3. Bound method and self
# # membuat objek/instance baru dari class MyClass
# obj = MyClass()
# print(obj.a)  # kita bisa mengakses atribut class (a = 10) melalui objek
# print(obj.b)  # kita bisa mengakses atribut class (b = "some string") melalui objek
# obj.say_hello()     # ini akan muncul Exception Type Error = takes 0 positional arguments but 1 was given
#                     # padahal kita ga naro argumen apa2
#                     # ketika kita memanggil fungsi menggunakan parenthesis ()
#                     # objek baru dibuat di memori, objek ini yg disebut "instance of the class"
#                     # lalu python secara otomatis menyampaikan(pass) referensi ke instance yg sama
#                     # sebagai argumen pertama dari fungsi tersebut
#                     # to capture this automatically passed we specify a parameter usually called "self"
#                     # lalu python secara otomatis menyampaikan referensi ke instance yg sama
#                     # klo di bagian fungsi class sudah ditambahkan argumen "self" proram sudah ok

# # 4. Function Type vs Method type
# print(MyClass.say_hello) #class function
# print(obj.say_hello) #class method
# print(hex(id(obj)))
# MyClass.say_hello(obj)

# 5. Purpose of self

obj2 = MyClass()
obj2.set_name("pawpaw")
obj2.greet()