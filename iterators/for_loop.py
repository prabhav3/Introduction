"""
iteration: The process of repeatedly executing a set of statements, typically using a loop, to traverse through elements of a collection or sequence.

iterator: An object that implements the iterator protocol, consisting of the __iter__() and __next__() methods, allowing traversal through all the elements of a collection, one element at a time.

iterable: An object capable of returning its members one at a time, allowing it to be iterated over in a loop. An iterable must implement the __iter__() method, which returns an iterator.
"""

# For loop + range class

# The for loop is used to iterate over a sequence (like a list, tuple, or string) or any iterable object.

for i in range(0, 10): # Lower limit, upper limit + 1. Lower limit is by default 0
    print(i, end=" ")

print()

for i in range(1, 11): # 11-1 = 10, 10 values will be returned starting from 1
    print(i, end=" ")

print()

# Generating negative numbers

for i in range(-10, 0): # -10, -9, -8, ..., -1
    print(i, end=" ")

print()

# Generate even numbers between 21 to 40 inclusive

# Solution 1: Using range with step

for i in range(21, 41):
    if i % 2 == 0: # Check if the number is even
        print(i, end=" ")

print()

# Solution 2: Using range with step argument

for i in range(22, 41, 2): # Start from 22 (where the steps start), go to 41, step by 2
    print(i, end=" ")

print()

# Generate odd numbers between 21 to 40 inclusive

# Solution 1: Using the conditional check

for i in range(21, 41):
    if i % 2 != 0: # Check if the number is odd
        print(i, end=" ")

print()

# Solution 2: Using range with step argument

for i in range(21, 41, 2): # Start from 21 (where the steps start), go to 41, step by 2
    print(i, end=" ")

print()

# Concept of negative stepping

for i in range(10, 0): # This will not print anything because the lower limit must be less than the upper limit for positive stepping
    print(i, end=" ")

print()

for i in range(10, 0, -1): # This will print numbers from 10 to 1 in reverse order
    print(i, end=" ")

print()

# Generate the numbers from negative 1 to -10

for i in range(-1, -9, -1): # This will print from -1 to -8 in reverse order (because for negative stepping you must subtract 1 instead of adding)
    print(i, end=" ")

print()

for i in range(-1, -11, -1):
    print(i, end=" ")

print()

print()
print("----------------------------------------------------------------------")
print("-----------------------For Loop With Strings--------------------------")
print()

# 1: Direct method

string_1 = "Prabhav"

for char in string_1: # This will iterate through each character in the string
    print(char, end=" ")

print()

# 2: Using range with len() function

for i in range (0, len(string_1)):
    print(string_1[i], end=" ") # Putting the index in the string to get each character, without it it will print the indices

print()

# Illustration 1: count the total number of vowels in the word "Mississippi"

string_2 = "Mississippi"

# First solution: Using count function

count = 0
for char in string_2:
    char = char.lower()  # Convert to lowercase to handle both uppercase and lowercase vowels
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1

print(f"Total number of vowels in '{string_2}' is: {count}")

# Second solution: Using memebership operator

count = 0
for char in string_2:
    if char.lower() in 'aeiou':
        count += 1

print(f"Total number of vowels in '{string_2}' is: {count}")

# Illustration 2: Find the total number of words words in the paragraph

random_paragraph = "One can cook on and with an open fire. These are some of the ways to cook with fire outside. Cooking meat using a spit is a great way to evenly cook meat. In order to keep meat from burning, it's best to slowly rotate it. Hot stones can be used to toast bread. Coals are hot and can bring things to a boil quickly. If one is very adventurous, one can make a hole in the ground, fill it with coals and place foil-covered meat, veggies, and potatoes into the coals, and cover all of it with dirt. In a short period of time, the food will be baked. Campfire cooking can be done in many ways."

total_words = 1 if random_paragraph else 0 # Initialize to 1 to count the first word if the paragraph is not empty, otherwise 0

for char in random_paragraph:
    if char == " ":
        total_words += 1

print(f"Total number of words in the paragraph is: {total_words}")
print(f"Check the actual amount: {len(random_paragraph.split())}")

# Illustration 3: Reversing a string, the word "desserts" ==> "stressed" using for loop

string_3 = "desserts"
reversed_string = ""

# Solution 1: Using direct looping

for char in string_3:
    reversed_string =  char + reversed_string  # Prepend each character to the reversed string

print(f"Reversed string of '{string_3}' is: {reversed_string}")

# Solution 2: Starting from the last to 0th index

reversed_string = ""
last_index = len(string_3) - 1

for index in range(last_index, -1, -1):  # Start from the last index to 0
    reversed_string += string_3[index]  # Append each character to the reversed string

