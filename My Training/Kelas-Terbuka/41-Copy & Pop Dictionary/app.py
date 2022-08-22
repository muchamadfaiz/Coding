# copy dictionary

teman_teman = {
    "fz" : "faiz_ganteng",
    "paw" : "pawpaw",
    "bil": "bilbil",
    "bul" : "bulbul",
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["fz"]="muchamad faiz"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary (berdasarkan key)

dataFaiz = friends.pop("fz")
print(f"data faiz = {dataFaiz}\n")
print(f"friends = {friends}\n")

# pop item dictionary (berdasarkan data terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")



