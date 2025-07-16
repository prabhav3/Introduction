# Properties of a list
# A list is a datatype: something that can store another value, mutable, indexable

# General properties

# Concatenation of lists
a_list = [10, 20, 30, 40]
b_list = [50, 60, 70, 80]
c_list = a_list + b_list
print(c_list)

print()
print("----------------------------------------------------------------------")
print()

# Multiplication by an integer
d_list = [True] * 10    # True will be multiplied by 10 in the array
print(d_list)

print()
print("----------------------------------------------------------------------")
print()

# Indexing, slicing, and stepping

# Indexing
fruit_list = ["apple", "banana", "orange", "grape", "mango", "tomato"]
print(fruit_list[0], fruit_list[-6])    # prints apple
print(fruit_list[1], fruit_list[-5])    # prints banana  \
print(fruit_list[2], fruit_list[-4])    # prints orange    } prints each twice for positive and negative index
print(fruit_list[3], fruit_list[-3])    # prints grape     /
print(fruit_list[4], fruit_list[-2])    # prints mango
print(fruit_list[5], fruit_list[-1])    # prints tomato

print()
print("----------------------------------------------------------------------")
print()

# Slicing
# lower index, upper index +1

# Slicing from the beginning - apple, banana, and orange
print(fruit_list[0:3])
print(fruit_list[-6:-3])
print(fruit_list[:3])
print(fruit_list[:-3])
print()

# Slicing in the middle - orange, grape, mango
print(fruit_list[2:5])
print(fruit_list[-4:-1])
print()

#Slicing from the end - grape, mango, tomato
print(fruit_list[3:6])
print(fruit_list[-3:])  # 0 will not work because the direction will change to positive index
print(fruit_list[3:])

print()
print("----------------------------------------------------------------------")
print()

# Stepping
print(fruit_list[:])    # This gives you the whole list (starting from beginning and ending at the end)
print(fruit_list[::1])  # Gives you the whole list (you step on every item)
print(fruit_list[::2]) # Steps on every two items, skips one, this increases for every increased step amount

# Negative stepping
print(fruit_list[::-1]) # Steps from right to left, (negative index)
print(fruit_list[::-2])

print()
print("----------------------------------------------------------------------")
print("------------------------------Functions-------------------------------")
print()

# Important functions for lists

# 1: Element addition functions
# .append(), .insert(), .extend()

# .append(value) - inserts the value at the end of the list
print("Fruits before:", fruit_list, sep="\n")
fruit_list.append("pineapple")
fruit_list.append("starfruit")
print("Fruits after:", fruit_list, sep="\n")
print()

# .insert(index, value) - inserts a value at a specific index and shifts the other content of that index rightwards
# insert guava between grape and mango, insert strawberry before starfruit
fruit_list.insert(4, "guava")
fruit_list.insert(-1, "strawberry") # insert cant put anything at the end
print("Fruit list after insertion:", fruit_list, sep="\n")
print()

# list_a.extend(list_b) - works like concatenation
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8,]
list_a.extend(list_b)
print("List a after extending:", list_a, sep="\n")

print()
print("----------------------------------------------------------------------")
print()

# 2: Deletion
# .pop(), .remove()

# .pop() | .pop(index) - if used without index, removes last element, otherwise removes specified index
# remove strawberry, starfruit, apple, and banana from the fruit list
fruit_list.pop()
fruit_list.pop()
print("Popping the last 2 elements:", fruit_list, sep="\n")
fruit_list.pop(0)
fruit_list.pop(0) # We use 0 both times because once apple is deleted banana becomes the first index
print("Popping at specified index:", fruit_list, sep="\n")
print() 

# .remove(value) - removes only the first occurrence of the specified value, it is advisable to use pop instead!
# remove guava from the list
fruit_list.remove("guava")
print("Removing the specific value:", fruit_list, sep="\n")

print()
print("----------------------------------------------------------------------")
print()

# 3: Element tracking
# .count(), .index()

student_list = ["Alex", "Bob", "Claire", "Alex", "Joshua", "Alex"]

# .count(value) - counts how many instances of a value there are
print(student_list.count("Alex"))
print()

# .index(value, start_index, end_index+1) - finds the index of a value
print(student_list.index("Alex"))
print(student_list.index("Alex", 1, len(student_list)))
print(student_list.index("Alex", 4, len(student_list)))

print()
print("----------------------------------------------------------------------")
print()

# 4: Sorting elements
# sorted() - inbuilt function, creates a new list with sorted values either numerical or alphabetical
num_list = [1, 3, 2, 4, 7, 5, 99, 13, 44, 8, 9]
fruit_list = ["banana", "apple", "starfruit", "grapefruit", "strawberry", "guava"]

sorted_nums_list = sorted(num_list)
print(f"Sorted number list:\n{sorted_nums_list}")

rev_sorted_nums_list = sorted(num_list, reverse=True)
print(f"Reverse sorted number list:\n{rev_sorted_nums_list}")
print()

sorted_fruit_list = sorted(fruit_list)
print(f"Sorted fruit list:\n{sorted_fruit_list}")

rev_sorted_fruit_list = sorted(fruit_list, reverse=True)
print(f"Reverse sorted fruit list:\n{rev_sorted_fruit_list}")

# .copy() - create a separate memory space

fruit_list_copy = fruit_list
print(fruit_list_copy is fruit_list)

fruit_list.append("grape")
fruit_list.append("dragonfruit")

fruit_list_copy.pop(0)
fruit_list_copy.pop(0)

print(fruit_list, fruit_list_copy, sep="\n")

print()

fruit_list = ['apple', 'banana', 'grapefruit', 'guava', 'starfruit', 'strawberry']

fruit_list_copy = fruit_list.copy()
print(fruit_list_copy is fruit_list)

fruit_list.append("grape")
fruit_list.append("dragonfruit")

fruit_list_copy.pop(0)
fruit_list_copy.pop(0)

print(fruit_list, fruit_list_copy, sep="\n")