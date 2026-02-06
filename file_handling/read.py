import csv

# File Operations
"""
File Operations-basically mean: opening a file, reading it, writing it and closing it safely.
Different kind of files:-
# I. Regular files like .txt, .csv's
## Below mention files are treated as Binary files for raw operations...
# II. Image file - Pillow Module
# III. Audio file- pyaudio Module
# IV. Video files like .mp4 - FFMPEG python extensions
"""
# Ist Operation - Reading a file (mode="r")
"""
1. with
with is called context manager.
It is used to set something up, use it, then clean it up automatically.
2.open
Helps up opening a file in Python.
We can open file in different modes, depending on the problem:-
"r"- read(file must exist)
"w"- write(creates new file or overwrite everything) 
"a"- append (adds to end; create new file if not exits)
"x"- create (fails if the file already exists)
"""

# Old/traditional way

my_file = open("wildlife.txt", mode="r", encoding="utf-8")
file_info = my_file.read()
# print(file_info)
my_file.close()

# Modern approach - using context manager (with keyword)

with open("wildlife.txt", mode="r", encoding="utf-8") as file:
    file_info = file.read()

# print(file_info)

# All possible methods for reading a file

# 1) read() function - stores the entire file as a single string

with open("wildlife.txt", mode="r", encoding="utf-8") as file:
    content = file.read()

print(type(content))

# 2) Extracting only a portion of the text

with open("wildlife.txt", mode="r", encoding="utf-8") as file:
    content1 = file.read(100) # first 100 char
    content2 = file.read(50) # next 50 char
    content3 = file.read(50)

print(content1, content2, content3, sep=" | ")

# 3) readline()/readlines() - readline() reads a single line while readlines() will read line by line, result is stored as a list

with open("python.txt", mode="r", encoding="utf-8") as file:
    content = file.readline()

print(content)

with open("python.txt", mode="r", encoding="utf-8") as file:
    contents = file.readlines()

# print(contents, type(contents))

# 4) For loop for extracting text

with open("wildlife.txt", mode="r", encoding="utf-8") as file:
    myContent = []
    for line in file:
        myContent.append(line.strip())

# print(myContent)

# 5) While loop for extracting text

with open("wildlife.txt", mode="r", encoding="utf-8") as file:
    myContent2 = []
    chunk = file.read(50)
    while chunk:
        myContent2.append(chunk.strip())
        chunk = file.read(50)

print(myContent2)

# 6) Reading a .csv file]

with open ("Metal_data.csv", mode="r", encoding="utf-8") as file:
    myCSV = []
    reader = csv.DictReader(file)
    for row in reader:
        myCSV.append(row)

print(myCSV)