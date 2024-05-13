import json

data = {
    "users": [
        {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian",
            "age": 23,
            "gender": "Male",
            "birthdate": "1999-02-01",
            "email": "Zaphod@gmail.com",
            "phone": "+1 987654321",
            "password": "12345678",
        },
    ]
}

def reading():
    with open("data_file.json") as data_file:
        old_data = json.load(data_file)
        print(old_data)

def writing():
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)
        # old_data = json.load(write_file)

def appending():
    with open("data_file.json", "a") as write_file:
        json.dump(data, write_file)
        write_file.close()
        print(data)

        with open("data_file.json", "a") as write_file:
            json.dump(data, write_file)



#
#
# data = old_data + data
#
#
# with open("data_file.json", 'w') as outfile:
#     json.dump(data, outfile)
