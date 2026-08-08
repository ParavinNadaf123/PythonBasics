from datetime import datetime

import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

#
# # Here’s what it means:
# #
# # datetime.datetime: Refers to the datetime class inside the datetime module.
# #
# # .now(): Is a function (or method) that returns the current date and time
#
# import datetime
#
# # get current date
current_date = datetime.date.today()
#
print(current_date)
#
#
#
# import datetime
#
print(dir(datetime))
#
# # Among all the attributes of datetime module, the most commonly used classes in the datetime module are:
# #
# # datetime.datetime - represents a single point in time, including a date and a time.
# # datetime.date - represents a date (year, month, and day) without a time.
# # datetime.time - represents a time (hour, minute, second, and microsecond) without a date.
# # datetime.timedelta - represents a duration, which can be used to perform arithmetic with datetime objects.

d = datetime.date(2022,3,3)
print(d)
#
from  datetime import  date
#
# d =date(2022,9,8)
# print(d)
#
todays_date = date.today()
print(todays_date)
#
# print(date.today().month)
# print(date.today().year)
# print(date.today().day)
#
# from  datetime import  time
#
# a=time()
# print(a)
#
# b= time(11,59,6,40000)
# print(b)
# from datetime import datetime
# c= datetime(2022,12,3)
# print(c)
#
# e = datetime(2021,2,3,23,55,59,999)
# print(e)
#
# from datetime import datetime
#
# f = datetime(2022, 12, 28, 23, 55, 59, 342380)
#
# print("Year =", f.year)
# print("Month =", f.month)
# print("Hour =", f.hour)
# print("Minute =", f.minute)
# print("Timestamp =", f.timestamp())
#
#
# t1 = date(year = 2022, month=2,day=7)
# t2 = date(year=2022,month=12,day=21)
# t3 = t1-t2
# print("t3 =",t3)
# print(type(t3))
#
# # using datetime()
# t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)
#
#
# print("Type of t3 =", type(t3))
# print("Type of t6 =", type(t6))
#
#
# from datetime import timedelta
#
# ta = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
# tb= timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
#
# tc = ta - tb
#
# print("tc =", tc)
# print(tc.total_seconds())
#
# # Python format datetime
# # The way date and time are represented may be different in different places,
# # organizations, etc. It's more common to use mm/dd/yyyy in the US,
# # whereas dd/mm/yyyy is more common in the UK.
# #
# # Python has strftime() and strptime() methods to handle this.
# #
# # Python strftime() Method
# # The strftime() method is defined under classes date, datetime and time.
# # The method creates a formatted string from a given date, datetime or time object.
# #
# # Let's see an example.
# # =====================#==	Format a datetime → string
# now = datetime.now()
# print(now)
#
# t = now.strftime("%H:%M:%S")
# print(t)
#
# s1 = now.strftime("%y/%m/%d")
# print("s1 =",s1)
#
# s2 = now.strftime("%d-%m-%y, %H:%M:%S")
# print("s2 = ",s2)
#
# timestamp = 12120144
# date_time = datetime.fromtimestamp(timestamp)
#
# print("Date time object :", date_time)
#
# d= date_time.strftime("%B")
# print(d)
#
#  # Python strptime() Method
# # The strptime() method creates a datetime object
# # from a given string (representing date and time).
#
# #================================Parse a string → datetime object
# from datetime import datetime
#
# date_string = "25 December, 2022"
# print("date_string =", date_string)
#
# # use strptime() to create date object
# date_object = datetime.strptime(date_string, "%d %B, %Y")
#
# print("date_object =", date_object)
#
# date_str = "03 October, 1993"
# print("date_string :",date_str)
#
# date_str_obj = date_time.strptime(date_str,"%d %B, %Y")
# print("date_str_obj :",date_str_obj)
#
#
# dt_string = "12/11/2018 09:15:32"
# date_st = date_time.strptime(dt_string,"%d/%m/%Y %H:%M:%S")
# print("Date stirng = ",date_st)
#
# date_obj = date_time.strptime(dt_string,"%m/%d/%Y %H:%M:%S")
# print(date_obj)
#
#
# Get today’s date. Write a program to print the current date in YYYY-MM-DD format.
# from datetime import datetime
#
# todays_date= datetime.now()
# print(todays_date)
#
# # Get current time. Print the current time in HH:MM:SS format.
# now= datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print(current_time)
# # Get full date & time. Show the current timestamp like: 25-07-2025 14:30:00.
# now = datetime.now()
# formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
# print(formatted_date)
# # Extract parts of date, From today’s date, print only:Year,Month,Day
#
# f = datetime(2022, 12, 28, 23, 55, 59, 342380)
# #
# print("Year =", f.year)
# print("Month =", f.month)
# print("day =", f.day)
#
# #
# # Check if today is weekend. Print whether today is a weekday or weekend.
#
# now = datetime.now()
# formatted_date = now.strftime("%A")
# print(formatted_date)
# if formatted_date == "sunday" or formatted_date == "saturday":
#     print("Its weekend")
# else:
#     print("its not weekend")
#
#
# d1 = input("Enter the date d1:")
# d2 = input("Enter the date d2:")
# try:
#     d1_obj = datetime.strptime(d1,"%Y-%m-%d")
#     print("date 1",d1_obj)
#     d2_obj = datetime.strptime(d2,"%Y-%m-%d")
#     print("date 2 ",d2_obj)
#
#     if d1_obj < d2_obj:
#         print(f"date 1  {d1_obj} is earlier")
#     elif d2_obj < d1_obj:
#         print(f"date 2 {d2_obj} is earlier")
#     else:
#         print("Both are same.")
#
# except ValueError:
#     print("❌ Invalid date format. Please use YYYY-MM-DD (e.g., 2023-07-25).")


