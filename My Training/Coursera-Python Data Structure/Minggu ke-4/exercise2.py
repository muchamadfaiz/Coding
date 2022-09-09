fname = "mbox-short.txt"
file = open(fname)
count = 0
# listjumlah = []
for line in file:
    line = line.strip()
    # print("line", line)
    line1 = line.split()
    # print("line1", line1)
    # print(line1)
    if len(line1) < 1:
        continue
    if line1[0] == "From" : 
        count += 1
        # listjumlah.append(line1)
        print(line1[1])
    else:
        continue

print("There were {} lines in the file with From as the first word".format(count))