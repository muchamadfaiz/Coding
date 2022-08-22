# Operator dictionary

data_dict = {
   "fz" : "muchamad faiz",
   "paw" : "pawpaw",
   "bil" : "bilbil",
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "paw"
CHECKKEY = KEY in data_dict
print(f"apakah ada {KEY} di data_dict:{CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["fz"])
# print(data_dict["paw"]) ini akan eror
print(data_dict.get("fz")) # baiknya untuk membedakan cara akses list dengan dict menggunakan get. (hasil sama)
print(data_dict.get("kis")) # tidak eror melainkan mengembalikan ke value none
print(data_dict.get("kis", "key tidak ditemukan")) # None bisa diganti string/message

# mengupdate data
data_dict["fz"] = "faiz si ganteng"
print(data_dict)
data_dict["bul"] = "bul-bul"
print(data_dict)

data_dict.update({"fz":"muchamad faiz"})
print(data_dict)
data_dict.update({"nkl":"si nackal"})
print(data_dict)

# mendelete data
del data_dict["bul"]
print(data_dict)