barang = "Tas"
harga = 2000
judul = "Titanic"
harga2 = 200.98

'''
d = integer
s = string
f = float

^ = center
> = rata kanan
< = rata kiri
'''


print("-"+" "*9+judul+" "*9+"-")
print("-{:25s}-".format(judul))
print("harga barang {1} dengan nama {0}".format(barang, harga))
print("harga barang {1:^25d} dengan nama {0}".format(barang, harga))
print("harga barang {:0.2f}".format(harga2))