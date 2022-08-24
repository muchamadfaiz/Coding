"""
Tanpa OOP
"""
# programmer = "eka"
# def programer_makan():
#     print(f"{programmer} makan nasi")

# petani = "putra"
# def petani_makan():
#     print(f"{petani} makan nasi")

# dokter = "putri"
# def dokter_makan():
#     print(f"{dokter} makan nasi")

# programer_makan()
# petani_makan()
# dokter_makan()

"""
Mulai OOP
"""
class Manusia:
    nama = "None" # Properties

    def __init__(self,nama):
        self.nama = nama

    def makan (self): # Fungsi/Method 
        print(f"{self.nama} makan nasi")

# programmer = Manusia("eka")
# programmer.makan()

# dokter = Manusia("debay")
# dokter.makan()

# influencer = Manusia("umiw")
# influencer.makan()

# """
# INHERITANCE
# """
# class ManusiaMilenial(Manusia): # manusia milenial merupakan subclass dari Manusia(superclass)
#     email = "None"

#     def set_email(self, email): 
#         self.email = email

#     def info(self): 
#         print(f"nama:{self.nama}, email = {self.email}")

# programmer = ManusiaMilenial("eka")
# programmer.set_email("ekatest.com")
# programmer.makan()
# programmer.info()

# dokter = ManusiaMilenial("debay")
# dokter.set_email("dokter.com")
# dokter.makan()
# dokter.info()

# influencer = ManusiaMilenial("umiw")
# influencer.set_email("umiw.com")
# influencer.makan()
# influencer.info()


"""
ENCAPSULATION
"""
# class ManusiaMilenial(Manusia): # manusia milenial merupakan subclass dari Manusia(superclass)
#     email = "None"
#     __pasword = "None"

#     def set_email(self, email): 
#         self.email = email

#     def set_pass(self, password):
#         self.__password = password

#     def __samarkan_password(self):
#         return self.__password.replace("a", "*")

#     def info(self): 
#         print(f"nama:{self.nama}, email = {self.email}\npassword = {self.__samarkan_password()}")

# programmer = ManusiaMilenial("eka")
# programmer.set_email("ekatest.com")
# programmer.set_pass("rahasia")
# programmer.info()

"""
POLYMORPHISM
"""

class ManusiaMilenial(Manusia): 
    email = "None"
    __pasword = "None"

    def set_email(self, email): 
        self.email = email

    def set_pass(self, password):
        self.__password = password

    def __samarkan_password(self):
        return self.__password.replace("a", "*")

    def info(self): 
        print(f"nama:{self.nama}, email = {self.email}\npassword = {self.__samarkan_password()}")

class Programmer(ManusiaMilenial):
    def info(self): 
        print(f"nama:{self.nama}/ email = {self.email}")

class Influencer(ManusiaMilenial):
    def info(self): 
        print(f"nama:{self.nama}| email = {self.email}")

programmer = Programmer("eka")
programmer.set_email("ekatest.com")
programmer.set_pass("rahasia")
programmer.info()

Influencer = Influencer("pawpaw")
Influencer.set_email("pawpaw.com")
Influencer.set_pass("aafadffaf")
Influencer.info()