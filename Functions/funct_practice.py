# a = int(input("Enter the number n1 :"))
# b = int(input("Enter the number n2 :"))
# c = int(input("Enter the number n3 :"))
#
# def sum(a,b,c):
#     total = a+b+c
#     print(total)
#
# sum(a,b,c)
#
# def avg(a,b,c):
#     avg = (a+b+c/3)
#     print(avg)
#
# avg(a,b,c)

# a = 10
#
# def show():
#     a = 5
#     print(a)
#
# show()
#
# print(a)
#
# def square(num):
#     """Takes a number and returns its square."""
#     return num**2
#
# square(7)
#
# print(square.__doc__)
#
# def info(name,age):
#     print(f"{name} is {age}")
#
# info("lolo","55")
# info(name="bebo",age=45)
#
#
# def add(*num):
#     return sum(num)
#
# add(2,3,4,5)
#
# def show_detail(**info):
#     for key,value in info.items():
#         print(f"{key}:{value}")
#
# show_detail(name="pari",age=33,gender="Female",city="Hubli")
#
# str = input("Enter the srting:")
# rev_str = str[::-1]
# def check_palidrom():
#     if str == rev_str:
#         print("the string is palindrom")
#     else:
#         print("Not palindrom")
#
# check_palidrom()
#
#
# str = input("Enter the srting:")
#
# def check_vowels(str):
#     vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
#     count_vowels = 0
#     for l in str:
#         if l in vowels:
#             count_vowels = count_vowels + 1
#
#     print(f"The count of {count_vowels} ")
#
# check_vowels(str)
#
# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#         print(fact)
#
# cal_fact(5)
#
# def fact(n):
#     if (n==0 or n ==1):
#         return 1
#     return fact(n-1) * n
#
# print(fact(6))
#
# def square(n):
#     return n**2
#
# def cube(n):
#     return n**3
#
# print(square(8))
# print(cube(2))
#
# list = [1,2,3,4,5]
# def rev_list(list):
#     reversed_list = []
#     for n in range(len(list)-1,-1,-1):
#         reversed_list.append(list[n])
#     return  reversed_list
#
# print(rev_list(list))
#
# name = ["pari","reshu","razia","hasan"]
# def rev_list1(name):
#     reversed_name_lst = []
#     for w in range(len(name)-1,-1,-1):
#         reversed_name_lst.append(name[w])
#     return reversed_name_lst
#
# print(rev_list1(name))

# num_list = [10,20,30,40,50]
# def check_rev_num_list(num_list):
#     rev_num_list = []
#     for n in range(len(num_list)-1,-1,-1):
#         rev_num_list.append(num_list[n])
#     return rev_num_list
#
# print(check_rev_num_list(num_list))

# num_list =list(map(int, input("enter the number separated by comma:").split(',')))
# print(num_list)

# def even_num(num_list):
#     for n in num_list:
#         if n % 2 == 0:
#             print("The num is even:",n)
#
# (even_num(num_list))

# numbers = [10, 25, 8, 40, 15]
#
# def check_largest_num(numbers):
#     largest_number = numbers[0]
#     for n in numbers:
#         if largest_number <= n:
#             largest_number = n
#     print(largest_number)
#
# # check_largest_num(numbers)

def add(*args):
    total = 0
    for n in args:
        total += n
    print("sum of all numbers is :",total)

add(1,2,3,3,4,4,5,6,7,7,44,3,344,555,666)

def cal_mul(*num):
    mul = 1
    for n in num:
        mul *= n
    print("multiplication of all the numbers is :",mul)

cal_mul(1,2,4,3,55,66)

def show_name(*Names):
    for name in Names:
        print("Hello",name)
show_name("pari","javed","zeehsan","Reshu")

def check_max_num(*nums):
    print("numbers are ",nums)
    print("the largest number is ",max(nums))

check_max_num(1,2,55,66,89,45)

def join_word(*words):
    sentence = " ".join(words)
    print(sentence)

join_word("my","name","is","parvin")

def emp_details(**e_details):
    for key,value in e_details.items():
        print(f"{key} : {value}")

emp_details(name ="Pari",age = 33,gender = "Female",city = "Banglore")

def name_greet(**name_msg):
    name = name_msg.get("name")
    msg = name_msg.get("msg")
    print(f"hello {name},{msg}")

name_greet(name = "pari",msg="God bless you")

def order_details(**o_details):
    for key,value in o_details.items():
        print(f"{key} : {value}")

order_details(name="Table",quantity = 5,price = 1500,order_no = "tab1234")


def sum_avg(*numbers):
    total = 0
    for n in numbers:
        total += n
        avg_num = total/len(numbers)
    print("sum of numbers",total)
    print("avg of numbers",avg_num)

sum_avg(1,4,5,6,78,99,7,66,6)

def area_rect(length,width):
    area_of_rect = length * width
    print(area_of_rect)

area_rect(5,6)

def check_min_max(*nums):
    min_num = nums[0]
    max_num = nums[0]
    for n in nums:
        if min_num > n:
            min_num = n
        if max_num < n:
            max_num = n

    print("The minimun number is :",min_num)
    print("The maximum number is :", max_num)

check_min_max(9,7,3,4,99,999,1222)

def check_longest_word(*str):
    longest_word = str[0]
    for w in str:
        if len(w) >len(longest_word):
            longest_word = w
    print(longest_word)

check_longest_word("my","name","is","paravin")