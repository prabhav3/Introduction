import math
import os
import time

RED = "\033[1;31m"
GREEN =  "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
ORANGE = "\033[38;5;208m"

message = """
Choose from the following options:
Addition        -   Enter 1
Subtraction     -   Enter 2
Multiplication  -   Enter 3
Division        -   Enter 4
Remainder       -   Enter 5
Quotient        -   Enter 6
Power           -   Enter 7
LCM             -   Enter 8
GCF             -   Enter 9
Square Root     -   Enter 10
Square          -   Enter 11
Cube Root       -   Enter 12
Cube            -   Enter 13
Exit            -   Enter exit
"""

prev, answer = None, None

while True:
    print(f"{ORANGE}Welcome to the calculator".rjust(50))
    try:
        if prev:
            num_1 = answer
            num_2 = float(input("Enter the 2nd number: "))
        else:
            num_1 = float(input("Enter the 1st number: "))
            num_2 = float(input("Enter the 2nd number: "))
    except Exception as e:
        print(f"An error occurred:\n{str(e)}")
        continue
    print(f"{ORANGE}{message}")
    choice = input("Enter the corresponding number for the operation: ").strip()

    try: 
        match choice:
            case "1":
                answer = num_1 + num_2
                print(f"{num_1} + {num_2} = {answer}")
            case "2":
                answer = num_1 - num_2
                print(f"{num_1} - {num_2} = {answer}")
            case "3":
                answer = num_1 * num_2
                print(f"{num_1} × {num_2} = {answer}")
            case "4":
                answer = num_1 / num_2
                print(f"{num_1} ÷ {num_2} = {answer:.3f}")
            case "5":
                answer = num_1 % num_2
                print(f"{num_1} ÷ {num_2} = {num_1 // num_2} r{answer}")
            case "6":
                answer = num_1 // num_2
                print(f"{num_1} ÷ {num_2} = {answer}")
            case "7":
                answer = num_1 ** num_2
                print(f"{num_1} ^ {num_2} = {answer}")
            case "8":
                num_1, num_2 = int(num_1), int(num_2)
                answer = math.lcm(num_1, num_2)
                print(f"The LCM of {num_1} and {num_2} is {answer}")
            case "9":
                num_1, num_2 = int(num_1), int(num_2)
                answer = math.gcd(num_1, num_2)
                print(f"The GCF of {num_1} and {num_2} is {answer}")
            case "10":
                which_num = input(f"Which number do you wish to take the square root of?: 1/2: ").strip()
                answer = math.sqrt(num_1) if which_num == "1" else math.sqrt(num_2)
                print(f"The square root is {answer}")
            case "11":
                which_num = input(f"Which number do you wish to square?: 1/2: ").strip()
                answer = math.pow(num_1, 2) if which_num == "1" else math.pow(num_2, 2)
                print(f"The square is {answer}")
            case "12":
                which_num = input(f"Which number do you wish to take the cube root of?: 1/2: ").strip()
                answer = math.pow(num_1, 1/3) if which_num == "1" else math.pow(num_2, 1/3)
                print(f"The cube root is {answer}")
            case "13":
                which_num = input(f"Which number do you wish to cube?: 1/2: ").strip()
                answer = math.pow(num_1, 3) if which_num == "1" else math.pow(num_2, 3)
                print(f"The cube is {answer}")
            case "exit":
                break
    except Exception as e:
        print(f"{RED}{str(e)}").capitalize()
        print(f"{RED}Please try again")
    use = input(f"{ORANGE}Do you wish to use the previous answer as an input for the next operation?: Y/N: ").strip().lower()
    if use == "y":
        prev = True
    else:
        prev = None
    time.sleep(2)
    os.system("clear||cls")