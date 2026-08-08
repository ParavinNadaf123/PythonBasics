# Write a program to read a file and remove all blank lines before printing.
#
# with open("demo3.txt","r") as f:
#     for line in f:
#         if line.strip() != "":
#             print(line.strip())

# read() + strip() only removes blank lines at the start and end of the file,
# NOT the blank lines in between.
#------------------------------------------------------------------------
# Read a file and count how many times a particular word appears.
# with open("demo1.txt","r") as f :
#     word = "Never"
#     count = 0
#     for w in f :
#         list_of_words = w.split()
#         # print(list_of_words)
#         for item in list_of_words:
#             if item == word:
#                 count += 1
# print("count of word Never: ", count)
#------------------------------------------------------------------------
# Read a file and create a dictionary with word:count pairs.
# 👉 Hint: Use .split()
# with open("demo1.txt","r") as f:
#     dict_of_words_count = {}
#
#     for line in f :
#         words = line.split()
#         for wd in words:
#             wd = wd.strip(",.!?")    # optional cleaning
#
#             if wd in dict_of_words_count:
#                 dict_of_words_count[wd] += 1
#             else:
#                 dict_of_words_count[wd] = 1
# print(dict_of_words_count)


#-------------------------------------------------------------------------------------
# Write a program to display only the lines that contain a specific keyword.
#
# with open("demo3.txt","r") as f :
#     specific_word = "pari"
#     for line in f:
#         if specific_word in line:
#             print(line)



# Write a program to merge two files into a third file.
# #
# with open("demo2.txt","r") as src:
#     with open("demo1.txt","r") as dest:
#         with open("demo3.txt","w") as result:
#
#             for line in src:
#                 result.write(line)
#
#             for line in dest:
#                 result.write(line)
#
# print("File merged  successfully!")



# Write a program to reverse the content of a file.
# 👉 Hint: reverse string or reverse list of lines
# #
# with open("demo1.txt","r") as f :
#     for l in f:
#         rev_data =l[::-1]
#         print(rev_data)
#
# with open("demo1.txt", "r") as f:
#     content = f.read()
#
# reversed_content = content[::-1]
# print(reversed_content)
#/////////////////////////////////////////////////////////////
# with open("demo1.txt", "r") as f:
#     lines = f.readlines()
#
# reversed_lines = lines[::-1]
#
# for line in reversed_lines:
#     print(line.strip())


# Write a program to store even-length words from a file into a separate file.
#
# Approach (in short)
# Open the input file in read mode.
# Open a new output file in write mode
# Read the file line by line.
# Split each line into words.
# For each word:
# Clean punctuation using .strip(",.!?") (optional but useful)
# Check if len(word) % 2 == 0
# If even-length → write it to the output file (add newline or space).
# Close files (automatic with with open()).

#
# with open("demo1.txt", "r") as f:
#     with open("new_file.txt", "w") as n:
#         for line in f:
#             words = line.split()
#             # print(words)
#             for wd in words:
#                 wd = wd.strip(",.!?")  # clean punctuation
#                 # print(wd)
#                 if len(wd) % 2 == 0:
#                     n.write(wd + "\n")   #





# Read a file and print the longest word.
# 👉 Hint: split(), compare lengths
#
# with open("demo1.txt", "r") as f:
#     longest_word = ""
#
#     for line in f:
#         words = line.split()
#         # print(words)
#         for wd in words:
#             wd = wd.strip(",.!?;:-")   # clean punctuation
#             # print(wd)
#             if len(wd) > len(longest_word):
#                 longest_word = wd
# #
# print("Longest word:", longest_word)

# Write a program to check if a file is empty.
# 👉 Hint: check file size
#
import os

file_path = "txt files/new_file.txt"

if os.path.getsize(file_path) == 0:
    print("The file is empty.")
else:
    print("The file is NOT empty.")
  #===========================================================================
with open("txt files/demo1.txt", "r") as f:
    content = f.read().strip()
    if len(content) == 0:
        print("File is empty.")
    else:
        print("File is not empty.")


# Write a program to read a CSV file and display rows one by one.
import csv

with open("csv files/data.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)
