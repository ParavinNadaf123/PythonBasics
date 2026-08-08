# #check the input creds
# from locale import currency
#
# username=str(input("enter the username:"))
# password =str(input("enter the password:"))
# if (username == "admin" and password == "admin123"):
#     print("valid username and password , Login successfull")
# elif (username !="admin"):
#     print("invalid username")
# elif(password !="admin123"):
#     print("invalid password")
# else:
#     print("login failed")
#
#
# # required_columns_names=["name","surname","id","age","email"]
# # column_names=list(input("enter the cloumn name to check:"))
# #
# # column_names = [col.strip() for col in/ column_input.split(",")]
# #
# #
# # if (column_names in required_columns_names):
# #     print("the column name check is passed")
# # else:
# #     print("the cloumn name check is failed")
#
# required_columns_names = ["name", "surname", "id", "age", "email"]
#
# # User enters comma-separated column names
# column_input = input("Enter the column names to check (comma separated): ")
#
# # Convert input string to a list and strip spaces
# column_names = [col.strip() for col in column_input.split(",")]
#
# # Check for missing columns
# missing_columns = [col for col in column_names if col not in required_columns_names]
#
# if not missing_columns:
#     print("✅ All column name checks passed.")
# else:
#     print("❌ Column check failed. Missing or invalid columns:", missing_columns)
#
# age= int(input("enter the age :"))
#
# if age > 0 and age <=120:
#     print("valid age ")
# else:
#     print("Invalid age")
#
# data = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": -5},
#     {"name": "Charlie", "age": 130},
#     {"name": "David", "age": 45}
# ]
#
# for record in data:
#     age = record["age"]
#
#     if age < 0:
#         print(f"{record['name']} → Invalid Age (Negative value: {age})")
#     elif age > 120:
#         print(f"{record['name']} → Invalid Age (Too high: {age})")
#     else:
#         print(f"{record['name']} → Valid Age ({age})")
#
#
# from datetime import datetime
# dates = ["2024-06-19", "2023-02-30", "2022-12-15", "19-06-2024", "2024-6-1"]
# for date_str in dates:
#     try:
#         # Try to parse using the correct format
#         datetime.strptime(date_str, "%Y-%m-%d")
#         print(f"{date_str} →  Valid format")
#     except ValueError:
#         print(f"{date_str} → Invalid format")
#
# data2 = [
#     {"country": "india","currency":"INR"},
#     {"country": "india","currency":"INR"},
#     {"country": "USA","currency":"USD"},
#     { "country": "USA","currency":"USD"}
# ]
#
# for country_record in data2:
#     country = country_record["country"]
#     currency= country_record["currency"]
#     if country == "india":
#         if currency == "INR":
#             print(f"{country} currency is correct i.e,  INR")
#         else:
#             print(f"{country} currency is incorrect")
#
#     elif country == "USA":
#         if currency == "USD":
#             print(f"{country} currency is correct i.e, USD")
#         else:
#             print(f"{country} currency is incorrect")
#
# #     else:
# #         print(f"{country} → Unknown country. No currency rule defined")
# #
# #
# emp_data = [
#     {"name": "pari","id":"123"},
#     {"name": "reshu","id":"989"},
#     {"name": "sita","id":"222"},
#     { "name": "gita","id":"343"},
#     { "name": "ram","id":"123"}
# ]
# seen_ids=set()
# duplicate_ids=[]
# for record_emp_id in emp_data:
#     emp_id = record_emp_id["id"]
#
#     if emp_id in seen_ids:
#         print(f"❌ Duplicate ID found: {emp_id}")
#         duplicate_ids.append(emp_id)
#     else:
#         seen_ids.add(emp_id)
#
# if not duplicate_ids:
#     print("✅ All IDs are unique.")
# else:
#     print(f"⚠️ Duplicates found: {set(duplicate_ids)}")
# #
#
# emp_salary_data = [
#     {"name": "pari","salary":45},
#     {"name": "reshu","salary":60},
#     {"name": "sita","salary":-20},
#     { "name": "gita","salary":30},
#     { "name": "ram","salary":00}
# ]
#
# for record in emp_salary_data:
#     emp_salary = record["salary"]
#     emp_name =record["name"]
#
#     if emp_salary == 0 or emp_salary < 0:
#         print(f"{emp_name} have {emp_salary}  and it is InValid Salary ")
#     else:
#          print(f"{emp_name} have {emp_salary}  and it is Valid Salary ")
#
#
emp_sal_tax=[{"name":"pari","sal":45000,"tax":"5%"},
             {"name":"zeeshu","sal":50000,"tax":"10%"},
             {"name":"reshu","sal":1000000,"tax":"10%"},
             {"name":"razia","sal":30000,"tax":"5%"},
             {"name":"javed","sal":5000000,"tax":"20%"}]

for record in emp_sal_tax:
    emp_sal= record["sal"]
    emp_tax= record["tax"]
    name = record ["name"]

    if emp_sal < 500000:
        expected_tax = "5%"
    elif emp_sal <= 1000000:
        expected_tax = "10%"
    else:
        expected_tax = "20%"

    if expected_tax == emp_tax:
        print(f"✅ {name}: Tax is correct ({emp_tax})")
    else:
        print(f"❌ {name}: Tax is incorrect. Expected {expected_tax}, got {emp_tax}")


# Step 1: Define salary slabs
tax_slabs = [
    {"min": 0, "max": 300000, "rate": 0},
    {"min": 300001, "max": 600000, "rate": 5},
    {"min": 600001, "max": 900000, "rate": 10},
    {"min": 900001, "max": 1200000, "rate": 15},
    {"min": 1200001, "max": 1500000, "rate": 20},
    {"min": 1500001, "max": float("inf"), "rate": 30}
]

# Step 2: Take input
salary = float(input("Enter salary: "))
given_tax = float(input("Enter tax percentage applied: "))

# Step 3: Validation logic
expected_tax = None

for slab in tax_slabs:
    if slab["min"] <= salary <= slab["max"]:
        expected_tax = slab["rate"]
        break

# Step 4: Compare and print result
if expected_tax is None:
    print("Invalid salary entered.")
elif given_tax == expected_tax:
    print("✅ Valid tax percentage for this salary slab.")
else:
    print(f"❌ Invalid tax percentage. Expected tax is {expected_tax}%.")


