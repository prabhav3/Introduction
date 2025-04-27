# Mathematical operators

# +, -, *, /, //, %, **

# Mathematical rules for +, -, *, //, and %

"""
int (+, -, *, //, and %) int = int
int/float = float
float/float = float
"""

print(25//5, 26//5, 27//5, 28//5, 29//5, 30//5)
print()
print(25//-5, 26//-5, 27//-5, 28//-5, 29//-5, 30//-5)
print()
print(25%5, 26%5, 27%5, 28%5, 29%5, 30%5)
print()
print(-25%5, -26%5, -27%5, -28%5, -29%5, -30%5)

# Mathematical rules for division

"""
int/int = float
int/float = float
float/float = float
"""

print()
print(15/3)

# Mathematical rules for exponents

"""
int int = int/float
"""

print()
print(3**0, 3**1, 3**2, 3**3)
print()
print(2**-1, 2**-2, 2**-3)
print()
print((-2)**2, (-2)**3)

# Rule 1: PEMDAS is always followed

print()
print(8+3*5)

# Rule 2: Direction of calculation will be from left to right

print()
# Expression 1
expression_1 = 250//35//2
# Left to right --> (250//35)//2 --> 7//2 --> 3
# Right to left --> 250//(35//2) --> 250//17 --> 14
print(expression_1)

# print(57/0) --> ZeroDivisionError

print()
expression_2 = 300%27%3
# Left to right --> (300%27)%3 --> 3%3 --> 0
# Right to left --> 300%(27%3) --> 300%0 --> ZeroDivisionError
print(expression_2)

# Rule 3: In case of multiple exponents, the direction of calculation will be right to left

print()
expression_3 = 2**3**2
# Left to right --> (2**3)**2 --> 8**2 --> 64
# Right to left --> 2**(3**2) --> 2**9 --> 512
print(expression_3)