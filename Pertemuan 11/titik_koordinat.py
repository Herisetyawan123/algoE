import math
buah = [
    [0,2],
    [3,2], 
    [5,4],
    [3,4],
    [6,7],
    [3,9],
    [0,1],
    [0,7],
    [1,9],
    [0,3]
]

temp = []

batas = math.inf

jarak_terkecil = 0


# ab**2 = (x2 - x1)**2 - (y2 - y1)**2
jumlah = len(buah)
for i in range(jumlah):
    for j in range(i+1, jumlah):
    #     print(i ,j)
    # print()
        x = buah[j][0] - buah[i][0]
        y = buah[j][1] - buah[j][1]
        hasil = math.sqrt(x**2 + y**2)
        print(hasil)
        if hasil < batas:
            temp = [buah[i], buah[j]]
            batas = hasil
            jarak_terkecil = hasil
        print()

# print(temp[0],"dan",temp[1],)
print(temp)
print(jarak_terkecil)