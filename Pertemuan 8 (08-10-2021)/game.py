import random

jumlah = int(input("Mau berapa kali ?"))
no = 1
koin = ["T", "F"]
while no <= jumlah:
    tanya = input("Masukan [T/F]")
    hasil = random.choice(koin)
    print(hasil)
    if hasil == tanya:
        print("bener")
    else:
        print("salah")
    no += 1