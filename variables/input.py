import sys

name = input("Please enter your name ")
print(name, "Nice to meet you")

# Type conversion - int: integer, float: decimal, str: string

num_1 = int(input("Enter the number 1: "))
num_2 = int(input("Enter the number 2: "))
print("Addition:", num_1 + num_2)
print("Subtraction:", num_1 - num_2)
print("Division:", num_1 / num_2)
print("Multiplication:", num_1 * num_2)

num_3 = float(input("Enter a number to square: "))
print("Square of the number:", num_3**2)

sys.exit("Code has finished")