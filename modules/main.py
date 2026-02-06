"""
A module in Python is just a file (usually something.py) that contains Python code: variables, functions, classes, and runnable statements. Think of it as a toolbox you can import 🧰.
Why modules exist
Reuse code across many programs
Organize big projects into smaller pieces
Avoid copy-paste
Create namespaces (so names don’t collide)
"""

import module1
from module2 import random_integer, random_picker

print("Calling functions with values of 50 and 100")

call_add = module1.addition(50, 100)
call_sub = module1.subtraction(50, 100)
call_mult = module1.multiplication(50, 100)
call_div = module1.division(50, 100)

print(f"Addition: {call_add}\nSubtraction: {call_sub}\nMultiplication: {call_mult}\nDivision: {call_div}")

print("Randomly picking one number from 1 to 100 and a value from Rock, Paper, Scissors")

rps = ["Rock", "Paper", "Scissors"]

number = random_integer(1, 100)
print(number)

rpschoice = random_picker(rps)
print(rpschoice)