# Every function can behave as a variable with the help of the return keyword

# If the return keyword is not specified or only specified without any value the value of the function will be None

# The return keyword serves two purposes: 
# 1: To return value(s) out of the function
# 2: If the function encounters a return keyword, it immediately stops its execution

import random
import string

def add_by_10_print(num):
    print(num+10)

def add_by_10_return(num):
    return num + 10

call1 = add_by_10_print(100)
print(call1)

call2 = add_by_10_return(120)
print(call2)

# truthsy, falsy: returning true or false value from a function

# Illustration 1: Check whether the number is even or not

def is_even(num):
    if num % 2 == 0:
        return True
    return False

num = random.randint(1, 100)

call3 = is_even(num)

if call3:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

# Illustration 2: Check whether a string is a pangram or not

def pangram(paragraph):
    for char in string.ascii_lowercase:
        if char not in paragraph.lower():
            return False
    return True

paragraph = "The quick brown fox jumps over the lazy dog."

call4 = pangram(paragraph)

if call4:
    print("The given paragraph is a pangram.")
else:
    print("The given paragraph is not a pangram.")

# Illustration 3: Check whether a given year is a leap year or not

def leap_year(year):
    if year < 1582:
        return None
    if year % 400:
        return True
    elif year % 100:
        return False
    elif year % 4:
        return True
    return False

year = int(input("Enter a year to check whether it is a leap year: "))

call5 = leap_year(year)

if call5 is None:
    print(f"Please enter a year after 1582")
elif call5:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")