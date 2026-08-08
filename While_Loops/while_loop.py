from operator import index
#
# count = 1
# while count<=5:
#     print("count is :",count)
#     count+=1

#
# a=1
# while a<=10:
#     print(a)
#     if a == 5:
#         break
#     a+= 2
# #
# product=("TV","Bike","CAR","Table","Computer")
# index =0
# while  index < len(product):
#     if product[index] == "Table":
#         print("Product fount",product[index])
#         break
#     index +=1
#
# counter = 0
# while counter < 3:
#     username = str(input("enter the username:"))
#     password = str(input("enter the password:"))
#     if (username == "admin" and password == "admin123"):
#         print("Login successfull")
#         break
#
#     else:
#         print("Invalid credentails , try again")
#     counter +=1
#
# else:
#     print("Account locked. Too many failed attempts.")
#
# secret_number = 7  # any number you want the user to guess
#
# while True:
#     user_guess = int(input("Guess a number between 1 and 10: "))
#
#     if user_guess == secret_number:
#         print("Correct!")
#         break  # exit the loop
#     else:
#         print("Try again.")
#
#
# while True:
#     num = int(input("enter a number : "))
#     if num <0:
#         print("its a negative number")
#         break
#     else:
#         print("its positive number")
#
# while True:
#     choice =input("enter a choice : ")
#
#     if choice == "add":
#         pass
#     elif choice == "sub":
#         pass
#     elif choice =="exit":
#         break
#     else:
#         print("invalid choice")
#
#
# while True:
#     random_text=input("enter a choice : ")
#     if random_text == "exit":
#         print("the loop will stop")
#         break


# while True:
#     number = int(input("Enter the odd number: "))
#
#     if (number % 2 != 0):
#         print("valid odd number")
#         break
#     else:
#         print("Its not odd number")
#
# count = 10
#
# while count >= 1:
#     print("Countdown:", count)
#     response = input("Do you want to stop the countdown? (yes/no): ").lower()
#
#     if response == "yes":
#         print("Countdown stopped by user.")
#         break
#
#     count -= 1
#
# if count == 0:
#     print("Countdown completed.")

# total = 0
# while True:
#     number = int(input("Enter the  number: "))
#     if number == 0:
#         break
#     total=total+number
# print("total is :",total)


# while True:
#     number = int(input("Enter the  number: "))
#     if number % 7 == 0:
#         break
# print("it is divisible by 7")

# while True:
#     password= str(input("Enter the password:"))
#     if password == "admin1234":
#         break
#     else:
#         print("Please enter the correct password")
# print("The password is correct")

# while True:
#     num = int(input("Enter the number: "))
#     if num % 5 == 0:
#         break
# print("It is divisible by 5")

# while True:
#     word = str(input("Enter the word contains 'z':" ))
#     if 'z' in word:
#         print("The word contains 'z'",word)
#         break
#     else:
#         print("The word doesnt contain 'z', Please enter the new word")

# while True:
#     sentence = str(input("Enter the sentence that ends with question mark: "))
#     if sentence.endswith("?"):
#         print("The sentence ends with '?'")
#         break
#     else:
#         print(" The sentence doesnt end with '?', Please Enter the new sentence ")
#
# while True:
#     word2 = str(input("enter the word ends with vowel: "))
#     if word2.endswith(("a","e","i","o","u")):
#         print("The word ends with vowel")
#         break
#     else:
#         print("The word doesnt ends with vowels , please enter the new word")


# consecutive_even_count = 0

# while True:
#     no = int(input("Enter a number: "))
#
#     if no % 2 == 0:
#         consecutive_even_count += 1
#     else:
#         consecutive_even_count = 0
#
#     if consecutive_even_count == 2:
#         print("You entered two even numbers in a row. Exiting.")
#         break
#     else:
#         print("Keep going...")


# Questions
#
#
# 🔹 Input Validation & User Interaction
# Keep asking the user for a number until they enter a multiple of 5. Then stop.
#
# Prompt the user to type a word that contains the letter "z". If the word contains "z", stop the loop.
#
# Ask the user to enter a sentence. Stop when the sentence ends with a question mark.
#
# Keep asking for a word. Break the loop if the word starts with a vowel.
#
# Continuously ask the user for numbers. Stop when they enter two even numbers in a row.
#
# 🔹 Menu & Command Loops
# Create a menu with options: "play", "pause", "stop". Loop until "stop" is chosen.
#
# Simulate a vending machine: ask for item codes and stop if the user enters "X".
#
# Keep showing a simple calculator menu. Let the user perform operations until they choose to exit.
#
# Create a language quiz. Ask vocabulary questions until the user types "quit".
#
# Implement a password reset loop. Keep asking for the new password until it meets a minimum length.
#
# 🔹 Math & Logic Loops
# Ask the user for numbers and keep track of the maximum number entered. Stop when they enter a negative number.
#
# Keep asking for numbers and check if they are prime. Stop when the user enters 1.
#
# Continuously double a number entered by the user. Stop when the result exceeds 1000.
#
# Ask for numbers and print whether they’re odd or even. Stop on the 5th odd number.
#
# Keep multiplying user-entered numbers. Stop if the product becomes 0.
#
# 🔹 Pattern & Countdown Practice
# Print numbers from 1 to 100 but stop if a number divisible by both 3 and 5 is found.
#
# Countdown from a user-provided number. Stop early if user types “stop”.
#
# Keep printing asterisks * one per line. Stop if the user enters the word "done".
#
# Ask for a character and print it repeatedly in a triangle pattern. Stop if character is a digit.
#
# Count up from 0. Stop when the user says "enough" or after 20 numbers, whichever comes first.