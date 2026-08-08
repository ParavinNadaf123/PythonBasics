# a = int(input("enter the value  a: "))
# b= 20
# c=50
#
# if (a>=b and a>=c):
#     print("a is largets")
# elif (b>=a and b>=c):
#     print("b is greater")
# else:
#     print("c is greater")
#
# num = int(input("Enter the num:"))
# if (num < 0 ):
#     print("the number is negative")
# elif (num > 0):
#     print("the number is positive")
# else:
#     print("The number is zerro")
#
# #✅ 5. Check if a number is even or odd
#
# n = int(input("Enter the num :"))
# if (n%2==0):
#     print("The number is even")
# else:
#     print("The number odd")
#
# year = int(input("Enter the year :"))
# if (year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
#     print("The year is leap year ")
# else:
#     print("the is not leap year")
import re
# Write a program to validate username and password credentials.
# un = "pari"
# pw = "admin"
# username = input("Enter the username :")
# password = input("Enter the password:")
# if (username == un) and password == pw:
#     print("The username and password correct , successfully login")
# elif (username !=un and password !=pw):
#         print("Both username and password are incorrect")
# elif (username != un) :
#     print("Invalid username.")
# else:
#     print("Invalid password.")
#
# predefine_col_list = ["Name","Surname","age","gender","role","experience"]
#
#
# # Take input
# column_to_check = input("Enter the column names (comma separated): ")
#
# # Split input into list
# user_columns = column_to_check.split(",")
#
# invalid_columns = []
#
# # Check each column
# for col in user_columns:
#     col = col.strip()   # remove extra spaces
#
#     if col not in predefine_col_list:
#         invalid_columns.append(col)
#
# # Print result
# if len(invalid_columns) == 0:
#     print("All column names are valid and present in predefined list.")
# else:
#     print("These columns are not in predefined list:", invalid_columns)

# Name_list = ["pari","lolo","koko","momo"]
#
# name_to_check = input("Enter the name with comma separated: ")
#
# user_name_list = name_to_check.split(",")
# # print(user_name_list)
#
# invalid_name =[]
#
# for name in user_name_list:
#     name = name.strip()
#
#     if name not in Name_list:
#         invalid_name.append(name)
#
# if len(invalid_name) == 0 :
#     print("All  names are valid and present in predefined list.")
# else:
#     print("These names are not in predefined list:", invalid_name)
#
#
# items_avalible = ["somasa","pizza","burger","pani puri","vada pav","tea","coffee"]
#
# user_order = input("enter the items to order (seperated by comma): ")
#
# user_ordered_list = user_order.split(",")
#
# item_unavalible = []
#
# for item in user_ordered_list:
#     item= item.strip()
#     # print(item)
#
#     if item not in items_avalible:
#         item_unavalible.append(item)
#
# if len(item_unavalible) == 0:
#     print("All  items are valid and present in predefined list.")
# else:
#      print("These items are not avaliable:", item_unavalible)


# items_avalible = ["somasa","pizza","burger","pani puri","vada pav","tea","coffee"]
#
# user_order = input("enter the items to order (seperated by comma): ").split(",")
# print(user_order)

# user_ordered_list = user_order.split(",")
#
# item_unavalible = []
#
# for item in user_order:
#     item= item.strip()
#     # print(item)
#
#     if item not in items_avalible:
#         item_unavalible.append(item)
#
# if len(item_unavalible) == 0:
#     print("All  items are valid and present in predefined list.")
# else:
#      print("These items are not avaliable:", item_unavalible)
#
# age = int(input("eneter the age :"))
# if age <18 or age > 45:
#     print("not eligible for marathon")
# # else :
# #     print("eligible for marathon ")
# #
#
# emp_details =[{"name":"pari","phone_num":9999888877},
#               {"name":"Hari","phone_num":88769065433},
#               {"name":"Kari","phone_num":1123778766789},
#               {"name":"Aari","phone_num":8876659986},
#               {"name":"Sari","phone_num":887332445},
#               {"name":"wari","phone_num":"8837487K19"},
#               {"name":"fari","phone_num":2287768976}]
#
#
# #phone numbers: Must be 10 digits and only numeric.
# for record in emp_details:
#     emp_name = record["name"]
#     emp_con_num = record["phone_num"]
#     # print(type(emp_con_num))
#
#     if len(str(emp_con_num)) == 10 and str(emp_con_num).isnumeric():
#         print(f"valid contact number {emp_con_num}")
#     else:
#         print(f"Invalid number {emp_con_num}")


