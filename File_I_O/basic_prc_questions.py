# ✅ Basic Level
#
# Write a Python program to read an entire file and print its content.
#
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)
# Write a program to read a file line by line.
#
# with open("demo.txt","r") as f:
#     for l in f :
#         print(l.strip()) #Use .strip() to remove the extra newline when printing.
# Write a program to count how many lines a file contains.
#
# with open("practice_question","r") as f:
#     count = 0
#     for l in f:
#         count += 1
#         print(l.strip())
#     print("no of lines",count)
# Write a program to write user input into a file (create a new file).
#
# with open("demo2.txt","w") as f:
#     txt = input("Enter the txt: ")
#     f.write(txt)
#     print(txt)
import os

# Write a program to append a new line to an existing file.
#
# with open("demo2.txt","a") as f:
#     txt = input("Enter the txt: ")
#     f.write("\n" + txt)
#     print(txt)

# Write a program to check if a file exists or not before reading it.
#
import os
#
# filename = "demo.txt"
#
# if os.path.exists(filename):
#     with open(filename, "r") as f:
#         print(f.read())
# else:
#     print("File not found!")

# Write a program to write a list of strings into a file (each string on a new line).
#
# with open("demo1.txt","w") as f:
#     str_list = ["Go","With","Flow"]
#     for s in str_list:
#         # f.write("\n" +s)
#         f.write(s + "\n")
#         print(s)
#

# Write a program to read a file and print only the first 10 characters.
#
# with open("demo1.txt","r") as f:
# #     data = f.read(10)
# #     print(data)
# # Write a program to find how many words are there in a text file.
# with open("demo2.txt","r") as f:
#     count_of_words = 0
#     for c in f :
#         list_of_words = c.split()
#         # print(list_of_words)
#         for l in list_of_words:
#             count_of_words += 1
#             print(l)
#     print("no of words",count_of_words)

#
# Write a program to copy content from one file into another file.

with open("txt files/demo2.txt", "r") as src:
    with open("txt files/demo3.txt", "w") as dest:
        for line in src:
            dest.write(line)

print("File copied successfully!")