# d3 = input("Enter the date in yyyy/mm/dd :")
# d4 = input("Enter the date in yyyy/mm/dd :")
# try:
#     d3_obj= datetime.strptime(d3,"%Y-%m-%d")
#     d4_obj = datetime.strptime(d4,"%Y-%m-%d")
#
#     diff = d3_obj - d4_obj
#     print(diff)
#     no_of_days = abs(diff.days)
#     print(f"no_of_days between {d3} and {d4} is :, {no_of_days} days")
#
# except ValueError:
#     print("❌ Invalid date format. Please use YYYY-MM-DD (e.g., 2023-07-25).")
from datetime import datetime, timedelta

# d1 = input("Enter the date in YYYY-MM-DD:")
# try:
#     d1_obj = datetime.strptime(d1,"%Y-%m-%d")
#     no_of_days=int(input("Enter the no of days to add to date :"))
#
#     days_to_add = timedelta(days=no_of_days)
#
#     new_date = d1_obj + days_to_add
#     print(f"\nOriginal date: {d1_obj.strftime('%Y-%m-%d')}")
#     print(f"New date after adding {no_of_days} days: {new_date.strftime('%Y-%m-%d')}")
#
# except ValueError:
#     print("❌ Invalid input. Please make sure the date is in YYYY-MM-DD format and days is a number.")

