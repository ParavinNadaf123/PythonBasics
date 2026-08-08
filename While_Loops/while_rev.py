# count = 1
# while count <=5:
#     print("The count is ",count)
#     count += 1
#
# a=1
# while a <= 10:
#     print("The value of a :",a)
#     if a == 7:
#         break
#     a +=2
# from If_Elif_Else.If_else_if import total_amount_int

# item = ["table","chair","bike","cycle","TV"]
# index = 0
# while index < len(item):
#     if item[index] == "table":
#         print("The table product found ",item[index])
#         break
#     index +=1
#
# counter = 0
#
# while counter < 3:
#     username = input("Enter the username: ")
#     password = input("Enter the password:")
#     if (username == "admin" and password == "admin1234"):
#         print("Successfull login")
#         break
#     else:
#         print("Invalid credentails")
#     counter +=1
#
# else:
#         print("Account locked. Too many failed attempts.")

# Write a guessing game that asks the user to guess a secret number until correct.
#
# secret_number = int(input("Enter the secret number :"))
# while True:
#     guessed_number = input("Enter the gussed number")
#     if guessed_number == secret_number:
#         print("The number is correct ")
#         break
#     else:
#         print("The number is incorrect,try again")


# Keep asking for a number until the user enters a negative number.
# while True:
#     num = int(input("Enter the number :"))
#     if (num < 0):
#         print("The number is negative",num)
#         break
#     else:
#         print("The number is positive",num)


# Create a menu that accepts "add", "sub", or "exit" and handles invalid input.

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


# Ask the user to enter numbers until an odd number is provided.
# while True:
#     num = int(input("Enter the number : "))
#     if num % 2 == 0:
#         print("the number is even")
#
#     else:
#         print("The number is odd ")
#         break

# Make a countdown from 10 to 1 that stops if the user types "yes".
#
# counter = 10
#
# while counter >=1 :
#     print(counter)
#     input_response = input("Enter the user response (yes/no) :")
#     if input_response == "yes":
#         print("The user response is yes, loop stops")
#         break
#     counter -=1

# Continuously add input numbers until the user enters 0 and then print the total.
# total = 0
# while True:
#     num = int(input("Enter the number "))
#     if num == 0:
#         break
#     total = total + num
# print("The total is ",total)

# Ask for numbers until one is divisible by 7.
# while True:
#     num = int(input("Enter the number: "))
#     if num % 7 == 0:
#         print("This number is divisible by 7")
#         break
#     else:
#         print("please continue")
#
# Keep asking for a password until the correct one is entered.

# while True:
#     password = input("Enter the password:")
#     if password == "admin123":
#         print("The password is correct")
#         break
#     else:
#         print("Try again ")

# while True:
#     word = input("Enter the word :")
#     if "z" in word :
#         print("The word contains 'z' ")
#         break
#     else:
#         print("try again , enter the new word")
#
# Keep asking for a sentence until one ends with a question mark (?).

# while True:
#     sentence = input("Enter the sentence :")
#     if '?' in sentence:
#         print("The sentence contain ? , stops here")
#         break
#     else:
#         print("Try again, enter the sentence ")
#
#

# Ask for words until one ends with a vowel.
# while True:
#     word = input("Enter the word : ")
#     if word.endswith(("a","e","i","o","u")):
#         print("The word ends with vowels")
#         break
#     else:
#         print("enter new word")


# Continue taking numbers until two even numbers are entered in a row.
# count = 0
# while True:
#     num = int(input("Enter the number :"))
#     if num % 2 == 0 :
#         count +=1
#     else:
#         count == 0
#
#     if count == 2:
#         print("You entered two even numbers in a row. Exiting.")
#         break
#     else:
#             print("Keep going...")

# Write a program with options "play", "pause", and "stop" that performs actions based on user input and exits on "stop".
# while True:
#     options = input("Enter the option  'play', 'pause', and 'stop' :")
#
#     if options == "play" :
#         print("The game is on ")
#         pass
#     elif options == "pause":
#         print(" The game is paused")
#         pass
#     elif options == "stop":
#         print("user enter to stop , exixting ......")
#         break
#     else:
#         print("Enter the correct option, option on defined ")

# Create a menu-driven program where users can select items like "Girmit", "Paddu", or "Exit" using item codes.
# Menu = [  {"A1":"Girmit"},
#             {"B1":"Paddu"},
#               {"C1":"Tea"},
#              {"D1":"Coffe"},
#            {"E1":"Exit"}]
# #
# while True:
#     options = input("Enter the option :")
#     if options == "A1":
#         print("The item selected is Girmit")
#     elif options  =="B1":
#         print("The item selected is paddu")
#     elif options == "C1":
#         print("The item selected is Tea")
#     elif options == "D1":
#         print("The item selected is Coffe")
#     elif options == "E1":
#          print("You selected Exit")
#          break
# print("Thank you visit again")


# Build a calculator that asks for two numbers and performs operations (+, -, *) or exits on "X".

# while True:
#     n1 = int(input("Enter the number n1 :"))
#     n2 = int(input("Enter the number n2 :"))
#     operations = input("Enter the operations to perfrom (+, -, *) or exits on X :")
#
#     if operations == "*":
#         print("The mul of n1 and n2 is n1*n2 :", n1 * n2)
#     elif operations == "+":
#         print("The addition of n1 and n2 is n1+n2 :", n1 + n2)
#     elif operations == "_":
#         print("The subtraction of n1 and n2 is n1-n2 :", n1 - n2)
#     elif operations == "/":
#         print("The division of n1 and n2 is n1/n2 :", n1 / n2)
#     elif operations == "X":
#         print("The operation selected is exist")
#         break
#     else:
#         print("Invalid operation. Please choose +, -, *, or X.")
# print("Thank you")

# while True:
#     password = input("Enter your password: ")
#     if len(password) >= 8:
#         print("Valid password")
#         break
#     else:
#         print("Password length doesnt meet, Please reset the password")

#
max_number = 0
while True:
    number = int(input("Enter your number: "))
    if number <0:
        print("The negative number is entered hence existing")
        break
    elif number > max_number:
        max_number = number
print("The max number is ", max_number)

# Write a program that checks if the entered number is prime and stops when the user enters 1.

while True:
    number = int(input("Enter a number (enter 1 to stop): "))

    if number == 1:
        print("Stopped. You entered 1.")
        break

    if number <= 1:
        print(f"{number} is not a prime number.")
    elif number == 2:
        print("2 is a prime number.")
    elif number % 2 == 0:
        print(f"{number} is not a prime number.")
    else:
        is_prime = True  # Assume it is prime

        # Check only odd numbers from 3 to √number
        i = 3
        while i * i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 2

        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
