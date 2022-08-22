# Looping Dictionary

teman_teman = {
    "fz" : "faiz_ganteng",
    "paw" : "pawpaw",
    "bil": "bilbil",
    "bul" : "bulbul",
}

# # looping first try (yang keluar adalah key nya)

# for teman in teman_teman: # kita gatau ini list atau apa?
#     print(teman)

# # maka dari itu tambahin
# # Operator untuk menbambil item/iterables


# keys = teman_teman.keys() # untuk ngecek iterables yg ada di key
# print(keys)

# print("\n")
# for key in teman_teman:
#     print(teman_teman.get(key))

# for key in teman_teman.keys():
#     print(teman_teman.get(key))

# values = teman_teman.values() # untuk ngecek iterables yg ada di values
# print(values)

# for value in teman_teman.values():
#     print(value)

# items = teman_teman.items()
# print(items)
# print("\n")

# for item in teman_teman.items():
#     print(item)

for key, value in teman_teman.items():
    print(f"key = {key} values = {value}")
