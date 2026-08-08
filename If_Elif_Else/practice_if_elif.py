# # ✅ 1. Check if a number is positive, negative, or zero
# while True:
#     num = int(input("enter the number: "))
#     if num > 0 :
#         print("the number is positive")
#         break
#     else:
#         print("The number is negative")
import re
# #check the largest number of 3
# n1= int(input("Enter the value of n1: "))
# n2= int(input("Enter the value of n2: "))
# n3= int(input("Enter the value of n3: "))
#
# if n1>=n2 and  n1>=n3:
#     print("The n1 is greater",n1)
# elif n2>n1 and n2>=n3:
#     print("n2 is grater",n2)
# else:
#     print("n3 is greater",n3)
# #grade on marks
# marks = int(input("enter the marks : "))
# if marks <= 35:
#     print("C Grade")
# elif marks > 36 and marks <=55:
#     print("B Grade")
# elif marks >56 and marks<= 65:
#     print("A Grade")
# else:
#     print("A+ Grade")
# # leap year
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a Leap Year ✅")
# else:
#     print(f"{year} is NOT a Leap Year ❌")

# #✅ 5. Check if a number is even or odd


# num = int(input("Enter the number :"))
# # while num > 0:
# if num % 2 == 0:
#     print("Its even number",num)
# else:
#     print("Its not even number")

# # 🔐 1. Username and Password Validation
# # Question:
# # Write a program that checks if the user-entered username and password match the expected credentials.
# If correct, print a login success message. Otherwise,
# provide appropriate error messages based on whether the username, password, or both are incorrect.
# username = "parikn"
# password = "1234"
# un  = input("Enter the username :")
# pw = input("Enter the password ")
# if un == username and pw == password:
#     print("username  and password is correct, login successful")
# elif (un != username):
#     print("The username is incorrect")
# elif (pw != password):
#     print("Password is incorrect")
# else:
#     print("login failed")





# # 📋 2. Column Name Check
# # Question:
# # Given a predefined list of required column names,
# write a program that accepts a comma-separated input of column names.
# Check whether all entered columns exist in the required list and display appropriate validation messages.

# required_column_list = ["name","surname","contact_no","age","gender","email"]
# column_list = input("enter the column name to check with comma separator:")
#
#
# column_names = [col.strip() for col in column_list.split(",")]
# print(col)
#
# # Step 1: Define the required column names
# required_columns = ["name", "surname", "id", "age", "email"]
#
# # Step 2: Ask the user to enter column names
# user_input = input("Enter the column names to check (comma separated): ")
#
# # Step 3: Split the input into a list
# # For example: "name, surname, id" → ["name", " surname", " id"]
# user_columns_raw = user_input.split(",")
# # print(user_columns_raw)
# # Step 4: Remove extra spaces from each column name
# cleaned_user_columns = []
# # print(cleaned_user_columns)
#
# for column in user_columns_raw:
#     cleaned_column = column.strip()  # remove spaces around the text
#     cleaned_user_columns.append(cleaned_column)
# #
# # Step 5: Check for any columns entered that are NOT in the required list
# invalid_columns = []
# #
# for column in cleaned_user_columns:
#     if column not in required_columns:
#         invalid_columns.append(column)
# #
# # Step 6: Show the result
# if len(invalid_columns) == 0:
#     print("✅ All column name checks passed.")
# else:
#     print("❌ Column check failed. These columns are not expected:", invalid_columns)

# required_subject = ["maths","english","science","hindi","kannada"]
# input_subject = input("Enter the suject with (comma separater):")
#
# input_sub_raw = input_subject.split(",")
# print(input_sub_raw)
#
# cleaned_subjects= []
#
# for sub in input_sub_raw:
#     subject_without_space=sub.strip()
#     cleaned_subjects.append(subject_without_space)
#
# invalid_sub_input=[]
#
# for  sub in cleaned_subjects:
#     if sub not in required_subject:
#         invalid_sub_input.append(sub)
#
#
# if len(invalid_sub_input) == 0:
#     print("The subjects check is passed")
# else:
#     print("❌ subjects check failed. These subjects are not expected:", invalid_sub_input)
#




# #
# # 🎂 3. Age Input Validation
# # Question:
# # Write a program that asks the user to enter their age. Validate that the age is a positive number and does not exceed 120.
# Display whether the age is valid or not.

# age = int(input("Enter the age: "))
# if age > 0 and age < 120:
#     print("Valid Age")
# else:
#         print("Invalid age ")
    # #
