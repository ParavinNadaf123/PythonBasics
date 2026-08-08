import logging
#
# logging.basicConfig(
#     filename="automation.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
#
#
# test_result = "PASS"
#
# if test_result == "PASS":
#     logging.info("Login Test Case : PASS")
# else:
#     logging.error("Login Test Case : FAIL")
#
# print("Logs written successfully.")
#
#
# test_result = "FAIL"
#
# if test_result == "PASS":
#     logging.info("Login Test Case : PASS")
# else:
#     logging.error("Login Test Case : FAIL")


# 2. Record Every Program Execution with Timestamps

import logging
#
# logging.basicConfig(
#     filename="execution.log",
#     level=logging.INFO,
#     format="%(asctime)s  - %(message)s"
# )
#
# logging.info("Program Started")
#
# print("Executing Program...")
#
# logging.info("Program Completed")


# 3. Read a Log File and Display Only ERROR Entries
#
# with open("automation.log", "r") as file:
#
#     for line in file:
#
#         if "ERROR" in line:
#             print(line.strip())
#
# # 4. Rotate Log Files (log1 → log2 → log3)
# #
# # import logging
# # from logging.handlers import RotatingFileHandler
# #
# # logger = logging.getLogger("AutomationLogger")
# # logger.setLevel(logging.INFO)
# #
# # handler = RotatingFileHandler(
# #     "automation.log",
# #     maxBytes=500,
# #     backupCount=3
# # )
# #
# #
# # formatter = logging.Formatter(
# #     "%(asctime)s - %(levelname)s - %(message)s"
# # )
# #
# # handler.setFormatter(formatter)
# # logger.addHandler(handler)
# #
# # for i in range(50):
# #     logger.info(f"Executing Test Case {i + 1}")
#
#
# # 1. Archive Old Log Files into a Backup Folder
#
# import logging
# import shutil
# from pathlib import Path
# from logging.handlers import RotatingFileHandler
#
#
# # ============================================================
# # 1. PROJECT PATHS
# # ============================================================
#
# # Get the folder where Logging_practice.py is located
# BASE_DIR = Path(__file__).resolve().parent
#
# LOG_DIR = BASE_DIR / "logs"
# BACKUP_DIR = BASE_DIR / "backup"
# REPORT_DIR = BASE_DIR / "reports"
#
# LOG_FILE = LOG_DIR / "automation.log"
# REPORT_FILE = REPORT_DIR / "test_report.txt"
# FAILED_FILE = REPORT_DIR / "failed_tests.txt"
#
#
# # ============================================================
# # 2. CREATE REQUIRED FOLDERS
# # ============================================================
#
# LOG_DIR.mkdir(exist_ok=True)
# BACKUP_DIR.mkdir(exist_ok=True)
# REPORT_DIR.mkdir(exist_ok=True)
#
#
# # ============================================================
# # 3. LOGGER CONFIGURATION
# # ============================================================
#
# logger = logging.getLogger("AutomationLogger")
# logger.setLevel(logging.INFO)
#
# # Prevent duplicate handlers if code is executed multiple times
# logger.handlers.clear()
#
# handler = RotatingFileHandler(
#     LOG_FILE,
#     maxBytes=2000,
#     backupCount=3
# )
#
# formatter = logging.Formatter(
#     "%(asctime)s - %(levelname)s - %(message)s"
# )
#
# handler.setFormatter(formatter)
#
# logger.addHandler(handler)
#
#
# # ============================================================
# # 4. EXECUTE TEST CASES
# # ============================================================
#
# test_cases = [
#     ("TC001", "Login Test", "PASS"),
#     ("TC002", "Logout Test", "PASS"),
#     ("TC003", "Search Test", "FAIL"),
#     ("TC004", "Payment Test", "PASS"),
#     ("TC005", "Profile Test", "FAIL")
# ]
#
#
# for test_id, test_name, status in test_cases:
#
#     if status == "PASS":
#         logger.info(f"{test_id} - {test_name} - PASS")
#
#     else:
#         logger.error(f"{test_id} - {test_name} - FAIL")
#
#
# # ============================================================
# # 5. GENERATE SUMMARY REPORT
# # ============================================================
#
# pass_count = 0
# fail_count = 0
#
# failed_tests = []
#
#
# with open(LOG_FILE, "r") as file:
#
#     for line in file:
#
#         if " - PASS" in line:
#             pass_count += 1
#
#         elif " - FAIL" in line:
#             fail_count += 1
#
#             # Extract test case name
#             message = line.split(" - ", 1)[1]
#
#             failed_test = message.replace(" - FAIL", "").strip()
#
#             failed_tests.append(failed_test)
#
#
# total_tests = pass_count + fail_count
#
#
# # ============================================================
# # 6. WRITE SUMMARY REPORT
# # ============================================================
#
# with open(REPORT_FILE, "w") as file:
#
#     file.write("TEST EXECUTION SUMMARY\n")
#     file.write("======================\n")
#     file.write(f"Total Test Cases : {total_tests}\n")
#     file.write(f"PASS             : {pass_count}\n")
#     file.write(f"FAIL             : {fail_count}\n")
#
#
# # ============================================================
# # 7. WRITE FAILED TEST CASES
# # ============================================================
#
# with open(FAILED_FILE, "w") as file:
#
#     for test in failed_tests:
#         file.write(test + "\n")
#
#
# # ============================================================
# # 8. DISPLAY RESULTS
# # ============================================================
#
# print("Test execution completed.")
# print()
# print("Total Test Cases :", total_tests)
# print("PASS             :", pass_count)
# print("FAIL             :", fail_count)
#
# print()
# print("Report generated :", REPORT_FILE)
# print("Failed tests      :", FAILED_FILE)


