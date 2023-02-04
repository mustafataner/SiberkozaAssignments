# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_mt = ["mustafa", "taner", "rumet", "egemen", "delal"]

for i in people_mt:
    print("current i: {}".format(i))

# break

for i in people_mt:
    if i == "rumet":
        break

    print("current i: {}".format(i))

# continue

for i in people_mt:
    if i == "rumet":
        continue

    print("current i: {}".format(i))


# range

for i in range(1,5):
    print("bu {}. döngüdür.".format(i))




# While loops execute a set of statements as long as a condition is true.


count = 0
while count <=10:
    print("count: {} ".format(count))
    count = count + 1

    
