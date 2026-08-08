# # A function is a block of reusable code that performs a specific task.
# # It helps make code modular, organized, and less repetitive.
# def function_name(parameters):
#     # code block
#     return s
#
#
# # 2. Types of Functions
# # a) Built-in Functions
# #
# # Already available in Python.
# # ✅ Examples: len(), print(), type(), sum(), max()
#
# print(len("Hello"))      # 5
# print(sum([1, 2, 3]))    # 6
# #
# # b) User-Defined Functions
# #
# # Created by the programmer using def.
#
def greet():
    print("Hello, welcome to Python!")
#
# greet()  # Function call
#
# def wish():
#     print("Helllo")
#
# wish()
#
# def add(a,b):
#     print("sum",a+b)
#
# add(1,2)
#
# def happy_birthday(name):
#     print("Happy birthday",name)
#     # return happy_birthday(name)
#
# happy_birthday("pari")
# happy_birthday("zeeshu")
#
n1 = int(input("Enter the number n1 :"))
n2 = int(input("Enter the number n2 :"))
n3 = int(input("Enter the number n3 :"))

def averg_of_number (n1,n2,n3):
    average = ((n1+n2+n3)/3)
    print(average)
#     return average
#
# averg_of_number(98,97,95)
#
# def multiply(a1,a2,a3):
#     mul = (a1*a2*a3)
#     print(mul)
#     return mul
#
# multiply(1,2,3)
# multiply(22,44,89)
#
# def student_info(name,age=18,*subjects,**details):
#     print("name :",name)
#     print("age:",age)
#     print("Subject",subjects)
#     print("Details",details)
#
# student_info("Pari", 20, "Math", "Science", city="Pune", grade="A")
#
# def place(name,gender,*country_name,**state_name,):
#     print("name: ",name)
#     print("gender: ",gender)
#     print("country:",country_name)
#     print("state:",state_name)
#
# place("zeeshu","Female","india","china","singapore","Dubai",city = "banglore",pincode = 560089)
#
#
# num_list = [1,2,3,4]
# veg_list = ["potatoes","onion","carrot","chilli","tomatoes"]
#
#
# def print_len_list(list):
#     print(len(list))
#
# print_len_list(num_list)
# print_len_list(veg_list)
#
# def print_list(list):
#     for l in list:
#         print(l,end=" ")
#
# print_list(veg_list)

# n=5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     print(fact)

# fact = 1
def cal_fact(n):
    fact = 1
    for i in range (1,n+1):
        fact *= i
        print(fact)

cal_fact(6)



# usd = n
# inr = n * 88.611

def usd_inr(n):
    inr = n * 88.611
    print(f"The conversion of {n} dollar is {inr} Rupees")
    return inr

usd_inr(5)
usd_inr(1000)

num = int(input("Enter the number "))
def odd_even(num):
    if num %2 ==0:
        print("The num is even ")
    else:
        print("The num is odd")

odd_even(num)