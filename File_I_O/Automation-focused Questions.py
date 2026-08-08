# Read test data from a file and print username-password pairs.
#
# import csv
# with open("user.csv","r") as f:
#     reader = csv.reader(f)
#     next(reader) #skip header row
#
#     for username,password in reader:
#         print(f"Username: {username} | Password: {password}")
# Write automation logs into a file with status (PASS/FAIL).
#
# import logging
#
# logging.basicConfig(
#     filename="automation_log.txt",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
#
# )
#
# def log_status(test_name, status, details=""):
#     if status.upper() == "PASS":
#         logging.info(f"{test_name} - PASS - {details}")
#     else:
#         logging.error(f"{test_name} - FAIL - {details}")
#
# log_status("Login Test", "PASS", "User logged in successfully")
# log_status("Checkout Test", "FAIL", "Button not clickable")
# log_status("Search Test", "PASS")
# log_status("Profile Update Test", "FAIL", "500 server error")
# Check if a screenshot file is generated after a test run.
# 👉 Hint: os.path.exists()
#
# import os
#
# screenshot_path = "screenshots/login_failure.png"
#
# if os.path.exists(screenshot_path):
#     print("✅ Screenshot generated successfully")
# else:
#     print("❌ Screenshot NOT generated")
# Read expected results from a file and compare with actual results.
#
# expected_results = {} #🔹 Step 1: Create an empty dictionary
#
# with open("expected.txt","r") as f:
#     for line in f:
#         test,result = line.strip().split("=")
#         expected_results[test]= result
#
# actual_results = {
#     "Login Test": "SUCCESS",
#     "Search Test": "FAIL",
#     "Checkout Test": "FAIL"
# }
#
# for test_name, expected in expected_results.items():
#     actual = actual_results.get(test_name)
#
#     if actual == expected:
#         print(f"{test_name} : PASS")
#     else:
#         print(f"{test_name} : FAIL (Expected: {expected}, Actual: {actual})")
#
# # Generate a CSV report of test results (test name, status, time).
# #
# import csv
# from datetime import datetime
#
# # Test results (normally from automation execution)
# test_results = [
#     ("Login Test", "PASS"),
#     ("Search Test", "FAIL"),
#     ("Checkout Test", "PASS")
# ]
#
# # Open CSV file in write mode
# with open("test_report.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#
#     # Write header row
#     writer.writerow(["Test Name", "Status", "Execution Time"])
#
#     # Write test result rows
#     for test_name, status in test_results:
#         execution_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         writer.writerow([test_name, status, execution_time])
#
# print("✅ CSV test report generated successfully")

# Read an API response stored in a JSON file and validate field values.
#
import json

with open("json files/api_response.json", "r") as file:
    response_data = json.load(file) #json.load() converts JSON → Python dictionary.
    # print(respond_data)

expected_values ={
    "name": "John",
    "status": "active"
}

for field,expected in expected_values.items():
    actual = response_data.get(field)

    if actual == expected:
        print(f"{field} validation PASS")
    else:
        print(f"{field} validation FAIL (Expected: {expected}, Actual: {actual})")
# Extract all email IDs from a text file.
# 👉 Hint: regex + file read
#

import re

# Step 1: Read file content
with open("txt files/data.txt", "r") as f:
    text = f.read()
    # print(text)

# Step 2: Define regex pattern for email
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Step 3: Find all email IDs
emails = re.findall(email_pattern, text)
# print(emails)

# Step 4: Print extracted emails
for email in emails:
    print(email)

# Read error logs and print only the lines with “ERROR”.
#
# Write a program to rotate log files (log1 → log2 → log3).
#
# Create a script to clean up temporary files older than 7 days.
# 👉 Hint: check file modification time