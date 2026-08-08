# from If_Elif_Else.If_else_if import emp_details
# from dictionary.dict_1 import employee


def add(a,b,c):
    print(a+b+c)

add(2,4,5)

def add1(*args):
    print(args)
    total = 0
    for n in args:
        total += n
    print("Sum of all numbers is :",total)

add1(1,3,4,5,6,5,5,5,5,5,5,5,5,7,7,7,7)

def cal_mul(*args):
    print(args)
    mul = 1
    for n in args:
        mul *= n
    print("Multiplication of all the numbers :",mul)

cal_mul(1,2)


# ✅ Example 1: Print all names

def show_name(*names):
    print(names)
    for name in names:
        print("Hello",name)

show_name("pari","zeeshu","lolo")


# ✅ Example 2: Find the largest number

def find_max(*nums):

    print("Numbers are:", nums)
    print("Maximum is:", max(nums))

find_max(4, 9, 2, 11, 6,33,77,100)

def join_words(*words):
    print(words)
    sentence =" ".join(words)
    print(sentence)

join_words("i","love","python")


# 🟢 2️⃣ **kwargs — accepts many keyword=value arguments
def emp_details(**e_deatils):
    for key,value in e_deatils.items():
        print(f"{key}: {value}")

emp_details(name = "pari",department="QA",project="evolve",team="Bengo")

def name_greet(**name_msg):
    # for key,value in name_msg.items():
    name = name_msg.get("name")
    msg = name_msg.get("msg")
    print(f"Hello {name},{msg}")

name_greet(name="Pari",msg="Good to see you")
name_greet(name="Reshu",msg="Have a good day")

# ✅ Example 3: Print order details

def order_details(**oder_details_status):
    print("order summary")
    for key,value in oder_details_status.items():
        print(f"{key} :{value}")

order_details(product_name="laptop",price=86000,quantity = 1,status = "delivered")

# Write a function that returns both the sum and average of numbers.


def cal_sum_avg(*num):
    sum=0
    for n in num:
        sum += n
        avg = sum/len(num)

    print("The total of all nums is :",sum)
    print(f"The average is of all nums :" ,avg)

cal_sum_avg(1,2,3,4)



def find_max(*args):
    if not args:        # if no arguments passed
        return None
    max_value = args[0] # assume first value is max
    for num in args:
        if num > max_value:
            max_value = num
    return max_value

# Write a function that accepts any number of arguments and returns the maximum value.

# Example
print(find_max(10, 25, 3, 48, 7))  # Output: 48
print(find_max(5, 2))              # Output: 5
print(find_max())                  # Output: None

#
# Write a function to multiply all numbers in a list and return the result.
#
def cal_list_mul(list_num):
    mul = 1
    for n in list_num:
        mul*= n
    print("the multiplication of all numbers is :",mul)

cal_list_mul([1,2,3,4])

# Write a function that returns multiple values (e.g., min and max from a list).
#

# def check_min_max(*nums):
#     max_num = nums[0]
#     for n in nums:
#         if max_num < n:
#             max_num = n
#     print("The maximun number is :",max_num)
#
# check_min_max(1,2,3,4,99,999,1222)

#
# def check_min_max(*nums):
#     min_num = nums[0]
#     for n in nums:
#         if min_num > n:
#             min_num = n
#     print("The minimun number is :",min_num)

# check_min_max(9,7,3,4,99,999,1222)

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

# Write a function that accepts a list of strings and returns the longest string.

def check_longest_str(*str_word):
    longest_word = str_word[0]
    for w in str_word:
        if len(w) > len(longest_word):
            longest_word = w
    print(longest_word)



check_longest_str("i","love","python","progr")




