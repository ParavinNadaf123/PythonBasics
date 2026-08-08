# Write a lambda function to add two numbers.
from dictionary.dict_1 import employee

add = lambda a,b :(a+b)
print(add(2,4))

# Write a lambda function to multiply three numbers.
mul = lambda x,y,z :(x*y*z)
print(mul(1,2,3))
# Write a lambda function to return the square of a number.
numbers = [12,34,56,78,95]

sq = list(map(lambda x : x *x ,numbers))
print(sq)

sq = lambda x :(x*x*x)
print(sq(3))
# Write a lambda function to return the cube of a number.

cb= lambda v :(v*v*v)
print(cb(2))

# Write a lambda function to check whether a number is even.

even_num = lambda q : q%2 == 0
print(even_num(8))

# Write a lambda function to check whether a string is a palindrome.
is_palimdrome = lambda s: s == s[::-1]
print(is_palimdrome("madam"))

# Write a lambda function to return the length of a string.
check_len = lambda s : len(s)
print(check_len("apri"))
# Write a lambda function to find the maximum of two numbers.
check_max_num = lambda a,b :max(a,b)
print(check_max_num(20,19))
# Write a lambda function to convert a string to uppercase.
con_upper_case = lambda s : s.upper()
print(con_upper_case("pari"))
# Write a lambda function to calculate the area of a rectangle.
area_rectangle = lambda l,w : l*w
print(area_rectangle(3,4))

#map
# Square every number in a list.
nums_1 = [1,2,3,5,77,889,5]
d_num = list(map(lambda x : x**2,nums_1))
print(d_num)


# Convert all strings to uppercase.
s = ["pari","kala","java","mala"]
u_str = list(map(lambda s: s.upper(),s))
print(u_str)
# Convert integers into strings.
int_items = [1,2,3,4,5]
int_str = list(map(lambda x : str(x),int_items))
print(int_str)
# Convert Celsius temperatures to Fahrenheit.
temp_cel = [99, 80, 87, 77]

temp_F = list(map(lambda c: (c * 9/5) + 32, temp_cel))

print(temp_F)

# Find the length of every word.
words = ["Pari","javed","zeeshan","paravinsultan"]
check_len = list(map(lambda w : len(w),words))
print(check_len)

# Remove leading and trailing spaces from every string.
words = ["Pari "," javed","zeeshan","paravinsultan"]
remove_space = list(map(lambda w : w.strip(),words))
print(remove_space)

# Round floating-point numbers to two decimal places.
numbers = [3.14159, 2.71828, 9.87654]
dec_num = list(map(lambda n :round(n,2),numbers))
print(dec_num)
# Extract only usernames from a list of email addresses.
email = ["pari@gmail.com","sesha@yahoo.com","lolo@gmail.com","bebo@yahoo.com"]
username = list(map(lambda e :e.split('@')[0],email))
print(username)
# Calculate GST for every product price.
product_price= [100,20000,4000,70,900]
gst_product = list(map(lambda p :(p * 0.05),product_price))
print(gst_product)

product_price= [100,20000,4000,70,900]
gst_product = list(map(lambda p :p+(p * 0.05),product_price))
print(gst_product)
# Convert a list of tuples into a list of dictionaries.
data = [
    ("Pari", 25),
    ("Javed", 30),
    ("Zeeshan", 4)
] #it's a list ([]) containing tuples (()).
# print(type(data))
result = list(map(lambda t: {"name": t[0], "age": t[1]}, data))
#
print(result)

employee = [(101,"pari",20000),
            (102,"javed",90000),
            (103,"zeeshan",1000000)]

resule_emp = list(map(lambda emp:{
    "id" : emp[0],
    "name":emp[1],
    "salary":emp[2]
},employee))

print(resule_emp)

# Add 10 to every element → same arithmetic transformation.#

numbers = [1,2,3,4,5]
result_num = list(map(lambda n : (10+n),numbers))
print(result_num)

str = ["LOLO","KOKO","BEBO","JOJO"]
RESULT_STR = list(map(lambda w : w.lower(),str))
print(RESULT_STR)


boolean = [True, True, False, False, True]

re_boolean = list(map(lambda b: int(b), boolean))

print(re_boolean)


###################FILTER####################
# Syntax:
#
# filter(function, iterable)
#
# Example:
#
# nums = [1, 2, 3, 4, 5, 6]
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)
# # Output: [2, 4, 6]
#
# ✅ Use Case: When you want to select only certain elements that meet a condition.


# Find all even numbers.

number = [1,2,65,4,56,226,76,166,7,89,104]
even_n = list(filter(lambda n : n % 2 ==0,number))
print(even_n)


