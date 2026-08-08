# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")
# data = f.read(10) #only to read startting 10 characters
# print(data)
# f.close()
#
#to read starting line

f = open("txt files/demo.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
f.close()

# writing in the file
# w - overwrites the entire file
#a - adds to the file

f = open("txt files/demo1.txt", "w")
f.write("Paravin here")
f.close()

f = open("txt files/demo1.txt", "a")
f.write("\nI am learing python")
f.close()

try:
    f = open("sample.txt","r")
    f.close()
except FileNotFoundError as msg:
    print("No such file or directory: 'sample.txt'")

f = open("sample.txt","w")
f.close()

# r+ - read and overwrite , pointer is at starting and no truncate
# w+ - read and overwrite ,  data gets truncate
# a+ - read and append , pointer at the end , no truncate

#with syntax
#using with syntax no need to close the file as it will automatically closes the file
with open("sample.txt","r") as f:
    data = f.read()

with open("sample.txt","w") as f:
    f.write("Hi Hello")

import os
os.remove("sample.txt")