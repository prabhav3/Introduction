# Comparison operators

# Equality/non-equality operators: ==, !=

var_a = 10
var_b = 10
var_c = 10.0
var_d = "10"

print(var_a == var_b, var_a == var_c, var_a == var_d)

# Python and JS use approximation
print(0.1 + 0.2 == 0.3)

print(var_a != var_b, var_a != var_c, var_a != var_d)

# Inequality operators >/>= and </<=

# Make sure the datatypes are the same during comparison

print(var_a > var_b, var_a > var_c, var_a < var_b, var_a < var_c)

# Type error: print(var_a > var_d)

print(var_a >= var_b, var_a >= var_c, var_a <= var_b, var_a <= var_c)
print()

# String comparison

var_e = "apple"
var_f = "banana"
var_g = "APPLE"
var_h = "BANANA"

# In the ASCII chart, lowercase letters' index is after uppercase letters, assigning them a larger number in alphabetical order

print(var_f > var_e, var_h > var_g)
# True
print(var_e > var_h)
# True
print("CHERRy" > "CHERRY")

# List/tuples comparison

# A tuple is a constant list

city_list_a = ["Amsterdam", "Berlin", "Chicago"]
city_list_b = ["Dubai"]
city_list_c = ["Amsterdam", "Berlin", "Dubai"]

print(city_list_b > city_list_a)
print(city_list_c > city_list_a)
print()

# Logical operator - and, or, & not

# And - true if all conditions are true

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

# Illustration 1: In an exam there are two tests and both of the tests have 100 marks each.
# In order to succeed in the exam, a student needs 40 or more marks in each test seperately
# Write a code snippet for the same

marks_1 = int(input("Enter the marks for test #1: "))
marks_2 = int(input("Enter the marks for test #2: "))

if marks_1 >= 40 and marks_2 >= 40:
    print("The student has passed the exam")
else:
    print("The student has failed the exam")

# Or - true if either condition is true

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print()

# Illustration 2: In an exam there are two tests and both of the tests have 100 marks each.
# In order to succeed in the exam, a student needs 40 or more marks in either test
# Write a code snippet for the same

marks_1 = int(input("Enter the marks for test #1: "))
marks_2 = int(input("Enter the marks for test #2: "))

if marks_1 >= 40 or marks_2 >= 40:
    print("The student has passed the exam")
else:
    print("The student has failed the exam")

# Not - true --> false, false --> true

print(not True)
print(not False)

compare = 5 > 10

if not compare:
    print("5 is less than 10")