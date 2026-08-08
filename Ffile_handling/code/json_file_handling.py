# Read a JSON file and print specific fields.
# import json
# with open("employees.json","r") as f:
#     data = json.load(f)
# print(data[0]["Name"])
# print(data[1]["Name"])

import json

with open("../json files/employees.json", "r") as f:
    data = json.load(f)

for employee in data:
    print(employee["Name"])


# Convert the contents of a text file into a JSON file.
with open("../textFiles/filename4.txt", "r") as f:
  data = f.read()
  json_data = {"content": data}

with open("../json files/output.json", "w") as json_file:
    json.dump(json_data,json_file,indent=4)

print("test file is converted in to jason")
# Read an API response stored in a JSON file and validate specific field values.
with open("../textFiles/filename1.txt", "r") as f:
    data = f.read()

    expected = {
        "status": "active",
        "name": "John"
    }
# Save an API response into a JSON file.
import requests
import  json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("../json files/api_response.json", "w") as file:
        json.dump(data,file,indent=4)

    print("Api response saved successfully")
else:
    print("request failed: ",response.status_code)


# Compare two JSON files and identify differences.
with open("../json files/file1.json", "r") as f1:
    data1 = json.load(f1)

with open("../json files/file2.json", "r") as f2:
    data2 = json.load(f2)

all_keys = set(data1.keys()).union(data2.keys())

for key in all_keys:
    value1= data1.get(key)
    value2 = data2.get(key)

    if value1 != value2:
        print(f"{key}:")
        print(" file1 - >",value1)
        print(" file2 - >",value2)
        print()
# Read a configuration JSON file and print application settings (URL, browser, etc.).

import json

with open("../json files/config.json", "r") as file:
    config = json.load(file)

print("Application Settings")
print("--------------------")
print("URL      :", config["url"])
print("Browser  :", config["browser"])
print("Username :", config["username"])
print("Password :", config["password"])
print("Timeout  :", config["timeout"])


import json

def read_config():
    with open("../json files/config.json", "r") as file:
        return json.load(file)

config = read_config()

url = config["url"]
browser = config["browser"]
username = config["username"]
password = config["password"]

print(url)
print(browser)
print(username)
print(password)