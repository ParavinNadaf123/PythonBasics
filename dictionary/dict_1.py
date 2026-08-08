# dictionary in Python is a collection of key-value pairs.
#
# Keys → Unique and immutable (like str, int, tuple)
#
# Values → Can be any data type
#
# Unordered, Mutable, and Dynamic
# my_dict = {
#     "key1": "value1",
#     "key2": "value2"
# }
#
# print(my_dict)

student_details = {
    "name" : "Pari",
    "Age" : "33",
    "Gender" : "Female"
}

print(student_details["name"])
print(student_details.get("Gender"))
# print(student_details)
# student_details["name"]="Zeeshu"
# student_details["Age"] = "3"
# student_details["Gender"] = "Male"
student_details["city"] = "Banglore"
print(student_details)

student = {
    "name": "Ravi",
    "age": 21,
    "course": "Python"
}

print(student)
print(student.get(("course")))
#
score_result =  {
    "Team" : "India",
    "score" : 220,
    "match" : "Test Match"}
#
#
# print(score_result["score"])
# print(score_result["Team"])
# print(score_result.get("match"))
#
# # Adding & Updating
# score_result["score"]= 245
# score_result["overs"] = 12
# print(score_result)
score_result["Man_of_match"]= "Kholi"
print(score_result)

employee = {
    "emp_no" : "001",
    "Name" :"Riya",
    "Address" :"Nadaf",
    "dept_no" : "01",
    "dept_name" :"QA Analyst"
}
# print(employee)
#
employee.pop("dept_no")
print(employee)
#
del employee["Address"]
print(employee)
#
for key,value in employee.items():
    print(key, "---" , value)
#
for key,value in student.items():
    print(key,"===",value)

for key,value in student_details.items():
    print(key, "-----" , value)
#
items = {"product":"chair",
         "price":"1110",
         "discount" : "20%"}

print(items)
# items.clear()
# print(items)
print(items.keys())
print(items.values())
print(items.items())

d = dict({"lolo":20,
         "bebo":30,
         "popo":50})
print(d)
#
d1 = dict([("durga",20),
          ("shiva",30),
          ("ravi",50)])
print(d1)
print(len(d))

x = dict({"koko" : 39,
          "jojo" : 55})

d1.update(x)
print(d1)
#
#
#
# # ================================================================
#
# # dictionary
# user = {}
# print(type(user))
#
# d = dict()
# print(type(d))
#
# d1 = {"a":1,"b":2,"c":3}
# print(type(d1))
# print(d1)
#
# d2 = dict(veg = "tomato",fruit = "apple",qty = 2)
# print(d2)
# d4 = dict(name="Pari", age=32)
# print(d4)
#
# user1 = {"name":"rolo","role":"dev","exp" :3}
# print(user1)
#
# user2 = {"name":"tara","role":"BA","exp" :10,"role":"PM"}
# print(user2)
# print(user2["name"]) # access
# user2["exp"] = 5 #updating
# print(user2)
# user2["city"] = "Goa"
# print(user2) #adding
# print(user2["city"]) #access
# print(user2.get("name")) #access
#
# # a = {[1,2]:"num"} TypeError: unhashable type: 'list'
# # print(a)
#
# b = {(1,2):"num"} #works -tuple is immutable
# print(b)
#
# # c = {dict(fruit = "apple",qty = 2):"shopping"} # unhashable type: 'dict'
# # print(c)
#
# c = {2 :"order"}
# print(c)
#
# # f = {{10,20,40}:"rate"} #TypeError: unhashable type: 'set'
# # print(f)
#
order = {"pname" :"phone","qty":10,"inventory":200}
# order.pop("inventory") #remove by key
# print(order)
# order = {"pname" :"phone","qty":10,"inventory":200,"location":"hubli"}
# order.popitem() # remove last key value pair
# print(order)
# order = {"pname" :"phone","qty":10,"inventory":200,"location":"hubli","invoice":1223}
# del order["invoice"]
# print(order)
# print(order.keys())
# print(order.values())
# print(order.items())
#
# for k ,v in order.items():
#     print(k,v)
#
# for k,v in user2.items():
#     print(k)
#
# for k,v in user1.items():
#     print(v)
#
# user1.update({"gender":"female"})
# print(user1)
#
# order.update({"month":"Dec","year":2025})
# print(order)
#
# user["DOB"] = "03-10-1980"
# print(user)
#
# user.update({"name":"paro","role":"CEO","exp":20})
# print(user)
#
#
# # dictionary
# user = {}
# print(type(user))
#
# d = dict()
# print(type(d))
#
# d1 = {"a":1,"b":2,"c":3}
# print(type(d1))
# print(d1)
#
# d2 = dict(veg = "tomato",fruit = "apple",qty = 2)
# print(d2)
# d4 = dict(name="Pari", age=32)
# print(d4)
#
# user1 = {"name":"rolo","role":"dev","exp" :3}
# print(user1)
#
# user2 = {"name":"tara","role":"BA","exp" :10,"role":"PM"}
# print(user2)
# print(user2["name"]) # access
# user2["exp"] = 5 #updating
# print(user2)
# user2["city"] = "Goa"
# print(user2) #adding
# print(user2["city"]) #access
# print(user2.get("name")) #access
#
# # a = {[1,2]:"num"} TypeError: unhashable type: 'list'
# # print(a)
#
# b = {(1,2):"num"} #works -tuple is immutable
# print(b)
#
# # c = {dict(fruit = "apple",qty = 2):"shopping"} # unhashable type: 'dict'
# # print(c)
#
# c = {2 :"order"}
# print(c)
#
# # f = {{10,20,40}:"rate"} #TypeError: unhashable type: 'set'
# # print(f)
#
# order = {"pname" :"phone","qty":10,"inventory":200}
# order.pop("inventory") #remove by key
# print(order)
# order = {"pname" :"phone","qty":10,"inventory":200,"location":"hubli"}
# order.popitem() # remove last key value pair
# print(order)
# order = {"pname" :"phone","qty":10,"inventory":200,"location":"hubli","invoice":1223}
# del order["invoice"]
# print(order)
# print(order.keys())
# print(order.values())
# print(order.items())
#
# for k ,v in order.items():
#     print(k,v)
#
# for k,v in user2.items():
#     print(k)
#
# for k,v in user1.items():
#     print(v)
#
# user1.update({"gender":"female"})
# print(user1)
#
# order.update({"month":"Dec","year":2025})
# print(order)
#
# user["DOB"] = "03-10-1980"
# print(user)
#
# user.update({"name":"paro","role":"CEO","exp":20})
# print(user)
#
#
# emp = {"name":"pira","age":33,"role":"qa"}
# print(emp)
#
# emp_details = { "emp1": {"name":"pira","age":33,"role":"qa"},
# "emp2": {"name":"lolo","age":38,"role":"dev"},
# "emp3": {"name":"polo","age":29,"role":"ba"},
# "emp4": {"name":"tata","age":45,"role":"PM"}
#
# }
# print(emp_details)
#
# std_details = {"std1" : {"name":"para","class":4,"price":1000},
#                "std2" : {"name":"lili","class":7,"price":500},
#                "std3": {"name" : "coco","class":9,"price":1500}}
# print(std_details)