print(f"Reversed string of '{string_3}' is: {reversed_string}")

# Complete in lists section

print()
print("----------------------------------------------------------------------")
print("--------------------Running For Loops For Lists-----------------------")
print()

fruits_list = ["apple", "banana", "cherry", "date", "elderberry"]

# 1: Direct method

for fruit in fruits_list:
    print(fruit, end=" ")

print()

# 2: Indexing using range and len() - value manipulation

for index in range(0, len(fruits_list)):
    print(fruits_list[index], end=" ")

print()

# 3: Using the enumerate() function - index and value manipulation

for index, fruit in enumerate(fruits_list):
    print(index, ":", fruit)

print()

for index, fruit in enumerate(fruits_list, start=1001):
    print(index, ":", fruit)

print()

# Not in place operations

# Illustration 4: For the random paragraph, highlight the word cook whenever it appears in the paragraph in red color

RED = "\033[91m"
RESET = "\033[0m"

highlighted_string = ""
para_list = random_paragraph.split(" ")

for word in para_list:
    if "cook" in word.lower():
        highlighted_string += f"{RED}{word}{RESET}" + " "
    else:
        highlighted_string += word + " "

print(highlighted_string)

# Illustration 5: Find the total words in a string
# Find the total words in the paragraph string

count = 0
para_list = random_paragraph.split(" ")

for _ in para_list:
    count += 1

print(f"The total word count for the paragraph is: {count}")

# Illustration 6: Find the total number of words which have 3 or more vowels in them

fruits_list = ["apple", "banana", "dragonfruit", "guava", "pineapple", "strawberry", "watermelon"]

# 1st solution

count = 0
vowels = "aeiou"

for fruit in fruits_list:
    cnt = 0
    for char in fruit:
        if char.lower() in vowels:
            cnt += 1
    if cnt >= 3:
        count += 1

print(f"The total number of fruits with more than 3 vowels in their name are: {count}")

# 2nd solution

count = 0

for fruit in fruits_list:
    if fruit.count("a") + fruit.count("e") + fruit.count("i") \
    + fruit.count("o") + fruit.count("u") >= 3:
        count += 1

print(f"The total number of fruits with more than 3 vowels in their name are: {count}")

# Dealing with list mutability - in place changes

# Illustration 7: For the given list, find the square values of the list in place

nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original number list: {nums_list}")

for index in range(0, len(nums_list)):
    nums_list[index] = nums_list[index] ** 2

print(f"Squared number list: {nums_list}")

# Illustration 8: For the above fruit list, convert it into uppercase fruit list using enumerate

print(f"Lowercase list: {fruits_list}")

for index, fruit in enumerate(fruits_list):
    fruits_list[index] = fruit.upper()

print(f"Uppercase list: {fruits_list}")

print()
print("----------------------------------------------------------------------")
print("--------------------Running For Loops for Tuples----------------------")
print()

# Same as list but without changing the values

marks_tuple = (82, 100, 96, 93, 89, 91)

# Illustration 9: Group the marks into frequency bin "81-85, 86-90, 91-95, 96-100"

frequency_bin = {"81-85": 0, "86-90": 0, "91-95": 0, "96-100": 0}

for marks in marks_tuple:
    if 80 < marks <= 85:
        frequency_bin["81-85"] += 1
    elif 85 < marks <= 90:
        frequency_bin["86-90"] += 1
    elif 90 < marks <= 95:
        frequency_bin["91-95"] += 1
    elif 95 < marks <= 100:
        frequency_bin["96-100"] += 1

print(f"The final frequency bin is {frequency_bin}")

print()
print("----------------------------------------------------------------------")
print("-------------------Number Based or Miscellaneous----------------------")
print()

# Illustration 10: Determine all prime numbers in a range

limit_1 = 1 # int(input("Enter the lower limit: "))
limit_2 = 100 # int(input("Enter the upper limit: "))
prime_number = []

for num in range(limit_1, limit_2):
    sqrt = int(num ** 0.5)
    is_prime = True
    for i in range(2, sqrt+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num not in [1]:
        prime_number.append(num)

print(f"The list of prime numbers between {limit_1} and {limit_2} is {prime_number}")

# Illustration 11: Finding the sequence of fibonacci sequence

num_1 = 0
num_2 = 1
sequence = [num_1, num_2]

for i in range(0, 10): # For any other sequence length, change the range
    num_1, num_2 = num_2, num_1 + num_2
    sequence.append(num_2)

print(f"The first ten numbers in the Fibonacci sequence are: {sequence}")

# Illustration 12: Finding the factorial of a number

number = 6
factor = 1

for i in range(1, number + 1):
    factor *= i

print(f"The factorial of {number} is {factor}")