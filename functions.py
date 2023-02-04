# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

def say_hello(name):
    print("merhaba {}".format(name))

say_hello("mustafa")

def sum_mt(num1, num2):
    total = num1 + num2
    return total

num = sum_mt(2,5)

print(num*2)

# lambda

getsum_mt = lambda num1, num2 : num1 + num2
print(getsum_mt(10,35))


