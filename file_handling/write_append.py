import csv

# Writing and appending operations

# 1) .write() - write to a file in one go

name = "Alex Smith"
age = 18
city = "Houston"
email = "alexsmith@gmail.com"

with open ("myfile.txt", mode="w", encoding="utf-8") as file:
    data = f"Name: {name}\nAge: {age}\nCity: {city}\nEmail: {email}\n"
    file.write(data)

# 2) .write() + append()

name1 = "Brian Smith"
age1 = 20
city1 = "Dallas"
email1 = "brians@gmail.com"

with open ("myfile.txt", mode="a", encoding="utf-8") as file:
    data = f"Name: {name1}\nAge: {age1}\nCity: {city1}\nEmail: {email1}\n"
    file.write(data)

# 3) .writeline()/.writelines() - Helps to write a line/lines through an iterator like list

people = ["Name: Brian Daniels\nAge: 15\nCity: Alberta\nEmail: briandaneil15@yahoo.com\n", "Name: Chandan Singh\nAge: 17\nCity: Austin\nEmail: chandansing17@yahoo.com\n"]

with open ("myfile.txt", mode="a", encoding="utf-8") as file:
    file.writelines(people)

# 4) Writing in a .csv file

rows = [
    ["Name", "Age", "City", "Email"],
    [name, age, city, email],
    [name1, age1, city1, email1]
]

with open ("myfile.csv", mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)