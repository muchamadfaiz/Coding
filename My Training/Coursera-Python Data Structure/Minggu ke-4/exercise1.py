# fname = input("Enter file name: ")
# fh = open(fname)
# y = list()
# for line in fh:
#     line = line.rstrip()
#     splits = line.split()
#     y.append(splits)
# newlist = y[0]+y[1]+y[2]+y[3]
# print(newlist)

fname = "romeo.txt"
fh = open(fname)
list1 = []
list2 = []
for line in fh:
    line = line.strip().split()
    list1 += line
    for i in list1:
        if i not in list2:
            list2.append(i)
# print(list2)
list2.sort()
print(list2)

# list0 = ["pawpaw", "bilbil", "nackal"]
# list0.sort()
# print(list0)

# # vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']

# # sort the vowels
# vowels.sort()

# # print vowels
# print('Sorted list:', vowels)
