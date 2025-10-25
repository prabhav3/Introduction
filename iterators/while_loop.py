# While loop runs while a condition is true, and when the condition becomes false, the loop stops its execution
# We use while loop when we have undetermined range

"""
while True:
    print("You are stuck in this while loop forever")
"""

while False:
    print("This while loop will not work")

# Conditions for running the while loop

# Illustration 1: Running while loops from 0-9 and 1-10

count = 0

while count < 10:
    print(count, end=" ")
    count += 1

print()
count = 1

while count <= 10:
    print(count, end=" ")
    count += 1

print()

# Illustration 2: Running while loop for multiple conditions

# We have 2 variables: x = y = 0, x increments until 10, and the y will decrement until -5. Run a while loop for the composite condition.
# Composite condition until one of the variables exceeds its limit

x = y = 0

while x <= 10 and y >= -5:
    print(f"{x=} {y=}")
    x += 1
    y -= 1

print()

# Illustration 3: Creating a negative counter

# NASA style counter

count_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

counter = 10

while counter:
    print(count_dict[counter])
    counter -= 1

print()

# Break and continue

while True:
    choice = input("Enter any key to see magic, press 1 not to see it, and press 2 to stop the loop: ").strip()
    if choice == "1":  
        continue
    elif choice == "2":
        break
    print("Abracadabra ✨🎇")

print()

# Running while loops with strings

# Illustration 1: Reversing a string

string_1 = "Hello World"

reversed_string = ""

index = 0

while index < len(string_1):
    reversed_string = string_1[index] + reversed_string
    index += 1

print(f"The reverse of {string_1} is {reversed_string}")

index = -1

reversed_string = ""

while index >= -len(string_1):
    reversed_string += string_1[index]
    index -= 1

print(f"The reverse of {string_1} is {reversed_string}")

# Illustration 2: find the number of words in a paragraph using while loop

paragraph = "This is a sample paragraph. It has multiple sentences. Each sentence has multiple words."

word_count = 1 if len(paragraph) else 0  # Start with 1 if paragraph is not empty

counter = 0

while counter < len(paragraph):
    if paragraph[counter] == " ":
        word_count += 1
    counter += 1

print(f"The paragraph has {word_count} words.")

# Illustration 3: Highlight the word tiger in a paragraph each time it occurs with a color of your choice

paragraph = "Tigers are the largest members of the cat family and are renowned for their power, grace, and striking appearance. With bold black stripes over a fiery orange coat, each tiger’s pattern is as unique as a fingerprint. Native to Asia, they thrive in diverse habitats—from dense jungles to snowy forests. Tigers are solitary hunters, relying on stealth and strength to ambush prey like deer and wild boar. Sadly, their numbers have dwindled due to habitat loss and poaching, making conservation efforts critical. Despite their fierce reputation, tigers play a vital role in maintaining the balance of their ecosystems, symbolizing both beauty and strength in the wild."

highlighted_paragraph = ""

paragraph_list = paragraph.split()

index = 0

while index < len(paragraph_list):
    word = paragraph_list[index]
    if "tiger" in word.lower():
        highlighted_paragraph += f"\033[93m{word}\033[0m "
    else:
        highlighted_paragraph += word + " "
    index += 1

print(highlighted_paragraph)

print()
print("----------------------------------------------------------------------")
print("-----------------------While Loops and Tuples-------------------------")
print()

# Illustration 1: Modify a list by keeping only the perfect square in it

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

index = 0

while index < len(numbers):
    sqrt = int(numbers[index] ** 0.5)
    if sqrt * sqrt != numbers[index]:
        numbers.pop(index)
    else:
        index += 1

print(f'The perfect squares from the list are {numbers}')

# Illustration 2: Making a list unique (dropping all the duplicates)

fruit_list = ["apples", "bananas", "oranges", "apples", "oranges", "bananas", "grapes", "apples", "oranges", "passionfruit", "oranges", "bananas", "passionfruit", "grapes", "kiwi"]

index = 1 if len(fruit_list) else 0

while index < len(fruit_list):
    fruit = fruit_list[index]
    if fruit in fruit_list[:index]:
        fruit_list.pop(index)
    else:
        index += 1

print(f"The unique fruits in the list are {fruit_list}")

# Illustration 3: Find the maximum and minimum number in a tuple using a while loop

numbers_tuple = (1, 12, 19, 34, 44, 56, 74)

index = 0

max_num = float('-inf')

min_num = float('inf')

while index < len(numbers_tuple):
    current = numbers_tuple[index]
    if current > max_num:
        max_num = current
    if current < min_num:
        min_num =  current
    index += 1

print(f"The maximum number in the tuple is {max_num} and the minimum number is {min_num}")