# Find numbers greater than 100.
greater_than100 = list(filter(lambda n : n >100,number))
print(greater_than100)
# Find positive numbers.
num1 = [11,22,-33,-4,929,993,0]
positive_num = list(filter(lambda n :n>0,num1))
print(positive_num)
# Find words longer than five characters.
char = ["pari","naveen","paravin","kolo"]
five_char = list(filter(lambda c :len(c)>5,char))
print(five_char)
# Find strings starting with a vowel.
word =["Apple","pari","ice-cream","zeeshan"]
v_char = list(filter(lambda v : v.startswith(("a","e","i","o","u","A","E","I","O","U")),word))
print(v_char)
#
# Find strings ending with ".csv".
word =["Apple.csv","pari","ice-cream","zeeshan.csv"]
v_char = list(filter(lambda v : v.endswith((".csv")),word))
print(v_char)
# Find prime numbers from a list.
numb = [1,13,5,6,66,78,45]
prime_num = list(filter(lambda n : n >1 and  all(n % i != 0 for i in range(2, int(n**0.5) + 1)),numb))
print(prime_num)
# Remove empty strings from a list.
word = [" ","pari","reshu"]
empty_str = list(filter(lambda w : w.strip(),word))
print(empty_str)
# Find students scoring above 75 marks.
student = [ ("pari",89),
           ("lata",79),
           ("lolo",67),
           ("rara",87)
]

sc_sutdent = list(filter(lambda s :s[1]>75,student))

print(sc_sutdent)

# Find employees whose salary is greater than 50,000.

emp = [ ("pari",30000),
        ("javed",70000),
        ("lata",20000),
        ("lopo",60000)]

emp_sal = list(filter(lambda  es : (es[1]>50000),emp))
print(emp_sal)

# Find products that are in stock.
prod_details = [("table","Instock"),
                ("chair","Instock"),
                ("Bat","OutOfStock"),
                ("ball","OutOfStock"),
                ("Bag","OutOfStock")]

stock_product = list(filter(lambda p :   p[1] == "Instock" ,prod_details))
print(stock_product)

# Find failed test cases.
testcase_details = [("TC001","Pass"),
                ("TC002","Fail"),
                ("TC003","Fail"),
                ("TC004","Pass"),
                ("TC005","Pass")]
tc_details = list(filter(lambda t :t[1] == "Fail",testcase_details))
print(tc_details)

########################### reduce() ############
# Find the sum of all numbers.
from functools import reduce
nums = [2, 3, 4,99,8]
sum = reduce(lambda x, y: x + y, nums)
print(sum)
# Find the product of all numbers.
prod = reduce(lambda x,y : x*y,nums)
print(prod)
# Find the largest number.
largest_num = reduce(lambda x,y : max(x,y),nums)
print(largest_num)
# Find the smallest number.
small_num = reduce(lambda x,y: min(x,y),nums)
print(small_num)
# Count even numbers.
count_even = reduce(lambda count,
                           num : count  + 1 if num % 2 == 0 else count ,
                           nums,
                            0)
print(count_even)

# count of odd numv=ber.

count_odd = reduce(lambda count,
                          num : count +1 if num % 2 != 0 else count,nums,0)
print(count_odd)

# Find the longest string.
str = ["Pari","paravinsultan","javednadaf","reshmaNadaf"]
long_str = reduce(lambda x,y: x if len(x) > len(y) else y,   words
)
print(long_str)
# Concatenate all strings.
str = ["I","love","Python","programming"]
conc_str = reduce(lambda x,y : x +" "+ y,str)
print(conc_str)
# Find the total salary of employees.
emp = [ ("pari",30000),
        ("javed",70000),
        ("lata",20000),
        ("lopo",60000)]

total_sal = reduce(lambda total,y : total+y[1],emp,0)
print(total_sal)
# reduce(
#     lambda accumulator, item: accumulator + value_from_item,
#     iterable,
#     0
# )
# Count the number of passed students.

student = [ ("pari",89,"passed"),
           ("lata",79,"passed"),
           ("lolo",28,"Fail"),
           ("rara",87,"passed"),
            ("koko",33,"Fail")
]

passed_std = reduce(lambda count_pass , z :
                    count_pass +1 if z[2] =="passed" else count_pass,student,0)
print(passed_std)

# Find the total bill amount.

product_price= [100,20000,4000,70,900]

total_bill = reduce(lambda total , x : total + x,product_price,0 )
print(total_bill)

# Find the average using reduce().
product_price= [100,20000,4000,70,900]
avg_price = reduce(lambda x, y : x+y/len(product_price),product_price)
print(avg_price)

