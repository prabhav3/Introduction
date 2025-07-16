# Membership operator: in
# The membership operator helps to check for substrings, items in a list, tuples, and key in dictionary

my_string = "Jakarta Miami Dahka Venice New Delhi are hotspots of global warming"
city = "ice N"

if city.lower() in my_string.lower():
    print(F"{city} is a hotspot for global warming")
else:
    print(F"{city} is not a hotspot for global warming")

cities_list = ["Jakarta", "Miami", "Dahka", "Venice", "New Delhi"]
city = "El Paso"

if city in cities_list:
    print(F"{city} is a hotspot for global warming")
else:
    print(F"{city} is not a hotspot for global warming")

info_dict = {"name": "Alex", "age": 14, "grade": 8}

key = "name"

if key in info_dict:
    print(f"{key} is present in the dictionary. Its value is {info_dict[key]}")
else:
    print(f"{key} is not present in the dictionary.")

# Identity operator: is
# Identity operator helps to check if two variables share the same memory location or not

var_a = "Hello"
var_b = "Hello"

print(id(var_a), id(var_b), var_a is var_b)

var_b += "World"

print(id(var_a), id(var_b), var_a is var_b)

cities_list = ["Jakarta", "Miami", "Dahka", "Venice", "New Delhi"]
cities_list_2 = ["Jakarta", "Miami", "Dahka", "Venice", "New Delhi"]

print(id(cities_list), id(cities_list_2), cities_list is cities_list_2)

cities_copy = cities_list

print(id(cities_list), id(cities_copy), cities_list is cities_copy)

cities_copy.append("Houston")
cities_list.pop(0)

print(cities_copy, cities_list)

# Assignment operators: =, +=, -=, *=, /=, //=
# for variable a_var, increase its value by 5 three times, subtract 2 from it four times, and multiply it by 1.5 three times

a_var = 10
a_var += 5
a_var += 5
a_var += 5
a_var -= 2
a_var -= 2
a_var -= 2
a_var -= 2
a_var *= 1.5
a_var *= 1.5
a_var *= 1.5

print(f"The final value of a_var is {a_var}")