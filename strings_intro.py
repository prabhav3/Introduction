# General properties: 

string_1 = "Hello World"
print(string_1, type(string_1))

# Concatenation

string_2 = "of Python"
string_3 = string_1 + " " + string_2

print(string_3)

# Multiplication by an integer

print(string_1 * 3)
# Finding total length of a string
print(f"The length of {string_1=} is {len(string_1)}")

# Indexing, slicing, and stepping

# Indexing

string_4 = "Prabhav"

print(string_4[0], string_4[-7])
print(string_4[1], string_4[-6])
print(string_4[2], string_4[-5])
print(string_4[3], string_4[-4])
print(string_4[4], string_4[-3])
print(string_4[5], string_4[-2])
print(string_4[6], string_4[-1])

# Slicing - the direction of slicing will always be left to right
# [lower index: upper index + 1]

# Starting from the very beginning - take the "prab"

print(string_4[0 : 4])
print(string_4[-7 : -3])
print(string_4[: 4])
print(string_4[: -3])

# Slicing in the middle - take the "abha"

print(string_4[2 : 6])
print(string_4[-5 : -1])

# Slicing until the end - take the "bhav"

print(string_4[3 : 7])
print(string_4[3 : 45])
print(string_4[-4 : 0]) # Doesn't work because 0 is in positive index and slice direction is left --> right
print(string_4[3 :])
print(string_4[-4 :])

# Stepping

print(string_4[:])
print(string_4[::1])
print(string_4[::2])
print(string_4[::3])
print(string_4[::4])
print()
print(string_4[::-1])
print(string_4[::-2])
print(string_4[::-3])