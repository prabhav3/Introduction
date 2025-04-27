import datetime

# f String means formatted strings

# Write mathematical operators and expressions and call functions

num_1 = 14
num_2 = 7

print(f"Addition: {num_1 + num_2}\nSubtraction: {num_1 - num_2}\nMultiplication: {num_1 * num_2}\nDivision: {num_1 / num_2}")

string_1 = "Hello world"

print(f"{string_1.upper()}")

# Using f string for multiline strings

print(f"""
Addition: {num_1 + num_2}
Subtraction: {num_1 - num_2}
Multiplication: {num_1 * num_2}
Division: {num_1 / num_2}
""")

# String formatter

string = "Welcome to the game!"

print(f"{string}")
print("-->" + f"{string:^55}" + "<--")
print("-->" + f"{string:@^55}" + "<--")

print("-->" + f"{string:>55}" + "<--")
print("-->" + f"{string:@>55}" + "<--")

print("-->" + f"{string:<55}" + "<--")
print("-->" + f"{string:@<55}" + "<--")

# Rounding of floats

result = 33.456876

print(f"{result:.3f}")
print(f"{result:.2f}")
print(f"{result:.1f}")
print(f"{result:.0f}")

# Scientific numbers

planck_constant = 6.62607015e-34

print(f"{planck_constant:.3e}")
print(f"{planck_constant:.2e}")
print(f"{planck_constant:.1e}")
print(f"{planck_constant:.0e}")

# Formatting of digits

big_num = 10_000_000_000

print(f"Ten billion: {big_num}")
print(f"Ten billion: {big_num:,}")

# Showing percentage

fraction = 129/343

print(f"{fraction:.2%}")
print(f"{fraction:.1%}")
print(f"{fraction:.0%}")

# 0 or character padding for numbers

number = 8167

# Fill the left side with characters
print(f"{number:>10d}")
print(f"{number:#>10d}")
print(f"{number:x>10d}")
print(f"{number:0>10d}")

# Fill the right side with characters
print(f"{number:<10d}")
print(f"{number:#<10d}")
print(f"{number:x<10d}")
print(f"{number:0<10d}")

# Formatting dates

# time and date - utc
now = datetime.datetime.now()

print(now)

formatted_date = f"{now:%A, %Y-%b-%d}"
formatted_time = f"{now:%I:%M:%S %p}"

print("For CST: ")
print(f"{formatted_date}, {formatted_time}")

# Reading a variable name with its value

a_var = "This is a variable"

print(f"{a_var}")
print(f"{a_var=}")