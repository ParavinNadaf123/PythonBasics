# # 1.	Write a program that prints each character of the string "Python".
#
# a = "python"
#
# for c in a:
#     print(c)

    # 2.	Count and print how many vowels are in a given string.

# name = "Entertainment"
# vowels = ["a","e","i","o","u","A","E","I","O","U"]
# count_of_vowels = 0
# for c in name:
#     if c in vowels:
#         count_of_vowels = count_of_vowels +1
#         print(c)
# print("The count of vowels in str :",count_of_vowels)

# 3.	Print the index and character of each letter in the string "Developer".

#
# i=0
# str_1= "Developer"
# for char in str_1:
#     print(i,char)
#     i += 1

# 4.	Check if a string is a palindrome using a loop.

# str = "APPA"
# rev_str = str[::-1]
# print(rev_str)
# if str == rev_str:
#     print("The srting is palindrome")
# else:
# #     print("Not a palindrome")
#
# word = input("Enter the string: ")
#
# length = len(word)
# is_palindrome = True
#
# for i in range(length // 2):
#     if word[i] != word[length - 1 - i]:
#         is_palindrome = False
#         break
#
# if is_palindrome:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")


    # 5.	Reverse a string without using slicing.

str = "Paravin"
rev_str = " "
for i in str:
    rev_str = i + rev_str
print(rev_str)

# 6.	Replace all vowels in a string with "*".

str = "zeeshan"
vowels = ["a","e","i","o","u","A","E","I","O","U"]
new_str = ""
for i in str:
    if i  in vowels:
        new_str += "*"
    else:
        new_str += i

print(new_str)

#
# word = input("enter the string :")
# new_word=""
# v = "aeiouAEIOU"
# for char in word:
#     if char not in v:
#         new_word += char
#
# print(new_word)

# 8.	Print only the vowels from a given string.

strg =  input("enter the string :")
vowels = "aeiouAEIOU"
new_strg = ""
for i in strg:
    if i in vowels:
        new_strg += i

print("The vowels present in string: ",new_strg)

# 9.	Count the number of uppercase and lowercase letters in a string.

strg =  input("enter the string :")
upper_letter= ""
lower_letter =""
count_upper= 0
count_lower = 0
for char in strg:
    if char.isupper() :
        upper_letter += char
        count_upper += 1
        # print("The upper letter :",upper_letter)
    elif char.islower() :
        lower_letter += char
        count_lower += 1
        # print("The lower letter :",lower_letter)

print(f"The count of lower letter {count_lower} and count of upper letter {count_upper} ")
print(f"The Lower letter are {lower_letter} and The Upper letter are {upper_letter}")


strg =  input("enter the string :")
char_freq = {}

for char in strg:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

for char, count in char_freq.items():
    print(f"The character {char} and its frequency {count}")

input_sentence = ("Mrs Paraveensultan refused to answer any questions")
split_sentence = input_sentence.split()
print(split_sentence)
longest_word = ""
for w in split_sentence:
    if len(w) >len(longest_word):
        longest_word = w
print(f"The longest words is {longest_word}")
