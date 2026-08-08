#🔁 1. For Looping Through a String

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#
# for x in "banana":
#   print(x)
# # Write a program that prints each character of the string "Python".
#
# char= "python"
#
# for x in char:
#     print(x)

# # Count and print how many vowels are in a given string.
# input_str = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
#
# for char in input_str:
#     if char in vowels:
#         print(char)
#         count += 1
#
# print("Number of vowels:", count)
#
#
# #Print the index and character of each letter in the string "Developer".
# i=0
# str_1= "Developer"
# for char in str_1:
#
#     print(i,char)

# Check if a string is a palindrome using a for loop.
#
# word = str(input("Enter the string : "))
# word2 = word[::-1]
# if word2 == word:
#     print(f"Its a polindrome, {word2}={word}")
# else:
#     print("Its not polindrome")
# # ****************************************************************************
# input_str  = str(input("Enter the string :"))
# lenght_of_input_str = len(input_str)
# is_palindrome = True
#
# for i in range(lenght_of_input_str // 2):
#     if input_str[i] != input_str[lenght_of_input_str - 1 - i]:
#         is_palindrome = False
#         break
#
# if is_palindrome:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# Skip printing elements in a list that are divisible by both 2 and 3.
#
# marks=[88,22,44,21,56,98,12,18,6]
#
# for i in marks:
#     if (i % 2 == 0) and (i % 3 == 0):
#         continue
#     print(i)

# Write a function that returns the number of uppercase and lowercase letters in a string.
# upper_count = 0
# lower_count = 0
# name = str(input("Enter the name :"))
# for char in name :
#     if char.isupper():
#         upper_count +=1
#
#     if char.islower():
#         lower_count +=1
#
# print("The count of uppercase letter",upper_count)
# print("The lowercase letter numbers :",lower_count)

# Reverse a string using a for loop without using slicing
#
# input_str = str(input("Enter the string :"))
# reversed_str = ""
# for char in input_str:
#     reversed_str = char + reversed_str
# print(reversed_str)
# # ==============================Given a string with multiple words, count the frequency of each character.
# input_str = input("Enter a string: ")
# char_freq = {}
#
# for char in input_str:
#     if char in char_freq:
#         char_freq[char] += 1
#     else:
#         char_freq[char] = 1
#
# for char, count in char_freq.items():
#     print(f"{char}: {count}")


# input_sentence = ("Mr Paraveensultan refused to answer any questions")
# split_sent = input_sentence.split()
# # print(split_sent)
# longest_word= ""
# for word in split_sent:
#    if len(word) > len(longest_word):
#        longest_word = word
#
# print(f"the longest word is {longest_word}")

# Implement a basic string compression algorithm (e.g., "aabcc" → "a2b1c2"

# 💡 Hints:
# Use a loop to go through each character in the string.
#
# Track the current character and how many times it repeats in a row.
#
# When the character changes, append the character + count to the result string.
#
# # At the end, don’t forget to add the last character group.
#
# def compress_string(s):
#     if not s:
#         return ""
#
#     compressed = ""
#     count = 1  # Start count at 1 for the first character
#
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed += s[i - 1] + str(count)
#             count = 1  # Reset count for the new character
#
#     # Add the last character group
#     compressed += s[-1] + str(count)
#
#     return compressed
#
# # Test
# input_str = str(input("Enter the string : "))
# print("Compressed string:", compress_string(input_str))

# # Print vowels
# word = input("Enter the string : ")
# vowels = "aeiouAEIOU"
#
# for char in word:
#     if char in vowels:
#         print(char)

#count the vowels

# word = input("Enter the string :")
# vowels = "aeiouAEIOU"
# count = 0
# for  char in word:
#     if char in vowels:
#         print(char)
#         count +=1
#
# print("The count of vowels",count)


# Count uppercase
# count=0
# word = input("Enter the string :")
# for l in word:
#     if l.isupper():
#         print(l)
#         count+=1
#
# print("The count of upper case letter",count)
#
# word = input("Enter the string : ")
# vowels = "aeiouAEIOU"
# new_word=""
# for char in word:
#     if char in vowels:
#         new_word += "*"
#     else:
#         new_word += char
#
# print("Modified string:", new_word)

#
# name = input("enter the string :")
# index_count=0
# for i in name:
#     print(i, index_count)
#     index_count += 1
#
# name = input("enter the string :")
# reverse_name=""
# for char in name:
#     reverse_name = char + reverse_name
#
#
# print(reverse_name)

# num = [9,8,33,76,99,111,298]
# count = 0
# for n in num:
#     if n %2 ==0:
#         print("the even number is",n)
#         count +=1
#
# print("The even numbers in the list are",count)


# word = input("enter the string :")
# new_word=""
# v = "aeiouAEIOU"
# for char in word:
#     if char not in v:
#         new_word += char
#
# print(new_word)


# num = int(input("Enter the  number :"))
# sum=0
# while num > 0:
#     last_num = num % 10
#     sum = sum + last_num
#     num = num // 10
# print("The sum of digit",sum)


# num1 = int(input("Enter the  number :"))
# fact = 1
# for i in range(1,num1+1):
#     fact = fact*i
#
# print(f"The factorial of {num1} is ",fact)

