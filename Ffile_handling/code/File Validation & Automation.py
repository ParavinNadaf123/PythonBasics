# 1. Verify That a Screenshot File Is Generated After Test Execution
# from selenium import webdriver
# import os
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.google.com")
#
# driver.save_screenshot("screenshots/google.png")
#
# if os.path.exists("screenshots/google.png"):
#     print("Screenshot saved successfully.")
# else:
#     print("Screenshot not generated.")
#
# driver.quit()

# 2. Read Expected Results from a File and Compare Them with Actual Results
# with open("expected.txt", "r") as file:
#     expected = file.read().strip()
#
# actual = "Login Successful"
#
# if expected == actual:
#     print("✅ Test Passed")
# else:
#     print("❌ Test Failed")
#     print("Expected:", expected)
#     print("Actual:", actual)
#
# # =============================================================
#
# with open("expected.txt", "r") as file:
#     expected_results = file.read().splitlines()
#
# actual_results = [
#     "Login Successful",
#     "Dashboard Displayed",
#     "Logout Successful"
# ]
#
# for expected, actual in zip(expected_results, actual_results):
#     if expected == actual:
#         print(f"PASS : {expected}")
#     else:
#         print(f"FAIL : Expected={expected}, Actual={actual}")
#
#
# # 3. Read Multiple Test Cases from a CSV File and Execute Them Sequentially
#
# import csv
#
# with open("testcases.csv", "r") as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         print("Executing:", row["TestCaseID"])
#         print("Username:", row["Username"])
#         print("Password:", row["Password"])
#
#         # Call your test function here
#         print("Test Executed Successfully\n")
#
# # 1. Read Browser Names from a Configuration File and Execute Tests
#
# def execute_test(browser):
#     print(f"Launching {browser} Browser...")
#     print(f"Executing test on {browser}")
#     print(f"Closing {browser}\n")
#
# with open("browsers.txt", "r") as file:
#     browsers = file.read().splitlines()
#
# for browser in browsers:
#     execute_test(browser)
#
#
# from selenium import webdriver
#
# with open("browsers.txt", "r") as file:
#     browsers = file.read().splitlines()
#
# for browser in browsers:
#
#     if browser.lower() == "chrome":
#         driver = webdriver.Chrome()
#
#     elif browser.lower() == "firefox":
#         driver = webdriver.Firefox()
#
#     elif browser.lower() == "edge":
#         driver = webdriver.Edge()
#
#     else:
#         print("Unsupported Browser:", browser)
#         continue
#
#     driver.get("https://www.google.com")
#     print(f"Test Executed on {browser}")
#     driver.quit()
# # 2. Extract All Email Addresses from a Text File Using Regular Expressions
#
# import re
#
# with open("data.txt", "r") as file:
#     data = file.read()
#
# emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", data)
#
# print("Email Addresses")
#
# for email in emails:
#     print(email)
#
# # Save Emails into Another File
# with open("data.txt","r") as file:
#     data = file.read()
#
# emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", data)
#
# with open("emails.txt","w") as f:
#     for email in emails:
#         f.write(email + "\n")
#
# print("Emails saved successfully.")
#
# # 3. Identify the Most Recently Modified File in a Directory
#
# import os
#
# folder = "."
#
# files = [os.path.join(folder, file) for file in os.listdir(folder)
#          if os.path.isfile(os.path.join(folder, file))]
#
# latest_file = max(files, key=os.path.getmtime)
#
# print("Latest Modified File:")
# print(latest_file)