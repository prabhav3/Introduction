# Using nested for loops, we can build simple 2d geometric shapes and the outer for loop controls rows and inner for loop controls columns

red = "\033[31;1m"
cyan = "\033[36;1m"
reset = "\033[0;0m"

lines = int(input("How many lines do you want?: "))

print("Square pattern:")

for row in range(0, lines):
    for col in range(0, lines):
        print("*", end = " ")
    print()

print("Isosceles triangle perpendicular to left side pattern:")

for row in range(0, lines):
    for col in range (0, row + 1):
        print("*", end = " ")
    print()

print("Reverse isosceles triangle perpendicular to left side pattern:")

for row in range(0, lines):
    for col in range(row, lines):
        print("*", end=" ")
    print()

print("Complete isoscelese triangle pattern:")

for row in range(0, lines - 1):
    for col in range (0, row + 1):
        print("*", end = " ")
    print()

for row in range(0, lines):
    for col in range(row, lines):
        print("*", end=" ")
    print()

print("Isosceles triangle perpendicular to right side:")

for row in range(0, lines):
    for col in range(row, lines - 1):
        print(" ", end=" ")
    for col in range(0, row + 1):
        print("*", end=" ")
    print()

print("Reverse isosceles triangle perpendiculr to right side")

for row in range(0, lines):
    for col in range(0, row):
        print(" ", end=" ")
    for col in range(row, lines):
        print("*", end=" ")
    print()

print("Complete isosceles triangle perpendicular to right side")

for row in range(0, lines - 1):
    for col in range(row, lines - 1):
        print(" ", end=" ")
    for col in range(0, row + 1):
        print("*", end=" ")
    print()

for row in range(0, lines):
    for col in range(0, row):
        print(" ", end=" ")
    for col in range(row, lines):
        print("*", end=" ")
    print()

print("Hill pattern (isosceles triangle facing up)")

for row in range(0, lines):
    for col in range(row, lines - 1):
        print(" ", end=" ")
    for col in range(0, row + 1):
        print(f"{red}*{reset}", end=" ")
    for col in range(0, row):
        print(f"{cyan}*{reset}", end=" ")
    print()

print("Upside down hill patttern")

for row in range(0, lines):
    for col in range(0, row):
        print(" ", end=" ")
    for col in range(row, lines):
        print(f"{red}*{reset}", end=" ")
    for col in range(row, lines - 1):
        print(f"{cyan}*{reset}", end=" ")
    print()

print("Diamond pattern")

for row in range(0, lines - 1):
    for col in range(row, lines - 1):
        print(" ", end=" ")
    for col in range(0, row + 1):
        print(f"{red}*{reset}", end=" ")
    for col in range(0, row):
        print(f"{cyan}*{reset}", end=" ")
    print()

for row in range(0, lines):
    for col in range(0, row):
        print(" ", end=" ")
    for col in range(row, lines):
        print(f"{red}*{reset}", end=" ")
    for col in range(row, lines - 1):
        print(f"{cyan}*{reset}", end=" ")
    print()