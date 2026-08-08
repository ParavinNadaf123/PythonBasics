# Read a large file (1GB+) without loading the entire content into memory.
# 👉 Hint: iterate line by line
# with open("test_data.txt","r") as file:
#     for line in file:
#         print(line.strip()) #strip() to remove extra newline

# Write a program to remove duplicate lines from a file.
# 👉 Hint: use a set
# seen_set_data = set()
# with open("demo1.txt","r") as scr:
#     with open("demo2.txt","w") as des:
#         for line in scr:
#             print(line.strip())
#             if line not in seen_set_data:
#                 des.write(line)
#                 seen_set_data.add(line)
#
# Read a file and create a frequency count for each character (including spaces).
# freq = {}
# with open("demo2.txt","r") as f:
#         for line in f:
#             for ch in line:
#                 if ch in freq:
#                     freq[ch] += 1
#                 else:
#                     freq[ch] = 1
#
# print(freq)


#
# Write a program to compare two files and check if their contents are identical.
# 👉 Hint: compare line by line
# #
# with open("demo1.txt", "r", encoding="utf-8") as f1, \
#      open("demo2.txt", "r", encoding="utf-8") as f2:
#
#     same = True
#
#     for line1, line2 in zip(f1, f2):
#         if line1 != line2:
#             same = False
#             break
#
#     # check for extra leftover lines
#     if same and (f1.read() or f2.read()):
#         same = False
#
# if same:
#     print("Files are identical")
# else:
#     print("Files are different")

#
#
#
# with open("demo1.txt", "r", encoding="utf-8") as f1, \
#      open("demo2.txt", "r", encoding="utf-8") as f2:
#
#     if f1.read() == f2.read():
#         print("Files are identical")
#     else:
#         print("Files are different")
#
#
# Write a program that logs every program execution into a log file with timestamps.
#
# from datetime import datetime
#
# with open("demo3.txt", "a") as f:
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     f.write(f"{timestamp} - Program executed\n")

# Write a program to read a JSON file and print specific fields (e.g., name, age).
import json
import os.path

# with open("data.json","r") as f:
#     data = json.load(f) # converts JSON → Python dict
#
# print("Name:", data.get("name"))
# print("Age:", data.get("age"))
# print("City:",data.get("city"))
# #
# Convert contents of a text file into a JSON file.
# 👉 Hint: Build a dict and dump with json
#
# with open("demo3.txt","r") as f:
#     lines = f.read().splitlines()
#     # print(lines)
#
# data = {
#     "content" : lines
# }
#
# with open("output.json","w") as json_file:
#     json.dump(data,json_file,indent= 4)
#
# print("Text converted to JSON successfully!")

# Write a program to validate that a CSV file has a specific number of columns in every row.
#
# import csv
# req_col = 10
# with open("customers-100.csv","r") as f:
#     reader = csv.reader(f)
#
#     for idx, row in enumerate(reader, start=1):
#         if len(row) == req_col:
#             print(f"Row {idx}: VALID")
#         else:
#             print(f"Row {idx}: INVALID (Found {len(row)} columns)")
# Write a program to split a big file into 5 small files of equal size.
# 👉 Hint: calculate chunk size
## Split a big file into 5 smaller files

num_parts = 5
file_name = "txt files/bigfile.txt"

# 1. Find total size of the file (in bytes)
# file_size = os.path.getsize(file_name)

# 2. Calculate chunk size = total_size / 5
# chunk_size = file_size // num_parts

# with open(file_name, "rb") as src:     # read in binary mode
#     for i in range(1, num_parts + 1):
#         with open(f"part_{i}.txt", "wb") as dst:
#
#             # Last file should take all remaining bytes
#             if i == num_parts:
#                 dst.write(src.read())      # read EVERYTHING left
#             else:
#                 dst.write(src.read(chunk_size))
#
# print("File split completed!")

# Write a program to read a file and find the most repeated word.
# 👉 Hint: dictionary + max()

from collections import Counter
import re

# Read file
with open("txt files/bigfile.txt", "r") as f:
    text = f.read().lower()          # convert to lowercase for uniform counting

# Extract words using regex (removes punctuation)
words = re.findall(r"\b[a-zA-Z]+\b", text)

# Count word frequencies
word_count = Counter(words)

# Find the most common word
most_common_word, frequency = word_count.most_common(1)[0]

print("Most repeated word:", most_common_word)
print("Frequency:", frequency)
