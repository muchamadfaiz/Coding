# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
jumlah = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    angka = float(line[line.find(".") - 1 : ])
    jumlah += angka
    
print("Average spam confidence:", jumlah/count)