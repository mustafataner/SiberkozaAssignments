# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


# String Formatting

# String Methods

name_mt = "mustafa"
age_mt = 25

# concatenate

print(" merhaba ben " + name_mt)

print(" Merhaba ben " + name_mt + " " + "yaşım:" + str(age_mt))

# argument by position

print("merhaba benim adım {} yaşım {}".format(name_mt, age_mt))

mt = "mustafa taner"

# capitalize string

print(mt.capitalize())

# make all uppercase

print(mt.upper())

# make all lower

print(mt.lower())

# swap case

print((mt.swapcase()))

# get length

print((len(mt)))

# replace

print(mt.replace("mustafa", "python"))

# count

a = "taner"

print(a.count("a"))

# starts with

print(mt.startswith("m"))

# end with

print(mt.endswith("r"))

# split into a list

print(mt.split())

# find position

print(mt.find("s"))

# is all alphanumeric

print(mt.isalnum())

# is all alphabetic

print(mt.isalpha())

# is all numeric

print((mt.isalnum()))









