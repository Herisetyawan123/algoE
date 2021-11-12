import os


def clear():
    os.system('cls')

clear()

# open()
# menambahkan baris
def appendFile():
    file = open('data.txt', 'a')
    file.write('\nassalamualaikum')
    file.close()

# menulis isi file
def writeFile():
    file = open('data.txt', 'w')
    file.writelines(['halo dunia\n', 'selamat pagi'])
    file.close()

# membaca file
def readFile():
    file = open('data.txt', 'r')
    hasil = file.readlines()
    file.close()

# print(hasil)

# with open()

# with open('data.txt', 'r') as file:
#     hasil = file.readlines()

# with open('data.txt', 'w') as file:
#     file.writelines(['string\n', 'strings\n'])

# with open('data.txt', 'a') as file:
#     file.writelines(['string\n', 'strings\n'])

def update(hasil):
    hasil_baru = []
    for nomer, row in enumerate(hasil, 1):
        if nomer == 3:
            baru = input('Masukan nama baru: ')
            hasil_baru.append(baru+'\n')
        else:
            hasil_baru.append(row)

    print(hasil_baru)
    # print(hasil_baru)
    with open('data.txt', 'w') as file:
        file.writelines(hasil_baru)



