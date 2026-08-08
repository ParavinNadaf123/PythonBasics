# # Write a Python program to search for a specific word in a file.
# from While_Loops.while_loop2 import count
#
# with open("filename1.txt","r") as f:
#     data = f.read()
#     word_to_check = "Never"
#     if word_to_check in data:
#         print(f"The word {word_to_check} to check is present")
#     else:
#         print(f"Word {word_to_check} is not found")

# Write a Python program to count how many times a particular word appears in a file.
#
# import re
#
# with open("filename1.txt", "r") as f:
#     data = f.read().lower()
#
# words = re.findall(r"\b[a-zA-Z]+\b", data)
#
# word_to_check = "never"
#
# count_of_word = 0
#
# for word in words:
#     if word == word_to_check:
#         count_of_word += 1
#
# print(f"Count of '{word_to_check}' is {count_of_word}")

# # Write a Python program to replace all occurrences of a word with another word in a file.
# with open("filename1.txt","r") as f:
#     data= f.read()
#     old_word = "july"
#     new_word = "June"
#     modified_data = data.replace(old_word,new_word)
#
# with open("filename1.txt","w") as f:
#     f.write(modified_data)
#
# print("Replacement compeleted")


# Write a Python program to remove duplicate lines from a file.
# seen_set_data = set()
# with open("filename1.txt","r") as scr:
#     with open("filename2.txt","w") as des:
#             for line in scr:
#                 if line not in seen_set_data:
#                     des.write(line)
#                     seen_set_data.add(line)


# Write a Python program to remove blank lines from a file.

# Remove blank lines from a file

# with open("filename1.txt", "r") as f:
#     lines = f.readlines()
#
# with open("filename1.txt", "w") as f:
#     for line in lines:
#         if line.strip():      # Keep only non-blank lines
#             f.write(line)
#
# print("Blank lines removed successfully!")

# Write a Python program to display only the lines containing a specific keyword.
# with open("filename1.txt","r") as f:
#     lines = f.readlines()
#     specific_keyword = "get"
#     for line in lines :
#         if specific_keyword in line:
#             print(line.strip())
#
#
# # Write a Python program to read only the odd-numbered lines of a file.
# with open("filename1.txt","r") as f:
#     counter = 1
#     for line in f:
#         if counter % 2!= 0:
#             print(line.strip())
#         counter += 1
#
# # Write a Python program to read only the even-numbered lines of a file.
# with open("filename1.txt","r") as f:
#     counter_even = 1
#     for lines in f:
#         if counter_even %2 ==0:
#             print(lines.strip())
#         counter_even +=1

# Write a Python program to display the last five lines of a file.
# with open("filename1.txt") as f:
#     lines = f.readlines()
#     for line in lines[-5:]:
#         print(line.strip())
# Write a Python program to display the longest line in a file.
# with open("filename1.txt","r") as f:
#     lines = f.readlines()
#     longest_line = ""
#     for line in lines :
#         # print(line.strip())
#         if len(line) > len(longest_line):
#             longest_line = line
#
# #     print(longest_line)
#
# # Write a Python program to display the shortest line in a file.
# with open("filename1.txt","r") as f:
#     lines = f.readlines()
#     shortest_line = lines[0]
#     for line in lines:
#         if len(line) < len(shortest_line):
#             shortest_line = line

# print(shortest_line.strip())

# Write a Python program to sort all lines in a file alphabetically.
# with open("filename1.txt","r") as f:
#     lines  = f.readlines()
#     lines.sort()

# with open("filename1.txt","w") as f:
#     f.writelines(lines)
#
# print("file sorted successfully")

# Write a Python program to reverse the contents of a file.
# with open("filename1.txt","r") as f:
#     data = f.read()
#     rev_data = data[::-1]
#     print(rev_data.strip())

# with open("filename1.txt","w") as f:
#     f.write(rev_data.strip())
# # Write a Python program to merge two text files into a third file.
# with open("filename1.txt","r") as f:
#     data1 = f.read()
#     with open("filename2.txt","r") as f1:
#         data2 = f1.read()
#         data3 = data1 + data2
#         with open("filename3.txt","w") as f2:
#             f2.write(data3)


# Write a Python program to compare two files and check whether their contents are identical.
# with open("filename1.txt","r") as f:
#     data = f.read()
#     with open("filename2.txt","r") as f1:
#         data1 = f1.read()
#         if data == data1:
#             print("their contents are identical.")
#         else:print("their contents are non identical.")
#
#
# with open("filename1.txt","r") as f:
#     data = f.read()
#     with open("filename3.txt","r") as f1:
#         data1 = f1.read()
#         if data == data1:
#             print("their contents are identical.")
#         else:print("their contents are non identical.")

# Write a Python program to create a backup copy of a file before modifying it.
# with open("filename2.txt","r") as f:
#     data = f.read()
#
#
# with open("filename4.txt","x") as n:
#     n.write(data)
#
# with open("filename2.txt","w") as f1:
#     f1.write("Wishes matter, even when unseen")

# Write a Python program to count the frequency of each character in a file.
# with open("filename2.txt","r") as f:
#     data = f.read()
#     freq_of_char = {}
#
#     for char in data:
#         if char in freq_of_char:
#             freq_of_char[char] += 1
#         else:
#             freq_of_char[char] = 1
#
#     print(freq_of_char)
# Write a Python program to count the frequency of each word in a file.

# with open("filename4.txt","r") as f:
#     data = f.read()
#     words= data.split()
#     freq_of_word = {}
#
#     for word in words:
#         if word in freq_of_word:
#             freq_of_word[word]+= 1
#         else:
#             freq_of_word[word]=1
#
#     print(freq_of_word)
# Write a Python program to find the most frequently occurring word in a file.
with open("../textFiles/filename4.txt", "r") as f:
    data = f.read()
    words = data.split()
    freq={}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] =1

    most_common_word = ""
    highest_count = 0


    for  word ,count in freq.items():
        if count > highest_count:
            highest_count = count
            most_common_word = word

    print("Most frequent word:", most_common_word)
    print("Frequency:", highest_count)
# Write a Python program to display the top five most frequently occurring words in a file.
with open("../textFiles/filename4.txt", "r") as f:
    data = f.read()

# Convert text into words
words = data.split()

# Dictionary to store word frequencies
freq = {}

# Count frequency of each word
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Convert dictionary into a list of (word, count) tuples
word_list = list(freq.items())

# Sort the list by frequency (highest first)
word_list.sort(key=lambda x: x[1], reverse=True)

# Display the top 5 words
print("Top 5 Most Frequent Words:\n")

for word, count in word_list[:5]:
    print(f"{word} : {count}")