import random

def random_integer(a, b):
    return random.randint(a, b)

def random_picker(sequence):
    try:
        length = len(sequence) - 1
        return sequence[random.randint(0, length)]
    except Exception as e:
        print(f"Error: {e}")