# # 👥 4. Age Validation in Records
# # Question:
# # Given a list of people with their names and ages,
# write a program to validate each person’s age.
# Ages must be between 1 and 120.
# # Print whether each person’s age is valid or specify if it's negative or too high.
# # #
# data = [{"name":"alice","age":"22"},
#         {"name":"sonu","age":"18"},
#         {"name":"Ali","age":"120"},
#         {"name":"sakku","age":"150"},
#         {"name":"zeeshu","age":"3"}
#         ]
#
# for record in data:
#     age_str =record["age"]
#     age = int(age_str)
#
#     if age < 0:
#         print(f"{record['name']} → Invalid Age (Negative value: {age})")
#     elif age > 120:
#         print(f"{record['name']} → Invalid Age (high value: {age})")
#     else:
#        print(f"{record['name']} → Valid Age (high value: {age})")



#

# # 📅 5. Date Format Validation
# # # Question:
# # # You are given a list of date strings. Write a program to validate whether each date is in the correct "YYYY-MM-DD" format using Python’s datetime module. Display whether each date string is valid or invalid.
# # #
# from datetime import datetime
#
# data = [
#     {"name": "alice", "DOB": "2022/05/03"},
#     {"name": "sonu", "DOB": "2011/12/12"},
#     {"name": "Ali", "DOB": "1999/2/22"},
#     {"name": "sakku", "DOB": "22/3/2015"},
#     {"name": "zeeshu", "DOB": "2/25/1995"}
# ]
#
# # Loop through each record and validate the date format
# for record in data:
#     name = record["name"]
#     dob_str = record["DOB"]
#
#     try:
#         # Try to parse date in correct format: YYYY-MM-DD
#         datetime.strptime(dob_str, "%Y/%m/%d")
#         print(f"{name} → {dob_str} is ✅ valid (format: YYYY/MM-DD)")
#     except ValueError:
#         print(f"{name} → {dob_str} is ❌ invalid (should be YYYY-MM-DD)")


# # 🌍 6. Country and Currency Validation
# # Question:
# # Given a list of records with countries and their currencies, write a program that verifies whether the currency matches the expected currency for a given country (India → INR, USA → USD).
# # Display appropriate messages for valid and invalid cases.
# data2 = [
#     {"country": "india","currency":"INR"},
#     {"country": "india","currency":"INR"},
#     {"country": "korea","currency":"won"},
#     {"country": "USA","currency":"USD"},
#     { "country": "USA","currency":"USD"},
#     {"country": "india","currency":"USD"},
#     {"country": "china","currency":"USD"}
# ]
#
# for record in data2:
#     country = record["country"]
#     currency = record["currency"]
#
#
#     if country == "india":
#         if currency == "INR":
#             print(f"The currency for {country} is {currency} is valid ")
#         else:
#             print(f"The currency for {country} is invalid")
#
#     elif country == "USA":
#         if currency == "USD":
#             print(f"The currency for {country} is {currency} is valid ")
#         else:
#             print(f"The currency for {country} is invalid")
#
#     else:
#         print(f"{country} → Unknown country. No currency rule defined")

# # 🆔 7. Duplicate Employee ID Check
# # Given a list of employee records with names and IDs,
# write a program to detect duplicate employee IDs.
# If any duplicates exist, print the IDs; otherwise, confirm all IDs are unique.
# emp_data = [
#     {"name": "alice", "id": "2022"},
#     {"name": "sonu", "id": "2011"},
#     {"name": "Ali", "id": "1999"},
#     {"name": "sakku", "id": "2022"},
#     {"name": "zeeshu", "id": "2"}
# ]
# seen_ids=set()
# dup_ids=[]
# for record in emp_data:
#     name= record["name"]
#     emp_id = record["id"]
#
#
#     if emp_id in seen_ids:
#         print(f"Duplicate id found : {emp_id}")
#         dup_ids.append(emp_id)
#     else:
#         seen_ids.add(emp_id)
#
# if not dup_ids:
#     print("All the ids are unique")
# else:
#     print(f"⚠️ Duplicates found: {set(dup_ids)}")


