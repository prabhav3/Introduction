def gcf(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def lcm(num1, num2):
    return (num1 * num2) // gcf(num1, num2)