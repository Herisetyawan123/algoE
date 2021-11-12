import json, os, time

PATH_DATA = "data/user.json"

def clean():
    os.system('cls')

def readJson():
    try:
        with open(PATH_DATA, 'r') as output:
            data = json.load(output)
        return data
    except FileNotFoundError:
        data_kosong = []
        with open(PATH_DATA, 'w') as output:
            json.dump(data_kosong, output, indent=4)
        return data_kosong
        
def writeJson(data):
    with open(PATH_DATA, 'w') as output:
        json.dump(data, output, indent=4)

def login():
    clean()
    username = input("username : ")
    password = input("password : ")
    user = readJson()

    status_login = False
    if len(user) != 0:
        for row in user:
            if row["username"] == username and row["password"] == password:
                status_login = True
    else:
        print("silahkan daftar dulu karena database masih belum ada akun")
        time.sleep(3)
        main()
    
    if status_login:
        clean()
        print("yeayyyy berhasil login")
    else:
        print("login gagal")
        time.sleep(2)
        main()

def daftar():
    clean()
    username = input("username baru : ")
    password = input("password baru : ")
    user = readJson()
    data_baru = {
        "username" : username,
        "password" : password
    }
    user.append(data_baru)
    # tulis
    writeJson(user)
    print("berhasil ditambah")
    main()


def main():
    clean()
    print('''
    1. login
    2. daftar''')
    choice = input("pilih [1/2]: ")
    if choice == '1':
        login()
    elif choice == '2':
        daftar()

if __name__ == "__main__":
    main()