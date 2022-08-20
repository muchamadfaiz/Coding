# program list buku

list_buku = []
while True:
    print("masukan data buku")
    judul = input("masukan judul buku\t: ")
    penulis = input("masukan penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    # print("No.\t| Judul\t\t\t| Penulis")
    print("=" * 10, "DATA BUKU", "=" * 10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    if len(list_buku) == 3:
        print("akhir program")
        break
    
    print("=" * 10)
    is_lanjut = print(input("apakah dilanjutkan? (y/n)\n"))
    if is_lanjut == "n":
        break
# data_buku = [["judul buku", "penulis"][][]]