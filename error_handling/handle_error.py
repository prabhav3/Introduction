# Handling specific errors

try:
    num1 = 12 # int(input("Enter the first number: "))
    num2 = 1 # int(input("Enter another number: "))
    divide = num1 / num2
    print(divide)
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division calculated successfully.")
finally:
    print("Database and API connections closed successfully.")

# Handle unknown error

try:
    num1 = 19 # int(input("Enter the first number: "))
    num2 = 1 # int(input("Enter another number: "))
    divide = num1 / num2
    print(divide)
except Exception as e:
    print(f"Error: {e}")
else:
    print("Division calculated successfully.")
finally:
    print("Database and API connections closed successfully.")

# Custom error

try:
    number = (input("Enter a number which is greater than 5: "))
    if not number.isdigit():
        raise TypeError("The input is not a number type")
    elif int(number) <= 5:
        raise ValueError("The number is not greater than 5")
except Exception as e:
    print(f"Error: {e}")