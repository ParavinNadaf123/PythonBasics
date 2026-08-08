# Write a function to find the maximum of three numbers.
#

# n1 = int(input("Enter the number n1 :"))
# n2 = int(input("Enter the number n2 :"))
# n3 = int(input("Enter the number n3 :"))
#
# def nums(n1,n2,n3):
#     if n1 > n2:
#         print("n1 is greater ")
#     elif n2 > n3:
#         print("n2 is greater")
#     else:
#         print("n3 is greater that n1 and n2")
#
# nums(n1,n2,n3)
#

# Write a function that prints whether a given number is even or odd.
# #
# num = int(input("Enter the number "))
# def odd_even(num):
#     if num %2 ==0:
#         print("The num is even ")
#     else:
#         print("The num is odd")
#
# odd_even(num)
# Write a function to check if a string is a palindrome or not.

# str = input("Enter the string :")
# rev_str = ()
# def check_palind(str):
#     reversed_string = str[::-1]
#     if str == reversed_string:
#         print(str, "is a palindrome")
#     else:
#         print(str, "is not a Palindrome")
#
# check_palind(str)


#
# Write a function that counts the number of vowels in a given string.
# str = input("Enter the string :")
# def count_vowels(str):
#     vowels = {"a","e","i","o","u","A","E","I","O","U"}
#     count_v = 0
#     for i in str:
#         if i in vowels:
#             # print(f"The letter {i} is vowels")
#             count_v = count_v + 1
#         # else:
#             # print(f" the letter {i} not vowels")
#
#     print(f"The count of vowels is {count_v}")
#
#
# count_vowels(str)


#
# Write a function to calculate the factorial of a number using recursion.
# #
# def cal_fact(n):
#     fact= 1
#     for i in range(1,n+1):
#         fact *=  i
#         print(fact)
#
# cal_fact(5)

# def fact(n):
#     if (n==0 or n ==1):
#         return 1
#     return fact(n-1) * n
#
# print(fact(6))


# Write a function that returns the square and cube of a given number.

# def squ_cube(n):
#     squ = n * n
#     cube = n*n*n
#     print("the sqaure of a number is",squ)
#     print("the cube of a number is",cube)
#
# squ_cube(3)
# #
# Write a function to reverse a list without using built-in methods.
# def reverse_list(lst):
#     reversed_list = []
#     for i in range(len(lst) - 1, -1, -1):  # start from last index to 0
#         reversed_list.append(lst[i])
#     return reversed_list
#
# nums = [10, 20, 30, 40]
# print(reverse_list(nums))


#
# Write a function that takes a list of numbers and returns only even numbers.
#
# my_list = list(map(int, input("Enter numbers separated by commas: ").split(',')))
#
#
# # print(my_list)
# # print(type(my_list))
#
# def even_nums(my_list):
#     for i in my_list:
#         if i % 2 == 0:
#             print("The num is even :",i)
#
# even_nums(my_list)

# Write a function to find the largest element in a list.
#
# num_list = list(map(int,input("enter the list if numbers :").split(',')))
#
# def check_large_ele(num_list):
#     large_ele = num_list[0]
#     for i in num_list:
#         if large_ele <=  i:
#             large_ele = i
#     print(large_ele)
#
# check_large_ele(num_list)


# Write a function that checks if a number is prime or not.

# def is_prime(num):
#     if num <= 1:
#         return("not prime")
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return("not prime")
#     return ("Its prime")
#
#
# print(is_prime(7))   # Output: True
# print(is_prime(10))  # Output: False
# print(is_prime(22))


# Write a function using positional arguments to calculate the area of a rectangle.
#
# def area_of_rectangle(length,breadth):
#     area_of_rect = length * breadth
#     print(area_of_rect)
#
# area_of_rectangle(3,4)

# Write a function using keyword arguments to print student details (name, age, grade).
#

# def std_info(name="pari",age=33,grade="6A"):
#     print(f"The student {name} is from {grade} and she is {age} year old")
#
# std_info()


# Write a function with a default argument that greets a user with a default name “Guest”.
# def greet(name="Guest"):
#     print(f"Hello {name}!")
#
# greet()         # uses default
# greet("Pari")   # overrides default


# Write a function using *args to find the sum of any number of values.
#

def cal_sum(*num):
    return  sum(num)

print(cal_sum(1,3,5,99,100))

# Write a function using **kwargs to display key-value details of a person.

def person_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}--{value}")

person_details(name ='pari',age=22,gender="Female",city="hubli",subject=["Maths","Science","English"])