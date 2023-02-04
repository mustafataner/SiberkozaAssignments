# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it.
# Almost everything in Python is an object


class user_mt:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age


    def greeting(self):
        return "my name is {} and I am {}".format(self.name,self.age)

taner = user_mt("mustafa", "mustafa@taner.com", 25)

print(taner.name)
print(taner.age)
print(taner.email)

print(taner.greeting())




