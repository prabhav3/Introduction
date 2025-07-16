import timeit

# Properties of tuples
# A tuple is a datatype: something that can store another value, that is indexable; however, it is immutable

# Ways of building a tuple
a_tuple = (10, 20, 30, 40, 50)
b_tuple = "a", "b", "c"
print(a_tuple, type(a_tuple))
print(b_tuple, type(b_tuple))

# This is the way to build a single element tuple - put comma afterwards
c_tuple = 4,
print(c_tuple, type(c_tuple))

# General properties

# Concatenation of tuples
d_tuple = (10, 20, 30, 40)
e_tuple = (50, 60, 70, 80)
f_tuple = d_tuple + e_tuple
print(f_tuple)

print()
print("----------------------------------------------------------------------")
print()

# Multiplication by an integer
g_tuple = (True,) * 10    # True will be multiplied by 10 in the array
print(g_tuple)

print()
print("----------------------------------------------------------------------")
print()

# Indexing, slicing, and stepping

# Indexing
fruit_tuple = "apple", "banana", "orange", "grape", "mango", "tomato"
print(fruit_tuple[0], fruit_tuple[-6])    # prints apple
print(fruit_tuple[1], fruit_tuple[-5])    # prints banana  \
print(fruit_tuple[2], fruit_tuple[-4])    # prints orange    } prints each twice for positive and negative index
print(fruit_tuple[3], fruit_tuple[-3])    # prints grape     /
print(fruit_tuple[4], fruit_tuple[-2])    # prints mango
print(fruit_tuple[5], fruit_tuple[-1])    # prints tomato

print()
print("----------------------------------------------------------------------")
print()

# Slicing
# lower index, upper index +1

# Slicing from the beginning - apple, banana, and orange
print(fruit_tuple[0:3])
print(fruit_tuple[-6:-3])
print(fruit_tuple[:3])
print(fruit_tuple[:-3])
print()

# Slicing in the middle - orange, grape, mango
print(fruit_tuple[2:5])
print(fruit_tuple[-4:-1])
print()

#Slicing from the end - grape, mango, tomato
print(fruit_tuple[3:6])
print(fruit_tuple[-3:])  # 0 will not work because the direction will change to positive index
print(fruit_tuple[3:])

print()
print("----------------------------------------------------------------------")
print()

# Stepping
print(fruit_tuple[:])    # This gives you the whole tuple (starting from beginning and ending at the end)
print(fruit_tuple[::1])  # Gives you the whole tuple (you step on every item)
print(fruit_tuple[::2]) # Steps on every two items, skips one, this increases for every increased step amount

# Negative stepping
print(fruit_tuple[::-1]) # Steps from right to left, (negative index)
print(fruit_tuple[::-2])

print()
print("----------------------------------------------------------------------")
print()

# Unpacking of tuples

history, math, science = ("History", "Math", "Science")
print(history, math, science)

# Unpacking first 2 objects
history, math, * other = ("History", "Math", "Science", "English", "Geography")
print(history, math)
print(other)

# Unpacking last 2 objects
* others, english, geography = ("History", "Math", "Science", "English", "Geography")
print(english, geography)
print(others)

print()
print("----------------------------------------------------------------------")
print("------------------------------Functions-------------------------------")
print()

# There are only element tracking functions
# .count(), .index()

student_tuple = ("Alex", "Bob", "Claire", "Alex", "Joshua", "Alex")

# .count(value) - counts how many instances of a value there are
print(student_tuple.count("Alex"))
print()

# .index(value, start_index, end_index+1) - finds the index of a value
print(student_tuple.index("Alex"))
print(student_tuple.index("Alex", 1, len(student_tuple)))
print(student_tuple.index("Alex", 4, len(student_tuple)))


print()
print("----------------------------------------------------------------------")
print("-------------------------Speed Comparison---------------------------")
print()

# Speed comparison between lists and tuples

list_speed = timeit.timeit("X=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", number=1_000_000)
tuple_speed = timeit.timeit("X=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)", number=1_000_000)
print(f"The list speed is: {list_speed} and the tuple speed is: {tuple_speed}") # Lists are almost 4 times slower