#
# item_price= [{"Prod_name":"table","Prod_price":20000,"discount":"20"},
#              {"Prod_name":"chair","Prod_price":2000,"discount":"10"},
#              {"Prod_name":"phone","Prod_price":9999,"discount":"50"},
#              {"Prod_name":"toy","Prod_price":200,"discount":"80"},
#              {"Prod_name":"necklace","Prod_price":500,"discount":"100"}
#              ]
#
# for record in item_price:
#     dicnt = record["discount"]
#     prodt = record["Prod_name"]
#     # print(dicnt)
#
#     if int(dicnt) <= 50 :
#         print(f"Its valid discount {dicnt}% for {prodt}")
#     else:
#         print(f"Its invalid discount {dicnt}% for {prodt} ")
#
#
#
# emp_details =[{"name":"pari","AadharNumber":"333312498592"},
#               {"name":"Hari","AadharNumber":"9844678QQ22222"},
#               {"name":"Kari","AadharNumber":"77778932822"},
#               {"name":"Aari","AadharNumber":"334445892899"},
#               {"name":"Sari","AadharNumber":"9949558999999"},
#               {"name":"wari","AadharNumber":"040433040221"},
#               {"name":"fari","AadharNumber":"224499249494"}
#                ]
#
#
# for record in emp_details:
#     a_num = record["AadharNumber"]
#     # print(a_num)
#
#     if len(a_num) == 12  and a_num.isdigit():
#         print(f"The AadharNumber {a_num} is valid")
#     else:
#         print(f"Its invalid AadharNumber {a_num}")
#
# import re
# emp_details =[{"name":"pari","PAN":"PARIN9999N"},
#               {"name":"Hari","PAN":"HARIN7766N"},
#               {"name":"Kari","PAN":"KARIN1425N"},
#               {"name":"Aari","PAN":"AarIN1237N"},
#               {"name":"Sari","PAN":"SARIN566N"},
#               {"name":"wari","PAN":"WARIN6644"},
#               {"name":"fari","PAN":"FARI2289f"}]
# for record in emp_details:
#     p_num = record["PAN"]
#
#     if re.fullmatch(r"^[A-Z]{5}[0-9]{4}[A-Z]$",p_num):
#         print(f"The pan number {p_num} is valid ")
#     else:
#         print(f"The pan number {p_num} is invalid ")
#
#
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
#
#     if re.fullmatch(r"^[EMP]{3}[0-9]{4}",e_code):
#         print(f"its valid employee code {e_code}")
#     else:
#         print(f"Its invalid employee code {e_code}")
#
# from datetime import datetime
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
#     join_date = record["DOJ"]
#     join_date_obj = datetime.strptime(join_date,"%Y-%m-%d")
#     date = (join_date_obj.date())
#     print(date)


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
# #         print("Red Flag (30 days or more)")
#
#
# # Step 1: Create country-currency mapping
# country_currency = {
#     "India": "INR",
#     "United States": "USD",
#     "Japan": "JPY",
#     "United Kingdom": "GBP",
#     "Australia": "AUD"
# }
#
# # Step 2: Take user input
# country = input("Enter country name: ").strip().title()
# currency = input("Enter currency code: ").strip().upper()
#
# # Step 3: Validation
# if country in country_currency:
#     if country_currency[country] == currency:
#         print("✅ Valid country and currency combination")
#     else:
#         print("❌ Invalid currency for", country)
# else:
#     print("❌ Country not found in system")