# # Given a list of employee salary records, write a program to validate each salary.
# Salaries must be positive and non-zero.
# Print messages indicating whether each salary is valid or invalid.
# emp_data = [
#     {"name": "alice", "salary": "20000"},
#     {"name": "sonu", "salary": "10000"},
#     {"name": "Ali", "salary": "50000"},
#     {"name": "sakku", "salary": "-100"},
#     {"name": "zeeshu", "salary": "0"}
# ]
#
# for record in emp_data:
#     name = record["name"]
#     emp_sal = record["salary"]
#
#     if emp_sal <= "0":
#         print(f"Salary {emp_sal} is negative and non-zero")
#     else:
#         print(f"The salary{emp_sal} is valid")

# # 🧾 9. Tax Validation Based on Salary Slabs

# # Given a list of employee records with names, salaries, and reported tax percentages,
# write a program to validate whether the tax percentage matches the expected value based on salary slabs:
# Display whether each employee’s tax is correct or not.
# emp_data = [
#     {"name": "alice", "salary": 200000,"tax":"5%"},
#     {"name": "sonu", "salary": 1000000,"tax":"10%"},
#     {"name": "Ali", "salary": 500000,"tax":"5%"},
#     {"name": "sakku", "salary": 1500000,"tax":"10%"},
#     {"name": "zeeshu", "salary": 2000000,"tax":"5%"}
# ]
# for record in emp_data:
#     name = record["name"]
#     salary = record["salary"]
#     tax = record["tax"]
#
#     if salary < 500000:
#         expected_tax = "5%"
#     elif salary >= 500000 and salary <=1000000:
#         expected_tax = "10%"
#     else:
#         expected_tax = "20%"
#
#
#     if expected_tax == tax:
#             print(f"✅ {name}: Tax is correct ({tax})")
#     else:
#             print(f"❌ {name}: Tax is incorrect. Expected {expected_tax}, got {tax}")

# #
# #
# 🧑‍💼 1. Capital Letter in Employee Name
# Question:
# Write a program to check if each employee's name starts with a capital letter.
# Print appropriate validation messages for each name.
# emp_data = [
#     {"name": "Alice", "salary": 200000,"tax":"5%"},
#     {"name": "sonu", "salary": 1000000,"tax":"10%"},
#     {"name": "Ali", "salary": 500000,"tax":"5%"},
#     {"name": "sakku", "salary": 1500000,"tax":"10%"},
#     {"name": "Zeeshu", "salary": 2000000,"tax":"5%"}
# ]
#
# for record in emp_data:
#     name = record["name"]
#
#     if name.istitle():
#         print(f"The name {name} start with capital letter ")
#     else:
#         print(f"The name {name} does not start with capital letter ")
#
#

# 📞 2. Phone Number Validation
# Question:
# Given employee phone numbers,
# write a program to validate that each number contains exactly 10 digits and consists only of numbers.
# emp_data = [
#     {"name": "Alice", "contact": "9875432178"},
#     {"name": "sonu", "contact": "4563217896"},
#     {"name": "Ali", "contact": "55786432poi"},
#     {"name": "sakku", "contact": "879654329"},
#     {"name": "Zeeshu", "contact": "897654329"}
# ]
#
# for record in emp_data:
#     con_no = record["contact"]
#
#     if con_no.isdigit() and len(con_no) == 10:
#         print(f"number {con_no} contains exactly 10 digits and consists only of numbers")
#     else:
#         print(f"The number {con_no} is in valid ")
# 📧 3. Email Format Validation
# Write a program to validate employee email addresses.
# A valid email should contain both '@' and '.'.
# Print whether each email is valid or invalid.

# emp_data = [
#     {"name": "Alice", "email": "alice@gmail.com"},
#     {"name": "sonu", "email": "sonu@gmail.com"},
#     {"name": "Ali", "email": "ali@gmail,com"},
#     {"name": "sakku", "email": "sakku%gmail.com"},
#     {"name": "Zeeshu", "email": "zee@gmail.com"}
# ]
# for record in emp_data:
#     email = record["email"]
#
#     if "@" in email and "." in email:
#         print(f"The {email} has '@' and '.' its valid email ID")
#     else:
#         print(f"The {email} doesnt have '@' and '.' its invalid  email ID")

# 💵 4. Product Price Range Check
# Question:
# Given a list of products and their prices,
# write a program to check if the price is in the range of 1 to 9999.
# Print if each product's price is within range or not.

# item_data = [
#     {"name": "toys", "price": 500},
#     {"name": "table", "price": 10000},
#     {"name": "chair", "price": 700},
#     {"name": "cycel", "price": 2500},
#     {"name": "bike", "price": 70000}
# ]
#
# for record in item_data:
#     prod_name = record["name"]
#     prod_price = record["price"]
#
#     if prod_price > 0 and prod_price < 9999:
#         print(f"Product {prod_name} price {prod_price} is within range")
#     else:
#         print(f"Product {prod_name} price {prod_price} is out of   range")

