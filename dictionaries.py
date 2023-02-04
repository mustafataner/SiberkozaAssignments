# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


person_mt = {
    "first_name": "mustafa",
    "last_name": "taner",
    "age": 25

}

# get value

print(person_mt.get("first_name"))

# add key/value


person_mt["phone"] = "541 123 45 67"

print(person_mt)

# get dict keys

print(person_mt.keys())

# get dict value

print(person_mt.values())

# get dict items

print(person_mt.items())

# remove item

del ( person_mt["age"])
person_mt.pop("phone")
print(person_mt)

