# # #slicing string
# #
# txt = "hello, World!"
#
# print(len(txt))
# #
# print(txt[0:5])
# print(txt[:6])
# # print(txt[7:])
# # print(txt[5:])
# print(txt[-6:-1:2])
# print(txt[::-1])
# # print(txt[-6])
# # print(txt[-1])
# # #
# # print(txt[::-1])
# # print(txt[:-6:-1])
#
# # print(txt[-6])
# #
# # #modify string
# #
# # Movie_title = "Dhoom machale"
# #
# # print(Movie_title.upper())
# # print(Movie_title.lower())
# # print(Movie_title.title())
# #
# # print(Movie_title.swapcase())
# #
# #
# # #############sTRING TESTING ############
# #
# # print("123".isdigit())
# # print("abc".isalnum())
# # print("ACII".isascii())
# # print(" ".isspace())
#
# # #++++++++++++++++++++Aligment and padding**********888
# # #
# name="zeeshu"
# # print(name.center(20,"*"))
# # print(name.ljust(20,'-'))
# # print((name.rjust(10,'@')))
# # print("45".zfill(10))
#
# # #+++++++++++++++++++Trimming and Stripping+++++++++++++++++++++
# #
# # print(" hello ".strip())
# # print(" hello ".lstrip())
# # print(" hello  ".rstrip())
# #
# #
# # #____________________________+++++++== Replace and Translate
# #
# # print(name.replace("e","a"))
# #
# # table = str.maketrans("sh", "45")
# # n=name.translate(table)
# # print(n)
# # "apple".translate(str.maketrans("ae", "12"))  # '1ppl2'
# # #
# # #===================Splitting and Joining
# # numbers= "one,two,three"
# # print(numbers.split(","))      # ['one', 'two', 'three']
# # sentence = "my name is pari"
# # print(sentence.split(" "))
# # print(numbers.rsplit(",", 1))  # ['one,two', 'three']
# #
# # # #splitlines([keepends])
# # # #Splits on line breaks.
# # print("hello\nworld".splitlines()) # ['hello', 'world']
# #
# #
# # #join(iterable)
# # #Joins iterable into string.
# # ",".join(['a', 'b', 'c'])  # 'a,b,c'
# #
# # # Searching and Finding
# # #find() / rfind() / index() / rindex()
# # #Definition: Locate substrings. find() returns -1 if not found; index() raises error.
# #
# # print("hello".find("a"))  # -1
# # print("hello".rfind("l"))   # 3 Searches for the last occurrence of a given substring.
# # print("hello".index("l"))   # 2 : Similar to .find(), it finds the first occurrence of a substring.
# #
# # print("nadaf".find("f"))
# # print("nadaf".find("a"))
# # print("zeeshan".rfind("e"))   # 3 Searches for the last occurrence of a given substring.
# # print("sharah".index("h"))
# # #
# #
# # ###########Checking Start/End==================
# #
# # print("Python".startswith("Py")) # True
# # print("Python".endswith("on"))   # True
# #
# #
# # def is_palindrome(s):
# #     s = s.lower().replace(" ", "")
# #     print(s)
# #     return s == s[::-1]  # Check if the string is equal to its reverse
# #
# # print(is_palindrome("Race car"))  # True
# # print(is_palindrome("annai"))     # False
#
# #
# # #Convert "HeLLo" to all lowercase.
# # str = "HeLLo"
# # print(str.lower())
#
# # #Count how many times "apple" appears in "apple banana apple".
# # text = "apple banana apple"
# # count = text.count("apple")
# # print("apple appears", count, "times.")
#
# #Remove extra spaces from the string " Hello World! "
#
# print(" Hello World! ".strip())
#
# print("12345".isdigit())
# print("oo".isdigit())
#
# text = "I have a dog"
# print(text.replace("dog","cat"))
#
# print("python is fun".title())
#
# print("john@example.com".endswith("gmail.com"))
# print("one,two,three".split(","))
#
# #9. Join the list ['a', 'b', 'c'] using - to make "a-b-c".
# list = ['a', 'b', 'c']
# result = '*'.join(list)
# print(result)
#
# print("banana".index("a"))
#
# #11. Write a function that counts how many words are in a sentence.
#
# def count_words(sentence):
#     words = sentence.split()
#     return len(words)
#
# # Example usage
# text = "Python is easy to learn"
# print("Word count:", count_words(text))
#
# def reverse_each_word(sentence):
#     words = sentence.split()
#     reversed_words = [word[::-1] for word in words]
#     return ' '.join(reversed_words)
#
# # Example usage
# text = "Python is fun"
# print(reverse_each_word(text))
#
#
# name = "John"
# age = 40
# print(f"my name is {name} and i am {age}")
#
# a = 2
# b = 3
# result = a + b
# print(f"{a} + {b} = {result}")
#
# price = 3.45678
# print(f"the price is {price:.2f} dollars")
#
# # 4. Print "John is 25 years old and 175cm tall" using variables.
# height = "175cm"
# print(f"{name} is {age} years old and {height} tall")

# score = 89
# print(f"{name:<10} {score:>5}")
# # 5. Display a table of names and scores aligned neatly using f-strings.
#
# # Sample data
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
#
# # Header
# print(f"{'Name':<10} {'Score':>5}")
# print("-" * 16)
#
# # Data rows
# for name, score in zip(names, scores):
#     print(f"{name:<10} {score:>5}")
#
#
# subjects = ["maths","Hindi","Science","Social Science","English"]
# Marks = [88,77,48,87,83]
#
# print(f"{'Subject':<10} {'Marks':<5}")
# print("-"*20)
#
# for subject,Marks in zip(subjects, Marks):
#     print(f"{subject:<10} {Marks:5}")
#
#
#
# h = 8
# m = 5
# s = 9
#
# print(f"{h:02}:{m:02}:{s:02}")
#
#
# txt= "banana"
# print(txt[0:3])
#
# # Extract "thon" from "Python" using slicing.
# a="python"
# print(a[2:])
#
# # Get the last character of "world" using negative index.
# b = "world"
# print(b[-1])
# print(b[::-1])
# print(txt[::2])
# print(a[1:5])
#
# input_str=input("Enter the string :")
# # rever_str=""
# reversed_str = input_str[::-1]
# print(input_str == reversed_str)
#
# if input_str == reversed_str:
#     print("Its palindrome ")
# else:
#      print("Its not palindrome ")
#
# input_mail = input("enter the mail: ")
# domain = input_mail.split("@")
# print(domain[1])
#
# input_mail = input("Enter the email: ")
#
# # Find the index of '@'
# at_index = input_mail.find('@')
#
# # Use slicing to get the domain
# if at_index != -1: #"Only continue if '@' was found in the email."
#     domain = input_mail[at_index + 1:]
#     print("Domain:", domain)
# else:
#     print("Invalid email format")
#
#
# tx = "The quick brown fox"
# s_txt= tx.split(" ")
# print(s_txt)
# print(s_txt[1])