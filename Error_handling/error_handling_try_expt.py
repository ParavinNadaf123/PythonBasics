#
# try:
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print(f"{num} is an even number ✅")
#     else:
#         print(f"{num} is an odd number 🔹")
# except ValueError:
#     print("❌ Error: Please enter a valid integer!")
# finally:
#     print("Program finished 👋")
#
# try :
#     print(10/2)
# except  ZeroDivisionError as msg:
#     print("exception raised and its description is :",msg)
#
# try:
#     x = int(input("Enter the number n1 :"))
#     y = int(input("Enter the number n2 :"))
#     print(x/y)
# except ZeroDivisionError as errormsg:
#     print("cant divide with zero")
# except ValueError as errormsg2:
#     print("Please enter the valid integer")

# AssertionError	Raised when an assert statement fails
# x = "Good Morning "
# assert  x =="Good Morning" #if condition returns True, then nothing happens:
#
# assert x == "Good Afternoon" #if condition returns False, AssertionError is raised:
# y = "Good"
# try :
#     assert y == "Bad"
#
# except AssertionError as errormsg:
#     print("Error in assert statement")
# except:
#     print("Something else went wrong")

# An AttributeError will occur if you try to access a method that does not exists:
# l= "zesshan"
# print(l.toupper())

# h = "pari"
# try:
#     print(h.toupper())
# except AttributeError as msg:
#     print("AttributeError: 'str' object has no attribute 'toupper'")
# except:
#     print("something else went wrong")
#
# # EOFError
# try:
#     n = int(input("Enter a number: "))
# except EOFError:
#     n = 0  # Assigning a default value
#     print("No input provided, setting default value to 0.")
#
# print("Result:", n * 10)

# Indexerror
# x = ["apple", "banana", "cherry"]
# print(x[5])

# print("End of program")
# v = ["apple", "banana", "cherry"]
# try:
#     print(v[2])
#     print(v[5])
# except IndexError as msg:
#     print("list index out of range")
# except:
#     print("something else went wrong")

#keyerror
# emp_details = {"name":"pari","Gender":"Female"}
# print(emp_details["age"])

# emp_details = {"name":"pari","Gender":"Female"}
# try:
#     print(emp_details["name"])
#     print(emp_details["city"])
#     # print(emp["Gender"])
# except KeyError as msg:
#     print("You are trying to access a dictionary item that does not exist!")
# except:
#     print("Something else went worng ")

# try:
#     z = float(input("Enter the float number :"))
# except ValueError as msg:
#     print("The value has wrong formate")
# except:
#     print("something else went wrong")

try:
  x = "hello" + 15
except TypeError:
  print("Please convert to string before concatenate")
except:
  print("Something else went wrong")



