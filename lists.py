# A List is a collection which is ordered and changeable. Allows duplicate members.

# creat list

number_mt = [1, 2, 3, 4, 5, 6]

fruits_mt = ["apples", "oranges", "grapes", "pears"]

# get a value

print(fruits_mt[0])

# get length

print(len(fruits_mt))

# append to list

fruits_mt.append("banana")
print((fruits_mt))

# remove from list

fruits_mt.remove("banana")
print((fruits_mt))

# insert into position

fruits_mt.insert(2, "banana")
print((fruits_mt))

# remove with pop

fruits_mt.pop(2)
print((fruits_mt))

# reverse list

fruits_mt.reverse()
print((fruits_mt))

# sort list

fruits_mt.sort()
print((fruits_mt))

# reverse sort

fruits_mt.sort(reverse=True)
print((fruits_mt))

# change value

fruits_mt[0] = "Mangos"
print((fruits_mt))

