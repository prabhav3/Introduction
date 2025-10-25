# *args --  if a function has te parameter, *args, that means that function can take any amount of positional arguments

def addition(*args, **kwargs):
    total = 0
    for i in args:
        total += i
    return total

call = addition()
print(call)

call1 = addition(1, 3, 9)
print(call1)

call2 = addition(1, 3, 9, 13, 36)
print(call2)

# turning arguments of a function only positional (/)

def expression1(a, b, c, /):
    return a + b * c

call3 = expression1(10, 5, 2)

print(call3)

# call4 = expression1(b=5, a=10, c=2) Throws error

# print(call4)

print()
print("----------------------------------------------------------------------")
print("--------------------------Keyword Arguments---------------------------")
print()

def zoo(*args, **kwargs):
    for key in kwargs:
        print(key, ":", kwargs[key])

call5 = zoo(zebra=5, lion=3, monkeys=50)

call6 = zoo(tiger=5, zebra=8, honey_bee=200, penguin=20)

# Note: *args and **kwargs both go hand in hand

# Making a function accepting only keyword argument values

def expression2(*, a, b, c):
    return a + b * c

call7 = expression2(a=10, b=5, c=2)

print(call7)

# call8 = expression2(10, 5, 2) Throws error