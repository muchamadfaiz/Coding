# Width and Multiline

# Data

data_nama = "faiz"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# String standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
# print("="*5,"Data String", "="*5)
print(f"{'='*5}Data String{'='*5}")
print(data_string)

# String multiline (dengan menggunakan enter, newline,\n)

data_string = f"nama = {data_nama}\numur = {data_umur}\ntinggi = {data_tinggi}\nsepatu = {data_nomor_sepatu}"
print(f"\n{'='*5}Data String{'='*5}")
print(data_string)

# String multiline (kutip triplets)

data_string = f"""
nama   = {data_nama:>5} #kalo kurang dari 5 akan rata kanan
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print(f"\n{'='*5}Data String{'='*5}")
print(data_string)