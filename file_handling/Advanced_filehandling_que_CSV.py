# CSV
# # Read test data from a CSV file and print username–password pairs.
# import csv
# with open("demo.csv","r") as f:
#     reader = csv.reader(f)
#
#     next(reader)    #Skip the header row
#
#     for username,password in reader:
#         print(f"username : {username} | password :{password}")
# # Validate that every row in a CSV file contains the required number of columns.
# import csv
#
# with open("employees.csv", "r") as f:
#     reader = csv.reader(f)
#
#     required_columns = 4
#
#     for row_number, row in enumerate(reader, start=1):
#         print(len(row))
#
#         if len(row) == required_columns:
#             print(f"Row {row_number}: Valid")
#         else:
#             print(f"Row {row_number}: Invalid")
#
#
#
# # Read a CSV file and calculate the average of a numeric column.
#     import csv
#
#     import csv
#
#     with open("employees.csv", "r") as f:
#         reader = csv.DictReader(f)
#
#         total_salary = 0
#         count = 0
#
#         for row in reader:
#             if row["Salary"]:  # Check Salary is not empty
#                 salary = int(row["Salary"])
#
#                 total_salary += salary
#                 count += 1
#
#     if count > 0:
#         average = total_salary / count
#         print(f"Average Salary: {average}")
#     else:
#         print("No salary data available")
#
#
# # Generate a CSV report containing Test Name, Status, and Execution Time.
# import csv
# from datetime import datetime
# test_results = [
#     ("Login Test", "PASS"),
#     ("Search Test", "FAIL"),
#     ("Checkout Test", "PASS"),
#     ("Profile Test", "PASS")
# ]
#
# with open("test_report.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#
#     writer.writerow(["Test Name", "Status", "Execution Time"])
#
#     for test_name, status in test_results:
#         execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         writer.writerow([test_name, status, execution_time])
#
# print("CSV report generated successfully!")
# # Convert a CSV file into a JSON file.
# import csv
# import json
# data = []
# with open("employees.csv","r") as csv_file:
#     reader = csv.DictReader(csv_file)
#
#     for row in reader:
#         data.append(row)
#
#
# # Write JSON file
# with open("employees.json", "w") as json_file:
#     json.dump(data, json_file, indent=4)
#
# print("CSV converted to JSON successfully!")
# # Convert a JSON file into a CSV file.

import json
import csv

# Read JSON file
with open("employees.json", "r") as json_file:
    data = json.load(json_file)

# Write CSV file
with open("employees.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

    writer.writeheader()
    writer.writerows(data)

print("JSON converted to CSV successfully!")