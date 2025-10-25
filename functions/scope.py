# Global scope

var_a = 50 # This is the global scope and a global variable--can be accessed from anywhere in the code

def first_function():
    print(var_a)

print(var_a)
first_function()

def second_function():
    var_b = 99
    print(var_b)

second_function()
# print(var_b) not defined error, cannot read function declared inside of a function in the global scope

var_c = "Hello world"

def third_function():
    var_c = "Goodbye world"
    print(var_c)

print(var_c)
third_function()
print(var_c)

# global keyword -- helps connect local and global variables

var_d = [1, 3, 4, 9, 15]

def fourth_function():
    global var_d, var_c
    # var_a += 1 cannot directly edit a global variable at a local scope
    var_c += " of Python"
    var_d[3] = 10

print(var_c)
print(var_d)
fourth_function()
print(var_c)
print(var_d)