fname = "mbox-short.txt"
fhandle = open(fname)
counts = {}
for line in fhandle:
    x = line.strip().split()
    if len(x) < 1:
        continue
    if x[0] == "From":
        counts[x[1]] = counts.get(x[1],0) + 1
    else:
        continue

# print(counts)
max_value = 0
max_key = None
for key, value in counts.items():
    if value > max_value:
        max_value = value
        max_key = key
print(max_key,max_value)

# bigcount = None
# bigword = None

# for x[1],count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = x[1]
#         bigcount = count

# print(bigword, bigcount)


# d = dict(Xena=3, Mark=5, Eve=2)
# max_value = 0
# max_key = None
# for key, value in d.items():
#     if value > max_value:
#         max_value = value
#         max_key = key
# print(max_key, max_value)