# # Write a Python program to read an entire file and print its contents.
#
# with open("Newfile.txt","r") as f:
#     data = f.read()
#     print(data)
#
# # Write a Python program to read a file line by line.
# with open ("filename1.txt","r") as f:
#    for l in f:
#        print(l.strip())
#
#
# # Write a Python program to count the total number of lines in a file.
# with open("Newfile.txt","r") as f:
#     count = 0
#     for l in f:
#         count += 1
#         l.strip()
#     print("The number of lines",count)
#
#
# # Write a Python program to count the total number of words in a file.
# with open("filename1.txt","r") as f:
#     count_word = 0
#     for words in f:
#         list_of_words = words.split()
#         for l in list_of_words:
#             count_word += 1
#     print("the count of words",count_word)
#
# # Write a Python program to count the total number of characters in a file.
#
# with open("filename1.txt","r") as f:
#     data = f.read()
#
# print("total number of charaters are ",len(data))
#
# # Write a Python program to print only the first 10 characters of a file.
# with open("filename1.txt","r") as f:
#     data = f.read(10)
#     print(data)
#
# # Write a Python program to take user input and write it into a new file.
# user_input = input("Enter the input:")
# with open("filename2.txt","x") as f:
#     f.write(user_input)
#
# # Read from file
# with open("filename2.txt", "r") as f:
#     data = f.read()
#     print(data)
#
#
# # Write a Python program to append text to an existing file.
# with open("filename2.txt","a") as f:
#     f.write("\nI am 33 year old")
#
# with open("filename2.txt", "r") as f:
#     data = f.read()
#     print(data)

# Write a Python program to check whether a file exists before opening it.
import os
filename = "demo.txt"

if os.path.exists(filename):
    with open("demo.txt","r") as f:
        print(f.read())
else:
    print("File not found")

# Write a Python program to write a list of strings into a file (one string per line).
name = ["pari","lata","popo","lala"]
with open("filename2.txt","a") as f:
    for n in name:
        f.write("\n"+ n)

with open("filename2.txt","r") as f:
    print(f.read())

# Write a Python program to copy the contents of one file into another file.

with open("filename1.txt","r") as scr:
    with open("filename2.txt","w") as dest:
        for line in scr:
            dest.write(line)

print("The file copied successfully")

# Write a Python program to rename a file.
import os
old_file = "Newfile.txt"
new_file = "filename3.txt"
if os.path.exists(old_file):
    os.rename("Newfile.txt", "filename3.txt")
else:
    print("File not found")

# Write a Python program to delete a file if it exists.
if os.path.exists("filename3.txt"):
    os.remove("filename3.txt")
else:
    print("File not found")


# Write a Python program to display the size of a file in bytes.
if os.path.exists("filename1.txt"):
    filesize = os.path.getsize("filename1.txt")
    print(filesize)
else:
    print("file not found")


# Write a Python program using with open() to automatically close a file after reading.
with open("filename1.txt","r") as f:
     print(f.read())