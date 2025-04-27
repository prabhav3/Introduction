print("My name is Prabhav")

# Properties of print

print()

print("Hello World", 5+5, True)

# Primitives in Python
# int, float, string, boolean, none

print()

print(3, type(3))
print(3.02, type(3.02))
print("Hello World", type("Hello World"))
print(5>10, type(5>10))
print(None, type(None))

print("---------------------------------------------")

# Concept of a variable
# Format: myVariable (camel-casing in JS), my_variable (snake-casing in Python)

my_variable = 3<2
print(my_variable, type(my_variable))

my_variable = "This is a variable"
print(my_variable, type(my_variable))

print("---------------------------------------------")

# Sep and end argument in print

# Sep

print()
print("Hello to the world of Python", sep="--")

print()
print("Hello", "to", "the", "world", "of", "Python", sep="--")

# End

print()
print("This is line #1")
print("This is line #2")

print()
print("This is line #1", end=", ")
print("This is line #2")

print("---------------------------------------------")

# Special characters

# "\" is the escape character

print()
# print(""Hello World"")

print("\"Hello World\"")

# "\\" is the double escape character

print("\\\"Hello World\\\"")

# "\n" is the new line character

print()
print("This is line #1\nThis is line #2\nThis is line #3")

# "\t" is the tab character

print()
print("Welcome\tto\tthe\tworld\tof\tPython\tprogramming")

# "\b" is the backspace character

print()
print("Welcome\bto\bthe\bworld\bof\bPython\bprogramming")

print("---------------------------------------------")

# Using special characters with sep and end arguments

# Sep

print("Welcome", "to", "the", "world", "of", "Python", sep="\\")
print()
print("Welcome", "to", "the", "world", "of", "Python", sep="\n")
print()
print("Welcome", "to", "the", "world", "of", "Python", sep="\t")
print()
print("Welcome", "to", "the", "world", "of", "Python", sep="\b")
print()
print("Welcome", "to", "the", "world", "of", "Python", sep="\r")
print()

# End

print("This is line 1", end="\r")
print("This is line 2")

print()