# 🚻 5. Gender Field Validation (Buggy Logic Example)
# Question:
# Write a program to validate that the gender field for each employee is either "M" or "F". Fix any logical errors in the condition that checks for valid gender.
#
# ✅ Note: The line if emp_gen == "M" and emp_gen == "F" will always fail because no value can be both "M" and "F". It should be:
#if emp_gen == "M" or emp_gen == "F":
# emp_details =[{"name":"pari","Gender":"F"},
#               {"name":"Hari","Gender":"M"},
#               {"name":"Kari","Gender":"M"},
#               {"name":"Aari","Gender":"other"},
#               {"name":"Sari","Gender":"F"},
#               {"name":"wari","Gender":"F"},
#               {"name":"fari","Gender":"F"}]
#
# for record in emp_details:
#     emp_gen = record ["Gender"]
#
#     if emp_gen == "M" or emp_gen == "F":
#         print("Valid Gender")
#     else:
#         print("Invalid Gender")

# Write a program to check if the discount applied on a product is 50% or less.
# Print "Valid" for discounts within the limit, and "Invalid" otherwise.
#
# item_data = [
#     {"name": "toys", "price": 500,"discount":"20%"},
#     {"name": "table", "price": 10000,"discount":"10%"},
#     {"name": "chair", "price": 700,"discount":"5%"},
#     {"name": "cycel", "price": 2500,"discount":"70%"},
#     {"name": "bike", "price": 70000,"discount":"80%"}
# ]
# for record in item_data:
#     prod_item = record["name"]
#     prod_disct = record["discount"]
#
#     if prod_disct <= "50%":
#         print(f"The product {prod_item}  has  Valid  discounts {prod_disct} within the limit")
#     else:
#         print("Invalid discount",prod_disct)
#
# 🧾 7. Invoice Price Check
# Question:
# Given a list of invoice records, write a program to validate that the total_price equals unit × unit_price. If not, flag the record.
# item_data = [
#     {"name": "toys", "unit_price": 500,"unit":5,"total_Price":2500},
#     {"name": "table", "unit_price": 10000,"unit":1,"total_Price":10000},
#     {"name": "chair", "unit_price": 700,"unit":4,"total_Price":2800},
#     {"name": "cycel", "unit_price": 2500,"unit":2,"total_Price":5000},
#     {"name": "bike", "unit_price": 70000,"unit":1,"total_Price":7000}
# ]
#
# for record in item_data:
#     prod_name = record["name"]
#     prod_unit_price = record["unit_price"]
#     prod_unit = record["unit"]
#     prod_total_Price = record["total_Price"]
#
#     if prod_total_Price == (prod_unit_price * prod_unit):
#         print(f"The total price  {prod_total_Price}  for {prod_name} is correct")
#     else:
#         print("The total Price is incorrect",{prod_name})




#
# # Given employee records with date of joining and date of exit,
# # write a program to ensure that the joining date is before the exit date.
# # Print valid or invalid messages accordingly.
# from datetime import datetime
#
# from If_Elif_Else.If_else_if import pan_no
#
# emp_details =[{"name":"pari","DOJ":"2021-02-15","DOE":"2025-01-31"},
#               {"name":"Hari","DOJ":"2019-02-22","DOE":"2022-10-10"},
#               {"name":"Kari","DOJ":"2022-10-03","DOE":"2016-10-10"},
#               {"name":"Aari","DOJ":"2010-04-22","DOE":"2022-05-09"},
#               {"name":"Sari","DOJ":"2021-11-20","DOE":"2022-12-28"},
#               {"name":"wari","DOJ":"2000-12-29","DOE":"2000-01-17"},
#               {"name":"fari","DOJ":"1999-12-15","DOE":"1996-12-28"}]
#
# for record in emp_details:
#     joining_date = record["DOJ"]
#     Exit_date = record["DOE"]
#
#     DOJ_obj = datetime.strptime(joining_date, "%Y-%m-%d")
#     DOE_obj = datetime.strptime(Exit_date, "%Y-%m-%d")
#
#     if DOJ_obj < DOE_obj:
#         print(f"Its valid the joining date {DOJ_obj} is before the exit date {DOE_obj} ")
#     else:
#         print(f"Its invalid the joining date {DOJ_obj} is after the exit date {DOE_obj}")
#
# # Write a program to validate PAN (Permanent Account Number) format in India. A valid PAN should:
# #Be 10 characters long.Follow the pattern: 5 uppercase letters, 4 digits, 1 uppercase letter (e.g., ABCDE1234F)
# #Use regex to check validity and print whether each PAN is valid or not.
#
# emp_details =[{"name":"pari","PAN":"PARIN9999N"},
#               {"name":"Hari","PAN":"HARIN7766N"},
#               {"name":"Kari","PAN":"KARIN1425N"},
#               {"name":"Aari","PAN":"AarIN1237N"},
#               {"name":"Sari","PAN":"SARIN566N"},
#               {"name":"wari","PAN":"WARIN6644"},
#               {"name":"fari","PAN":"FARI2289f"}]
#
# for record in emp_details:
#     pan_no = record["PAN"]
#
#     if re.fullmatch(r"^[A-Z]{5}[0-9]{4}[A-Z]$",pan_no):
#         print(f"The pan number {pan_no} is valid ")
#     else:
#         print(f"The pan number {pan_no} is invalid ")

