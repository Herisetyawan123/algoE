import json
import csv


# write and read ( open() )
def writeAppendFile(name_file, content):
    file = open(name_file, 'a')
    file.write(content)
    file.close()

def writeFile(name_file, content):
    file = open(name_file, 'w')
    file.write(content)
    file.close()

def readFile(nama_file):
    file = open(nama_file, 'r')
    hasil = file.readlines()
    file.close()
    return hasil


# write and read ( with open() as ... )
def writeOpenFile(nama_file, content):
    with open(nama_file, 'w') as file:
        file.writelines(content+'\n')


def writeAppendOpenFile(nama_file, content):
    with open(nama_file, 'a') as file:
        file.writelines(content+'\n')

def readOpenFile(nama_file):
    with open(nama_file, 'r') as file:
        hasil =  file.readlines()
    return hasil



# json
def writeJsonFile(nama_file, content):
    with open(nama_file, 'w') as data:
        writer = json.dump(content, data, indent=4)

def readJsonFile(nama_file):
    with open(nama_file, 'r') as data:
        reader = json.load(data)
    return reader

def addJsonFile(nama_file, row):
    with open(nama_file, 'r') as output:
        reader = json.load(output)
    
    # append row baru
    reader.append(row)
    with open(nama_file, 'w') as output:
        writer = json.dump(reader, output, indent=4)



if __name__ == '__main__':
    content = [
        {
            'nama' : "ahmad",
            'age' : 12
        },
        {
            'nama' : "paijo",
            'age' : 18
        }
    ]
    row_baru = {
            'nama' : "supri",
            'age' : 45
        }
    # print(readJsonFile('data.json')[0]['nama'])
    addJsonFile('data.json', row_baru)
    # writeJsonFile('data.json', content)
