# Functions: when a piece of code is used multiple times, it is better to use it as a function. It works on DRY principle, which means Don't Repeat Yourself
# Functions help to localize errors, if there is an error in the function code, it will be reflected everywhere the function is called

"""
for i in range(0, 10):
    print("Hello World")

print()

for i in range(0, 10):
    print("Hello World")

print()

for i in range(0, 10):
    print("Hello World")
"""

def function1():
    for i in range(0, 10):
        print("Hello World")

"""
function1()

print()

function1()

print()

function1()
"""

# Same result but shorter, nonrepeating code

# Function with parameters

"""
for i in range(1, 10):
    print("Hello World")

print()

for i in range(1, 15):
    print("Hola World")

print()

for i in range(1, 8):
    print("Bonjour World")
"""

def function2(length, message):
    for i in range(1, length):
        print(message)

"""
function2(10, "Hello World") # Positional arguments -- 10, "Hello World"

print()

function2(length = 15, message = "Hola World") # Keyword argument -- 15, "Hola World"

print()

function2(8, message = "Bonjour World") # Mixed argument -- 8, "Bonjour World"
"""

# Function with default parameters

for i in range(1, 10):
    print("Hello World")

print()

for i in range(1, 10):
    print("Hola World")

print()

for i in range(1, 15):
    print("Hello World")

def function3(length = 10, message = "Hello World"):
    for i in range(1, length):
        print(message)

function3()

print()

function3(message = "Hola World") # Use keyword argument for changing default parameters

print()

function3(length = 15)

# Argument passing for functions
# positional argument passing

def expression(a, b, c, d):
    print(f"{a=} {b=} {c=} {d=}")
    return a + b * c / d

call = expression(10, 20, 30, 40)
print(call)

# keyword argument passing

call = expression(a = 10, d = 40, b = 20, c = 30)
print(call)

# example of good keyword passing

"""
In US, people used to greet themselves with their first name first and last name's initial. But in certain cultures, for example, Hungary, people used to greet by their last name initial and followed by the first name.
Design a function database that is capable of handling both kinds of cultural references as first name being the first column followed by last name column
"""

def database(fname, lname):
    print("Inserting in the database")
    print(f"{fname=} {lname=}")

 # using positional arguments
# in US

database("Clark", "Kent")

# in Hungary

database("Kent", "Clark") # Kent is not the fname, but Hungarians will keep Kent first

# using keyword arguments
# in US

database(fname = "Clark", lname = "Kent")

# in Hungary

database(lname = "Kent", fname = "Clark")

# Mixed argument passing -- positional arguments should come before the keyword arguments

expression(10, 20, d = 40, c = 30)
expression(10, c = 30, d = 40, b = 20)

# Error cases
# expression(10, c = 30, d = 40, 20) positional argument should not follow keyword argument
# expression(10, 20, d = 40, b = 30) multiple values of argument b

# Functions help to localize errors

def greet():
    console.log("Hello from Python")