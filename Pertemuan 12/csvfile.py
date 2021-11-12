import csv

hasil = []
def readCsv():
    with open('data.csv', 'r') as filecsv:
        read = csv.reader(filecsv, delimiter=';')
        for baris in read:
            hasil.append(baris)

def writeCsv():
    with open('data.csv', 'w', newline='') as filecsv:
        write = csv.writer(filecsv, delimiter=';')
        # write.writerow(['titan', '170','alogE'])
        write.writerows([['titan', '170','alogE'], ['abner', '170', 'algoF']])

def appendCsv():
    with open('data.csv', 'a', newline='') as filecsv:
        wirte = csv.writer(filecsv, delimiter=';')
        wirte.writerow(['salsa', '155', 'algoA'])
