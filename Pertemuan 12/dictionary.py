import json
# data = {
#     "user123" : {
#         "username": "admin",
#         "password": "admin"
#     },
#     "user124" : {
#         "username": "admin",
#         "password": "admin"
#     }
# }


PATH_DATA = "data/user.json"

def readJson():
    try:
        with open(PATH_DATA, 'r') as output:
            data = json.load(output)
        return data
    except FileNotFoundError:
        data_kosong = {}
        with open(PATH_DATA, 'w') as output:
            json.dump(data_kosong, output, indent=4)
        return data_kosong
        
data = readJson()
print(data)
data["user123"] = {
        'username': "admin",
        'password': "admin"
    }

print("data yg telah ditambah")
print(data)
with open("data/user.json", 'w') as output:
    json.dump(data, output, indent=4)

# try:
#     print(data["user123"]['password'] == "admin")
# except KeyError:
#     print("id tidak ada")

# print(data)