# emp_details =[{"name":"pari","AadharNumber":"333312498592"},
#               {"name":"Hari","AadharNumber":"98446783822222"},
#               {"name":"Kari","AadharNumber":"77778932822"},
#               {"name":"Aari","AadharNumber":"334445892899"},
#               {"name":"Sari","AadharNumber":"9949558999999"},
#               {"name":"wari","AadharNumber":"040433040221"},
#               {"name":"fari","AadharNumber":"224499249494"}]
#
# for record in emp_details:
#     a_no = record["AadharNumber"]
#
#     if len(a_no) == 12 and a_no.isdigit():
#         print(f"The Aadhar Number {a_no} is valid")
#     else:
#         print(f"The Aadhar Number {a_no} is invalid as it has {len(a_no)} digits")



# An employee code should follow the format EMP1234. Write a program to check if each employee code:
# Starts with "EMP,Followed by exactly 4 digits
#
# emp_details =[{"name":"pari","emp_code":"EMP1234"},
#               {"name":"Hari","emp_code":"EMO9689"},
#               {"name":"Kari","emp_code":"EMP8596"},
#               {"name":"Aari","emp_code":"EMP1968"},
#               {"name":"Sari","emp_code":"EP1295"},
#               {"name":"wari","emp_code":"EMMP124959"},
#               {"name":"fari","emp_code":"EMP13"}]
#
# for record in emp_details:
#     e_code = record["emp_code"]
# #
#
#     if re.fullmatch(r"^[EMP]{3}[0-9]{4}",e_code):
#         print(f"Its valid emp_code {e_code}")
#     else:
#         print(f"Its invalid emp_code {e_code}")

# Only emails from domains like gmail.com, yahoo.com, and company.com are allowed. Write a program to validate if email addresses belong to allowed domains.

emp_data = [
    {"name": "Alice", "email": "alice@gmail.com"},
    {"name": "sonu", "email": "sonu@yahoo.com"},
    {"name": "Ali", "email": "ali@company.com"},
    {"name": "sakku", "email": "sakku@firefor.com"},
    {"name": "Zeeshu", "email": "zee@explorer.com"}
]

for record in emp_data:
    emp_email = record["email"]

    if "gmail.com" in emp_email:
        print(f"its valid {emp_email}")
    elif "yahoo.com" in emp_email:
        print(f"its valid {emp_email}")
    elif "company.com" in emp_email:
        print(f"its valid {emp_email}")
    else:
        print(f"Its has invalid domain in email id {emp_email}")
# 4. Check for Leap Year in a List of Years
# Question:
# Given a list of joining years, write a program to print whether each year is a leap year or not.
#
from datetime import datetime
#
# emp_details =[{"name":"pari","DOJ":"2021-02-15"},
#               {"name":"Hari","DOJ":"2019-02-22"},
#               {"name":"Kari","DOJ":"2022-10-03"},
#               {"name":"Aari","DOJ":"2028-04-22"},
#               {"name":"Sari","DOJ":"2021-11-20"},
#               {"name":"wari","DOJ":"2000-12-29"},
#               {"name":"fari","DOJ":"2020-12-15"}]
#
# for record in emp_details:
#     joining_date = record ["DOJ"]
#     joining_date_obj = datetime.strptime(joining_date,"%Y-%m-%d")
#     year = (joining_date_obj.year)
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a Leap Year ✅")
#     else:
#             print(f"{year} is NOT a Leap Year ❌")


