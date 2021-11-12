# import itertools


n = int(input())
# data = []

# for p in itertools.product([6, 9], repeat=n):
#     sui = ''.join([str(x) for x in p])
#     if'666' not in sui and '999' not in sui:
#         data.append(sui)

# print(data)
# print(len(data))


nilai_awal, nilai_kedua = 0, 2

for i in range(n):
    jumlah = nilai_awal + nilai_kedua
    nilai_awal, nilai_kedua = nilai_kedua, jumlah

print(nilai_kedua)