#
# # 23.	Write a program to validate tax percentage based on salary slabs.
#
# emp_sal_tax=[{"name":"pari","sal":45000,"tax":"5%"},
#              {"name":"zeeshu","sal":50000,"tax":"10%"},
#              {"name":"reshu","sal":1000000,"tax":"10%"},
#              {"name":"razia","sal":30000,"tax":"5%"},
#              {"name":"javed","sal":5000000,"tax":"20%"}]
#
# for record in emp_sal_tax:
#     emp_sal= record["sal"]
#     emp_tax= record["tax"]
#     name = record ["name"]
#
#     if emp_sal < 500000:
#         expected_tax = "5%"
#     elif emp_sal <= 1000000:
#         expected_tax = "10%"
#     else:
#         expected_tax = "20%"
#
#     if expected_tax == emp_tax:
#         print(f"✅ {name}: Tax is correct ({emp_tax})")
# #     else:
# #         print(f"❌ {name}: Tax is incorrect. Expected {expected_tax}, got {emp_tax}")
#
#
# # 24.	Write a program to verify invoice total (unit × unit_price = total_price).?
#
# item_data = [
#     {"name": "toys", "unit_price": 500,"unit":5,"total_Price":2500},
#     {"name": "table", "unit_price": 10000,"unit":1,"total_Price":10000},
#     {"name": "chair", "unit_price": 700,"unit":4,"total_Price":2800},
#     {"name": "cycel", "unit_price": 2500,"unit":2,"total_Price":5000},
#     {"name": "bike", "unit_price": 70000,"unit":1,"total_Price":7000}
#     ]
#
# for record in item_data:
#     unit_p = record["unit_price"]
#     total_p = record["total_Price"]
#     unit_n = record["unit"]
#     name = record["name"]
#
#
#
#     expected_total = unit_p * unit_n
#
#     if total_p == expected_total:
#         print(f"✅ {name}: Correct invoice total ({total_p})")
#     else:
#         print(f"❌ {name}: Incorrect invoice total. Expected {expected_total}, got {total_p}")
#
#
#
#
# from datetime import datetime, timedelta
# emp_details =[{"name":"pari","DOJ":"2021-02-15","DOE":"2025-01-31"},
#               {"name":"Hari","DOJ":"2019-02-22","DOE":"2022-10-10"},
#               {"name":"Kari","DOJ":"2023-10-03","DOE":"2022-10-10"},
#               {"name":"Aari","DOJ":"2010-04-22","DOE":"2010-04-22"},
#               {"name":"Sari","DOJ":"2021-11-20","DOE":"2022-12-28"},
#               {"name":"wari","DOJ":"2000-12-29","DOE":"2002-01-17"},
#               {"name":"fari","DOJ":"1999-12-15","DOE":"2000-12-28"}]
#
# for record in emp_details:
#     doj = record["DOJ"]
#     doe = record["DOE"]
#
#
#     doj_obj = datetime.strptime(doj,"%Y-%m-%d")
#     doe_obj = datetime.strptime(doe,"%Y-%m-%d")
#     # print(doj)
#     # print(doe)
#     # print(doj_obj)
#     if doj_obj < doe_obj:
#         print(f"date of joining {doj} is before date of exit {doe}")
#     elif doe_obj == doj_obj:
#         print(f" DOJ ({doj}) and DOE {doj} are same date")
#     else:
#         print(f"Invalid dates as date of joining {doj} is after date of exit {doe} ")
#
#
#
# emp_data = [
#     {"name": "Alice", "email": "alice@gmail.com"},
#     {"name": "sonu", "email": "sonu@yahoo.com"},
#     {"name": "Ali", "email": "ali@company.com"},
#     {"name": "sakku", "email": "sakku@firefor.com"},
#     {"name": "Zeeshu", "email": "zee@explorer.com"}
# ]
#
# for record in emp_data:
#     emp_email = record["email"]
#
#     if ("gmail.com")  in emp_email:
#         print(f"its valid {emp_email}")
#     elif "yahoo.com" in emp_email:
#         print(f"its valid {emp_email}")
#     elif "company.com" in emp_email:
#         print(f"its valid {emp_email}")
#     else:
#         print(f"Its has invalid domain in email id {emp_email}")
#
# now = datetime.now().date()
# print(now)
#
# event_date = input("Enter the event date in DD-MM-YY formate: ")
# event_date_obj = datetime.strptime(event_date,"%d-%m-%Y").date()
# if event_date_obj > now:
#     print(f"The event date {event_date_obj} is future date compared to today date {now}")
# else:
#     print(f"The event date {event_date_obj} is not future date compared to today date {now}")

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
#
# emp_details =[{"name":"pari","Designation":"Intern","Salary":"20000"},
#               {"name":"Hari","Designation":"Executive","Salary":"30000"},
#               {"name":"Kari","Designation":"Intern","Salary":"15000"},
#               {"name":"Aari","Designation":"Manager","Salary":"50000"},
#               {"name":"Sari","Designation":"Manager","Salary":"45000"}]
#
# for record in emp_details:
#     emp_designation = record ["Designation"]
#     emp_name = record ["name"]
#     emp_sal = record ["Salary"]
#
#     if emp_designation == "Manager":
#         if int(emp_sal)  > 40000:
#             print(f"✅ {emp_name}: Salary is correct for {emp_designation}")
#         else:
#             print(f"✅ {emp_name}: Salary out of range  correct for {emp_designation}")
#
#     elif emp_designation == "Executive":
#         if int(emp_sal) > 15000 and int(emp_sal) <40000:
#             print(f"✅ {emp_name}: Salary is correct for {emp_designation}")
#         else:
#             print(f"✅ {emp_name}: Salary out of range  correct for {emp_designation}")
#     elif emp_designation == "Intern":
#         if int(emp_sal) < 15000:
#             print(f"✅ {emp_name}: Salary is correct for {emp_designation}")
#         else:
#             print(f"✅ {emp_name}: Salary out of range  correct for {emp_designation}")
#
#     else:
#             print(f"⚠ {emp_name}: Unknown designation")


 # 13. Validate IFSC Code
