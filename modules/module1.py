def addition(*args):
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum

def subtraction(a, b):
    return a - b

def multiplication(*args):
    total_product = 0
    for num in args:
        total_product *= num
    return total_product

def division(a, b):
    try:
        div = a / b
        return div
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Testing functions with value 10 and 20")
    call_add = addition(10, 20)
    call_sub = subtraction(10, 20)
    call_mult = multiplication(10, 20)
    call_div = division(10, 20)
    print(addition.__name__, call_add)
    print(subtraction.__name__, call_sub)
    print(multiplication.__name__, call_mult)
    print(division.__name__, call_div)