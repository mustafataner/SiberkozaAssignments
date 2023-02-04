# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

userJSON_mt = '{"first_name": "mustafa","last_name":"taner", "age": 25}'

user = json.loads(userJSON_mt)

print(user)

print(user["first_name"])

car_mt = {"make": "ford", "model": "mustang", "year": 1970}

carJSON = json.dumps(car_mt)

print(carJSON)
