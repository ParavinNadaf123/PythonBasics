# 🧩 What is Error Handling?
#
# Error handling means detecting and managing runtime errors
# (like dividing by zero, wrong input, or missing files) so
# your program doesn’t crash suddenly.
#
# We handle errors using try, except, finally, and raise.
# ZeroDivisionError
# try:
#     n= int(input("Enter the number :"))
#     print(10/n)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("please enter valid numbetr")
#
# #valurError
# try:
#     n = int(input("Enter the number:"))
#     print(10/n)
# except ValueError:
#     print("enter the valid integer")
from pydoc import browse

#TypeError
# try:
#     add = 10+"20"
#     print(add)
# except TypeError:
#     print("Cannot add an integer and a string!")

#NameError
# try:
#     print(age)
# except NameError:
#     print("name 'age' is not defined")
#
# #indexError
# try:
#     num = [1,2,4,6,8]
#     print(num[5])
# except IndexError:
#     print("list index out of range")
#
# #keyerror
# try:
#     d = {"name" : "pari","age" : 22,"gender" : "Female"}
#     print(d["city"])
# except KeyError:
#     print("Key not found in dictionary!")
#
# #AttributeError
# try:
#     str = "lopo"
#     print(str.touppercase())
# except AttributeError:
#     print("str' object has no attribute 'touppercase'")
#
# #8. FileNotFoundError
# try:
#     file = open("data.txt","r")
#     print(file.read())
# except  FileNotFoundError:
#     print("No such file or directory: 'data.txt'")
#
# try:
#     import mymodule
# except ModuleNotFoundError:
#     print("Module not found!")
#
#
# # num = float('inf')  # infinity value
# #
# # if num == float('inf'):
# #     raise FloatingPointError("Floating point overflow occurred!")
#
# try:
#     raise FloatingPointError("Floating point calculation error")
# except FloatingPointError:
#     print("Floating point error occurred!")
#
#
# try:
#     num = 10 / 0
# except Exception as e:
#     print("Error:", e)
#
#
# # /-------------------------------------------------- finally:
# try:
#     num = int(input("Enter the number:"))
#     print(10/num)
# except ZeroDivisionError:
#     print("cannot div by zero")
# except ValueError:
#     print("Invalid input!")
#
# finally:
#     print("This will work")



file = None
try:
    file = open("data.txt","r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("No such file or directory: 'data.txt'")

finally:
    if file:
        file.close()
        print("file closed successfuly")


connection = None
try:
    print("connecting to database")
    connection = "database connection created"
    print("Fetching the data")

except Exception as e:
    print("Database error:",e)
finally:
    if connection:
        print("Database connection closed")


 # ----------------------

try:
    num = 10 / 0

except Exception as e:
    print("Error:", e)

# ==========================================================

api_connection = None
try:
    print("connecting API server")
    api_connection = True
    print("sending API request")

except Exception as e:
    print("API Error",e)

finally:
    if api_connection:
        print("API connection clsed")

browse =  None
try:
    print("Opening the browser")
    browse = "chorme browser"
    print("Running the test case")
except Exception as e:
    print("test failed Error",e)

finally:
    if browse:
        print("Closing browser and releasing resources")

# ===============================================================
driver = None

try:
    print("Launching browser")
    driver = "Chrome"

    print("Opening application")
    print("Executing test case")

except Exception as e:
    print("Test Failed:", e)

finally:
    print("Taking screenshot")
    print("Closing browser")
    driver = None
    print("Test execution completed")


# =============================================RAIse

age = int(input("Enter the age:"))

if age < 18 :
    raise ValueError("You must be at least 18 years old.")

print("Access Granted")

num = int(input("Enter the number:"))
if num <0:
    raise ValueError("Negative Number is not allowed")

print(num)

marks = int(input("Enter the marks :"))
if marks > 100:
    raise ValueError("Marks cannot be greater than 100")

print("Marks:",marks)

passwrod = input("Enter the password:")
if len(passwrod) < 8:
    raise ValueError("Password must contain at least 8 characters.")
print("password accepted")

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)
finally:
    print("Program finished")