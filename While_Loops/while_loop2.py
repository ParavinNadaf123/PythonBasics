# while True:
#     menu = str(input("options: play, pause, stop: "))
#     if menu == "play":
#         print("Game is on")
#     elif menu == "pause":
#         print("game is paused")
#     elif menu == "stop":
#         print("game is stopped")
#         break
#     else:
#         ("enter your correct options")

# Menu = [{"A1":"Girmit"},
#          {"B1":"Paddu"},
#          {"C1":"Tea"},
#          {"D1":"Coffe"},
#          {"E1":"Exit"}]
#
# while True:
#     item = str(input("Enter the items :"))
#     if item == "A1":
#         print("You selected Girmit")
#     elif item =="B1":
#         print("You selected Paddu")
#     elif item == "C1":
#         print("You selected Tea")
#     elif item == "D1":
#         print("You slelected Coffe")
#     elif item == "E1":
#         print("You selected Exit")
#         break
#
# print("Thank You, Visit again ")

# while True:
#     a = int(input("Enter the first num : "))
#     b = int(input("Enter the second num : "))
#     operations = input("enter the operations: ")
#     if operations == "+":
#         print("The sum of a and b is :",a+b)
#     elif operations == "*":
#         print("The mul of a and b is :",a*b)
#     elif operations == "-":
#         print("The minus os a and b is :",a-b)
#     elif operations == "X":
#         print("Exit")
#         break
# print("Thank you")

# while True:
#     print("\nSimple Calculator Menu")
#     print("Choose an operation: +, -, *, or X to exit")
#     operations = input("Enter the operation: ")
#
#     if operations.upper() == "X":
#         print("Exiting calculator...")
#         break
#
#     # Check for valid operation before asking for numbers
#     if operations in ["+", "-", "*"]:
#         a = int(input("Enter the first number: "))
#         b = int(input("Enter the second number: "))
#
#         if operations == "+":
#             print("The sum of a and b is:", a + b)
#         elif operations == "*":
#             print("The product of a and b is:", a * b)
#         elif operations == "-":
#             print("The difference of a and b is:", a - b)
#     else:
#         print("Invalid operation. Please choose +, -, *, or X.")
#
# # print("Thank you for using the calculator!")
# #
# quiz = {
#     "loquacious": "talkative",
#     "benevolent": "kind",
#     "obstinate": "stubborn",
#     "serene": "calm",
#     "frugal": "thrifty"
# }
#
# print("🔤 Welcome to the Vocabulary Quiz!")
# print("Type 'quit' at any time to exit.\n")
#
# while True:
#
#     for word, meaning in quiz.items():
#         answer = input(f"What is the meaning of '{word}'? ").strip().lower()
#         if answer == "quit":
#             print("Exiting quiz...")
#             break
#         elif answer == meaning:
#             print("✅ Correct!\n")
#         else:
#             print(f"❌ Incorrect. The correct answer is '{meaning}'.\n")
#     else:
#         continue
#     break  # Exits outer loop if inner loop is broken
#
# print("Thanks for playing!")




# while True:
#     password = input("Enter your password: ")
#     if len(password) >= 8:
#         print("Valid password")
#         break
#     else:
#         print("Password length doesnt meet, Please reset the password")

# max_number = 0
# while True:
#     number = int(input("Enter the number:"))
#     if number > max_number:
#         max_number = number
#         print("update maximum number is :",max_number)
#     if  number < 0:
#         break
#
# print("The maximum number is :",max_number)
#
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


while True:
    number = int(input("Enter a number (enter 1 to stop): "))

    if number == 1:
        print("Stopped. You entered 1.")
        break

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


# while True:
#     number = int(input("Enter a number : "))
#     if number < 1000:
#         double_number = number*2
#         print("The doubled number is : ", double_number)
#     if double_number > 1000:
#         print(" Stopped the result exceeds 1000.")
#         break
# print("Exit")

# odd_count =0
# while True:
#     number = int(input("Enter a number: "))
#
#     if number % 2 != 0:
#         print("It's an odd number:", number)
#         odd_count += 1
#     else:
#         print("It's an even number:", number)
#
#     if odd_count == 5:
#         print("You entered 5 odd numbers. Stopping.")
#         break
#
# print("Exit")

#
# product = 1
# while True:
#     num = int(input("enter the number:" ))
#     product *= num
#     print("Current product : ",product)
#
#     if product == 0:
#         print("Product became 0. Stopping.")
#         break
# for i in range(1, 101):
#     print(i)
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"Stopped at number {i} because it is divisible by both 3 and 5.")
#         break
# start = int(input("Enter a number to start countdown: "))
#
# for i in range(start, 0, -1):
#     print(i)
#     user_input = input("Press Enter to continue or type 'stop': ")
#     if user_input.lower() == "stop":
#         print("Countdown stopped by user.")
#         break
# else:
#     print("Countdown completed.")

# while True:
#     print("*")
#     user_input = str(input("Enter a done to stop : "))
#
#     if user_input == "done":
#         break
while True:
    char = str(input("Enter the charater:" ))

    if char.isdigit():
        print("digit entered ,stopping ....")
        break


    for i in range(1,6):
        print(char * i)



count = 0

while count < 20:
    print(count)
    user_input = input("Press Enter to continue or type 'stop': ")
    if user_input.lower() == "stop":
        print("Counting stopped by user.")
        break
    count += 1
else:
    print("Counted up to 20 successfully.")


