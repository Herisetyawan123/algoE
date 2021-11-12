import json
PATH_DATA = "data/data.json"


try:
    with open(PATH_DATA, 'r') as output:
        data = json.load(output)
except FileNotFoundError:
    data_kosong = []
    with open(PATH_DATA, 'w') as output:
        json.dump(data_kosong, output, indent=4)