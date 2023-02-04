# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 


# A Set is a collection which is unordered and unindexed. No duplicate members.


fruits_mt = ("apples", "oranges", "grapes")

# single value needs trailing comma

fruits_mt2 = ("apple", )

# get value
print(fruits_mt[1])

# can't change value

# fruits_mt[0] = "banana"

# delete tuple
del fruits_mt2

# get lenght

print(len(fruits_mt))

fruits_mt_set = {"apple", "banana", "mango"}

# check if in set
print("apple" in fruits_mt_set)

# add to set

fruits_mt_set.add("orange")

# remove from set

fruits_mt_set.remove("orange")
print(fruits_mt_set)

# add duplicate
fruits_mt_set.add("apple")

# clear set

fruits_mt_set.clear()

# delete

del fruits_mt_set



