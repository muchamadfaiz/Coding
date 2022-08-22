# list -> array, mengakses dengan menggunakan index
# di list kita mengakses data menggunakan index nya
data_list = ["ucup", "otong", "dudung"]

print(data_list[0])

#dictionary (dict) --> associative array 
# kita mengakses data dengan identifier --> identitasnya key
# data_dict = {
#     "key1":"value1",
#     "key2":"value2"
# }

data_dict = {
    "cp":"ucup",
    "tg":"otong",
    "dg": "dudung",
    "nmber": 100,
    "list": data_list,
}

print(data_dict["cp"]) # cara akses menggunakan identifier bukan index
print(data_dict["list"])