# Question:
# An IFSC code must follow this pattern: 4 uppercase letters + 0 + 6 digits (e.g., HDFC0001234). Write a regex-based validator.
emp_details = [
    {"name": "pari", "ifsc": "SBIN0001234"},
    {"name": "hari", "ifsc": "sbin0001234"},
    {"name": "kari", "ifsc": "SBIN00012345"},
    {"name": "aari", "ifsc": "SBI0001234"},
    {"name": "sari", "ifsc": "SBIN1001234"}
]

for record in emp_details:
    IFSC = record ["ifsc"]
    emp_name = record ["name"]

    if re.fullmatch(r"^[A-Z]{4}0[0-9]{6}$",IFSC):
        print(f"The ifsc number {IFSC} is valid ")
    else:
        print(f"The ifsc number {IFSC} is invalid ")




products = [
    {"id": 101, "name": "Laptop", "category": "Electronics"},
    {"id": 102, "name": "Shoes", "category": "Fashion"},
    {"id": 103, "name": "Coffee Mug", "category": ""},
    {"id": 104, "name": "Notebook", "category": "Stationery"},
    {"id": 105, "name": "Water Bottle", "category": None},
    {"id": 106, "name": "Headphones", "category": "Electronics"},
    {"id": 107, "name": "Backpack"},
    {"id": 108, "name": "Smartphone", "category": "Electronics"},
    {"id": 109, "name": "T-shirt", "category": "Fashion"},
    {"id": 110, "name": "Desk Lamp", "category": "Home Decor"}
]

invalid_products =[]

for record in products:
    p_id = record["id"]
    p_name = record["name"]
    p_category = record.get("category")



    if "category" not in record:
        invalid_products.append(record)
        print(f"❌ {p_name}: Category field missing")
    elif p_category is  None :
        invalid_products.append(record)
        print(f"❌ {p_name}: Category is None")
    elif p_category == "":
        invalid_products.append(record)
        print(f"❌ {p_name}: Category is empty")


        if invalid_products == []:
            print("All products have valid category")
        else:
            print("\nlist of products with missing category")
            for item in invalid_products:
                print(item)



emp_details = [
    {"name": "pari", "ifsc": "SBIN0001234"},
    {"name": "hari", "ifsc": "sbin0001234"},
    {"name": "kari", "ifsc": "SBIN00012345"},
    {"name": "aari", "ifsc": "SBI0001234"},
    {"name": "sari", "ifsc": "SBIN1001234"}
]

for record in emp_details:
    IFSC = record ["ifsc"]
    emp_name = record ["name"]

    if re.fullmatch(r"^[A-Z]{4}0[0-9]{6}$",IFSC):
        print(f"The ifsc number {IFSC} is valid ")
    else:
        print(f"The ifsc number {IFSC} is invalid ")