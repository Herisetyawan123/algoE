import json

FILEKU = "data.json"

def readJson(namafile):
    with open(namafile, 'r') as ouput:
        hasil = json.load(ouput)
    return hasil



def writeJson(data_baru):
    with open(FILEKU, 'w') as ouput:
        json.dump(data_baru, ouput, indent=4)


# data_baru = [{"nama" : "joko", "age" : 19}]

# with open(FILEKU, 'a') as output:
#     json.dump(data_baru, output, indent=4)

def tambahJson(data_baru):
    data = readJson(FILEKU)
    data.append(data_baru)
    writeJson(data)


# print(data)
# print(data_baru)