# 5. Validate PIN Code
# # Question:
# # A PIN code must be a 6-digit number and should not start with 0. Write a program to validate a list of PIN codes.
#
# emp_details =[{"name":"pari","pincode":"202102"},
#               {"name":"Hari","pincode":"201902"},
#               {"name":"Kari","pincode":"902210"},
#               {"name":"Aari","pincode":"02894"},
#               {"name":"Sari","pincode":"9801120"},
#               {"name":"wari","pincode":"984949"},
#               {"name":"fari","pincode":"09380999"}]
# for record in emp_details:
#     pin = str(record["pincode"])
#
#     if pin.isdigit() and len(pin) == 6 and pin[0] != '0':
#         print(f"Its valid pincode {pin}")
#     else:
#         print(f"its invalid pincode {pin} ")

# 6. Validate Product SKU Code
# Question:
# SKU code must be alphanumeric and exactly 8 characters. Write a program to check validity.
#
# 7. Validate Employee Name (Only Alphabets)
# Question:
# Write a program to ensure each employee name contains only alphabets (no numbers or special characters).
#
# 8. Check for Null/Empty Fields
# Question:
# Given employee records, write a program that checks for any empty or None fields (e.g., name, age, phone) and flags them.
#

# 10. Check Salary Within Range by Designation
# Question:
# Based on designation, validate salary range:
#
# Intern: < 15,000
#
# Executive: 15,000 – 40,000
#
# Manager: > 40,000
# Write a program that verifies if salaries are within expected ranges.
#
# 11. Validate Vehicle Registration Number
# Question:
# Registration number format: "MH12AB1234" → 2 letters (state), 2 digits (district), 2 letters, 4 digits. Validate such vehicle numbers.
#
# 12. Check Working Days Between Two Dates
# Question:
# Given DOJ and DOE, calculate total working days (excluding weekends) and flag if less than 30 days.
from datetime import datetime, timedelta
# emp_details =[{"name":"pari","DOJ":"2021-02-15","DOE":"2025-01-31"},
#               {"name":"Hari","DOJ":"2019-02-22","DOE":"2022-10-10"},
#               {"name":"Kari","DOJ":"2022-10-03","DOE":"2022-10-10"},
#               {"name":"Aari","DOJ":"2010-04-22","DOE":"2010-05-09"},
#               {"name":"Sari","DOJ":"2021-11-20","DOE":"2022-12-28"},
#               {"name":"wari","DOJ":"2000-12-29","DOE":"2002-01-17"},
#               {"name":"fari","DOJ":"1999-12-15","DOE":"2000-12-28"}]
#
# for record in emp_details:
#     doj = record["DOJ"]
#     doe = record["DOE"]
#
#     date_join_obj = datetime.strptime(doj,"%Y-%m-%d")
#     date_exit_obj = datetime.strptime(doe, "%Y-%m-%d")
#
#     # working_period = date_join_obj - date_exit_obj
#     working_period = date_exit_obj - date_join_obj
#     print(f"{record['name']} worked for {working_period.days} days")
#     # print(type(working_period))
#
#     if working_period.days < 30 :
#         print("Green Flag (Less than 30 days)")
#     else:
#         print("Red Flag (30 days or more)")



# Write a program that checks whether
# the given event date is in the future compared to today’s date.
now = datetime.now().date()  # Only the date part
print(f"Today's date: {now}")
even_date = input("Enter the event date in YYYY-MM-DD format: ")
even_date_obj = datetime.strptime(even_date,"%Y-%m-%d").date()
if even_date_obj > now:
    print(f"the given event date {even_date_obj} is in the future compared to today’s date {now}")
else:
    print(f"the given event date {even_date_obj} is not in the future compared to today’s date {now}")
# 13. Validate IFSC Code
# Question:
# An IFSC code must follow this pattern: 4 uppercase letters + 0 + 6 digits (e.g., HDFC0001234). Write a regex-based validator.
#
# 14. Check All Products Have a Category
# Question:
# In a product list, each product should have a non-empty category. Write a program to identify missing categories.
#
# 15. Validate GST Number (India)
# Question:
# GST format: 15 characters → 2 digits (state) + 10-character PAN + 1 entity code + 1 checksum. Write a validator using regex.
#
#