#
# date =  input("Enter a date (e.g., 28 December 2022): ")
#
# try:
#
#     date_obj = datetime.strptime(date,"%d %B %Y")
#     print(type(date_obj))
#     formate_date = datetime.strftime(date_obj,"%Y-%m-%d")
#
#     print(f"The formatted date is ",formate_date)
#
#     print(type(formate_date))
#
# except ValueError:
#     print("❌ Invalid date format. Please enter the date as '28 December 2022'")
#
# current_date = datetime.now()
# print(current_date)
#
# print(current_date.year)
#
# next_year = current_date.year + 1  # → 2026
# print(next_year)
#
# new_year = datetime(next_year, 1, 1)
# print(new_year)
#
# time_left = new_year - current_date
# print(time_left)
#
# # Extract total seconds
# total_seconds = time_left.total_seconds()
#
# # Convert to days, hours, minutes, seconds
# days = time_left.days
# hours = int((total_seconds % (24 * 3600)) // 3600)
# minutes = int((total_seconds % 3600) // 60)
# seconds = int(total_seconds % 60)
#
# # Print the countdown
# print(f"⏳ Time left until New Year ({next_year}-01-01):")
# print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
#
# import calendar
#
# now = datetime.now()
# print(now)
#
# current_year = now.year
# print(current_year)
#
# current_month = now.month
# print(current_month)
#
# current_month_cal = calendar.month(current_year, current_month)
# print(current_month_cal)


# from datetime import datetime, timedelta
#
# # 1. Get user input
# d1 = input("Enter the dates d1 in YYYY-MM-DD format: ")
# d2 = input("Enter the dates d2 in YYYY-MM-DD format: ")
#
# try:
#     # 2. Convert input strings into datetime objects
#     start_date = datetime.strptime(d1, "%Y-%m-%d")
#     end_date = datetime.strptime(d2, "%Y-%m-%d")
#
#     # 3. Ensure start_date is before end_date
#     if start_date > end_date:
#         start_date, end_date = end_date, start_date  # Swap if necessary
#
#     # 4. Initialize counter for workdays
#     workdays = 0
#     current = start_date
#
#     # 5. Loop through each day between the two dates
#     while current <= end_date:
#         if current.weekday() < 5:  # 0=Monday, 1=Tuesday, ..., 4=Friday
#             workdays += 1
#         current += timedelta(days=1)  # Move to the next day
#
#     # 6. Print result
#     print(f"Workdays between {d1} and {d2}: {workdays}")
#
# except ValueError:
#     print("❌ Invalid date format. Use YYYY-MM-DD.")
# ///////////////////
# import time
# future_date_time = input("enter a future date and time (e.g., 2025-08-01 12:00:00):")
#
# try:
#     target_time = datetime.strptime(future_date_time,"%Y-%m-%d %H:%M:%S")
#
#     if target_time <= datetime.now():
#         print("❌ The entered time is not in the future.")
#     else:
#         print(f"\n⏳ Countdown to {target_time} has started...\n")
#
#         while True:
#                     now = datetime.now()
#                     if now >= target_time:
#                         print("🎉 Time's up! The countdown has finished.")
#                         break
#
#                     # Calculate the time difference
#                     time_left = target_time - now
#                     total_seconds = int(time_left.total_seconds())
#
#                     # Convert to days, hours, minutes, seconds
#                     days = total_seconds // 86400
#                     hours = (total_seconds % 86400) // 3600
#                     minutes = (total_seconds % 3600) // 60
#                     seconds = total_seconds % 60
#
#                     # Print countdown, overwrite previous line
#                     print(f"\rTime left: {days}d {hours:02}h {minutes:02}m {seconds:02}s", end="")
#
#                     # Wait 1 second
#                     time.sleep(1)
#
# except ValueError:
#             print("❌ Invalid format. Please use YYYY-MM-DD HH:MM:SS (e.g., 2025-08-01 12:00:00).")
#
#
from datetime import datetime
import pytz

# 1. Get current local time
# local_time = datetime.now()
# print("Local time:", local_time.strftime("%Y-%m-%d %H:%M:%S"))

# 2. Set local timezone (you can customize this)
# local_timezone = pytz.timezone("Asia/Kolkata")  # Replace with your local zone
# localized_time = local_timezone.localize(local_time)

# 3. Choose the target timezone
# target_timezone = pytz.timezone("US/Eastern")  # You can use any valid timezone name

# 4. Convert to target timezone
# converted_time = localized_time.astimezone(target_timezone)

# 5. Print result
# print("Converted time in US/Eastern:", converted_time.strftime("%Y-%m-%d %H:%M:%S"))