# Merge multiple dictionaries into one.
from functools import reduce

dicts = [
    {"lolo": 20, "bebo": 30, "popo": 50},
    {"durga": 20, "shiva": 30, "ravi": 50},
    {"pari": 40, "javed": 60}
]

full_dict = reduce(lambda d1, d2: d1 | d2, dicts)

print(full_dict)


# ⭐ Combination Questions (Highly Asked)
#
# These are the ones most commonly asked in Python interviews.
#
# Use filter() and map() together to square only even numbers.
number = [12,13,45,67,89,4]
even_num = list(map(lambda x: x**2,filter(lambda x : x%2 == 0,number)))
print(even_num)

# Use map() and reduce() to calculate the total price after tax.
from functools import reduce

price = [1200, 9899, 987, 675, 546]

# Step 1: Add 5% tax to each price
price_after_tax = list(map(lambda x: x + (x * 0.05), price))

# Step 2: Calculate total
total_price = reduce(lambda total, p: total + p, price_after_tax, 0)

print(price_after_tax)
print(total_price)
# Use filter() and reduce() to calculate the sum of positive numbers.
post_num = [12,34,577,9,998,-99,-69]
post_n = list(filter(lambda x : x>0,post_num))
sum_post_n = reduce(lambda total,n:total + n,post_n)
print(sum_post_n)

# Find the average of all even numbers.

num_n= [1,54,6,7,8,44,80]
even_num = list(filter(lambda x:x%2 ==0,num_n))
print(even_num)
add_even_num = reduce(lambda total,n: total + n,even_num,0)
print(add_even_num)
avg_even_num = add_even_num/len(even_num)
print(avg_even_num)

# Convert all names to uppercase and filter names longer than five characters.

names = ["pari","zeeshan","javednadaf","hasan","husan","paravinnadaf"]
upper_name = list(map(lambda n : n.upper(),names))
print(upper_name)
five_char_name = list(filter(lambda n : len(n)>5,upper_name))
print(five_char_name)

upper_name = list(map(lambda n : n.upper(),filter(lambda n : len(n)>5,names)))
print(upper_name)
#
# Filter failed students and calculate their average marks.
students = [
    ("Pari", 85, "Pass"),
    ("Javed", 42, "Fail"),
    ("Lata", 76, "Pass"),
    ("Ravi", 38, "Fail"),
    ("Zeeshan", 91, "Pass"),
    ("Kiran", 29, "Fail"),
    ("Anjali", 68, "Pass"),
    ("Rahul", 35, "Fail")
]

failed_std = list(filter(lambda x :x[2]=="Fail",students))
print(failed_std)
failed_std_marks = reduce(lambda  total,students : total + students[1],failed_std,0)
print(failed_std_marks)

avg_failed_std_marks = failed_std_marks /len(failed_std)
print(avg_failed_std_marks)

# Find the total salary of employees whose experience is greater than five years.
employees = [
    ("Pari", 65000, 6),
    ("Javed", 48000, 4),
    ("Lata", 72000, 8),
    ("Ravi", 55000, 5),
    ("Zeeshan", 90000, 10),
    ("Kiran", 45000, 3),
    ("Anjali", 78000, 7),
    ("Rahul", 52000, 2)
]

emp_5y = list(filter(lambda e :e[2]>5,employees))
print(emp_5y)
total_sal_5y = reduce(lambda total,e : total + e[1],emp_5y,0 )
print(total_sal_5y)
# Filter prime numbers and calculate their sum.
num = [1,2,4,5,13,778,77,17,98]
prime_num = list(filter(lambda n : n >1 and  all(n % i != 0 for i in range(2, int(n**0.5) + 1)),num))
print(prime_num)
sum_prime_num = reduce(lambda total,pn : total+pn,prime_num,0)
print(sum_prime_num)
# Remove invalid email addresses and convert the remaining emails to lowercase.

emails = [
    "Pari@gmail.com",
    "JAVED@yahoo.com",
    "invalid_email",
    "Lata@Outlook.COM",
    "zeeshan@gmail",
    "RAVI123@GMAIL.COM",
    "hello.com",
    "Anjali@company.org",
    "rahul@",
    "KIRAN@YAHOO.COM"
]

valid_email = list(map(lambda e: e.lower(),
                       filter(lambda e: "@" in e and "." in e.split("@")[-1],email)))

print(valid_email)
# Filter odd numbers and multiply them together.
num = [27,4,3,5,77,9,56,75,34,59]
odd_num = list(filter (lambda x : x %2 !=0,num))
print(odd_num)

mul_odd_num = reduce(lambda mul,x : x* mul,odd_num,1)
print(mul_odd_num)
