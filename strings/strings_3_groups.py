import string

# String functions/methods

# Group 1: Case modifier functions
# The main functions are: .upper(), .lower(), .title(), .capitalize(), .casefold()

string_1 = "hEllo WoRlD"
print("Default:    ", string_1)
print("Lowercase:  ", string_1.lower())
print("Uppercase:  ", string_1.upper())
print("Title:      ", string_1.title())
print("Capitalize: ", string_1.capitalize())

print()

# Casefold is mostly used for comparison and to not get confused with lower/upper
print("Hello World" == "hElLo WoRlD")
print("Hello World".casefold() == "hElLo WoRlD".casefold())

print()
print("---------------------------------------------------------------------------------")
print()

# Group 2: Is x functions
# The main functions are: .isalnum(), .isalpha(), .isdigit(), .isspace()

# .isalnum() checks if the string contains only alphanumerical characters, not case sensitive

string_2 = "dshi21kp23"
string_3 = "@8973asdasd"
print(string_2.isalnum(), string_3.isalnum())
print()

# .isalpha() checks for only alphabetical characters, not case sensitive

string_4 = "abcdEFGHIJKlmnop"
print(string_4.isalpha(), string_2.isalpha())
print()

# .isdigit() checks if the string contains only numbers (digits), decimals are excluded because of "."

string_5 = "3495830"
string_6 = "3495.83"
print(string_5.isdigit(), string_6.isdigit())
print()

# .isspace() checks if the string only contains spaces or space characters

string_7 = " "
string_8 = " \n   \t" # \b is not considered a space character because it removes the previous character
print(string_7.isspace(), string_8.isspace())

print()
print("---------------------------------------------------------------------------------")
print()

# Group 3: Converting strings into lists and vice versa
# The two functions are: .split(), .join()

# .split() splits a string into a list by separating the portions of the string separated by a character that defaults to " "

string_9 = "Hello and welcome to the world of Python"
string_10 = "Hello-and-welcome-to-the-world-of-Python"
print(string_9.split(" "))
print(string_10.split(), string_10.split("-")) # only works with correct character(s)

# .join() joins items in a list together to form a string

list_1 = ['Hello', 'and', 'welcome', 'to', 'the', 'world', 'of', 'Python']
string_11 = "".join(list_1)
print(string_11)
string_12 = " ".join(list_1)
print(string_12)
string_13 = "-".join(list_1)
print(string_13)

print()
print("---------------------------------------------------------------------------------")
print()

# Group 4: Strip group - remove the trailing and leading whitespace
# The functions are: .strip(), .rstrip(), .lstrip()

# Remove whitespace
string_14 = "                Hello world        "
print("-->" + string_14 + "<--")
print("-->" + string_14.strip() + "<--")
print("-->" + string_14.rstrip() + "<--")
print("-->" + string_14.lstrip() + "<--")

# Remove specific characters
string_15 = "../!%$99@)}]445222##$4#_)(@#(@!?)hello world....???!!"
print("-->" + string_15 + "<--")
print("-->" + string_15.strip(string.digits + string.punctuation) + "<--")
print("-->" + string_15.rstrip(string.digits + string.punctuation) + "<--")
print("-->" + string_15.lstrip(string.digits + string.punctuation) + "<--") 

print()
print("---------------------------------------------------------------------------------")
print()

# Group 5: Checking prefix/suffix
# The main functions are: .startswith(), .endswith(), .removeprefix(), .removesuffix()

# .startswith() check if a string starts with a particular character(s)
string_16 = "Hello World"
print(string_16.startswith("H"), string_16.startswith("h"))
print(string_16.startswith("Hello"), string_16.startswith("hello"))
print(string_16.startswith(("Hola", "Hello", "Bonjour")), string_16.startswith(("hola", "hello", "bonjour")))

# .endswith() check if a string ends with a particular character(s)
print(string_16.endswith("d"), string_16.endswith("D"))
print(string_16.endswith("world"), string_16.endswith("World"))
print(string_16.endswith(("Mundo", "World", "Monde")), string_16.endswith(("mundo", "world", "monde")))

# .removeprefix() removes the desire character(s) at the beginning of the string
print(string_16.removeprefix("H").capitalize(), string_16.removeprefix("Hello"))

# .removesuffix() removes the desire character(s) at the end of the string
print(string_16.removesuffix("d"), string_16.removesuffix("World"))

print()
print("---------------------------------------------------------------------------------")
print()

# Group 6: index counting and modifiers
# The main functions are: .index(), .count(), .replace()

# .index() the first index of the desired character(s) of the substring
string_17 = "Paris is a great city. I visited Paris last summer."
print("First occurrence of \"Paris:\"", string_17.index("Paris"))
print("Second occurrence of \"Paris:\"", string_17.index("Paris", 1, len(string_17)))

# .count() helps count character(s), digit(s), or whitespace(s)
print(string_17.count("Paris"))
print(string_17.count(" ") + "," + string_17.count("e"))