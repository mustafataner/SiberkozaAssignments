# If/ Else conditions are used to decide to do something based on something being true or false

x = 1
y = 2

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# if x > y:
#    print("{} is greater than {} ".format(x, y))

"""
if x > y:
    print("{} is greater than {} ".format(x, y))

elif x == y:
    print("{} is equal to {} ".format(x, y))

else:
    print("{} is greater than {} ".format(y, x))
"""

# nested if

if x > 2:
    if x <= 10:
        print("{} is greather than 2 and less than or equal to 10".format(x))





# Logical operators (and, or, not) - Used to combine conditional statements


"""
# and
if x > 2 and x <= 10:
    print("{} is greather than 2 and less than or equal to 10".format(x))
# or
if x > 2 or x <= 10:
    print("{} is greather than 2 or less than or equal to 10".format(x))

# not
if not(x==y):
    print("{} is not equal to {}".format(x,y))
"""


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

number_mt = [1, 5, 3, 10, 20]

if x in number_mt:
    print(x in number_mt)


if x not in number_mt:
    print(x  not in number_mt)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
