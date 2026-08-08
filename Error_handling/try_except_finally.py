# 🔹 2. finally
#
# Used to execute code no matter what happens (error or no error).
# Usually for cleanup (like closing files or connections).
#
# try:
#     n = int(input("Enter the input :"))
#     if n % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is not even ")
#
# except ValueError as msg:
#     print("The value is in wrong formate")
#
# except ZeroDivisionError :
#     print("The number not divisible by zero")
#
# finally:
#     print("The program is end ")

# try:
#     h = "HEY"
#     assert h == "HI"
# except AssertionError as msg:
#     print("Error is in assertion statement")
#
# finally:
#     print("The program contiunes ")

# 🔹 5. Using else with try–except
#
# Question:
# Write a program to convert a string into an integer.
# If the conversion is successful, print "Conversion successful".
# Otherwise, print "Invalid input".
#
# Use try–except–else.

# Program to convert a string into an integer using try–except–else

# user_input = input("Enter a number: ")
#
# try:
#     num = int(user_input)
# except ValueError:
#     print("Invalid input")
# else:
#     print("Conversion successful")
#     print("You entered:", num)

# try :
#     x= int(input("Enter the number n1 :"))
#     y = int(input("Enter the number n2 :"))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as msg:
#     print("Please provide valid number only and problem is :",msg)


x = input("Enter the number n1 : ")
y = input("Enter the number n2 : ")

try:
    # Convert input to integers (fixes string division error)
    x = int(x)
    y = int(y)

    print(x / y)

    try:
        print(x.toUpperCase())   # This will ALWAYS fail → int has no such method
    except AttributeError as msg_inner:
        print("AttributeError:", msg_inner)

except ZeroDivisionError:
    print("Can't divide by zero!")

except ValueError:
    print("Please enter valid numbers only!")

finally:
    print("End of program")




