fname = "mbox-short.txt"
fhandle = open(fname)

counts = {}
for line in fhandle:
    word = line.split()
    if len(word) < 3 :
        continue
    if  word[0] != "From" :
         continue
    full_jam = word[5]
    jam = full_jam.split(":")
    jam = str(jam[:1])
    jam = jam[2:4]
    if jam in counts :
        counts[jam] = 1 + counts[jam]
    else :
        counts.update({jam:1})
lst = list()
for k, v in counts.items():
    new_tup = (k, v)
    lst.append(new_tup)
 
lst = sorted(lst)    
for k, v in lst:
    print(k,v)
