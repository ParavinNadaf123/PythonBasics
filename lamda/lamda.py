# lamda arguments: Expresion
# A lambda function is a small, anonymous function (without a name).
# It can have any number of arguments but only one expression.

add = lambda a,b : (a+b)
print(add(1,2))

cude = lambda a: a*a*a
print(cude(2))

square = lambda b :b*b
print(square(7))

even_check = lambda y : y%2 == 0
print(even_check(8))

len_check = lambda s : len(s)
print(len_check("pari"))
# 🔹 Why Use Lambda Functions?
# To write short, single-line functions.
# Commonly used with map(), filter(), reduce().
# Useful in data transformation, sorting, list comprehensions, and automation scripts.
from functools import reduce

nums = [1,2,3,4,11,66,98]
sq = list(map(lambda x : x * x,nums))
print(sq)
product = reduce(lambda x,y : x *y,nums)
print("Product of all is ",product)
sumation = reduce(lambda x,y : x + y , nums)
print("Product of all is ",sumation)
cb = list(map(lambda a : a*a*a ,nums))
print(cb)

chk_even = list(map(lambda b : b%2 == 0,nums))
print(chk_even)

name = ["pari","razia","reshma","hassain","hussian","tara"]
filter_word = list(filter(lambda w : len(w) < 6,name))
print(filter_word)

n_list = [1,2,55,6,78,9]
n = list(filter(lambda e_n : e_n % 2 == 0,n_list))
print(n)


# 1️⃣ Double each number in a list

nums_1 = [1,2,3,5,77,889,5]
d_num = list(map(lambda x : x*2,nums_1))
print(d_num)

name = ["pari","razia","reshma","incia","Arun","tara"]
name_words = list(filter(lambda w : w[0].lower() in 'aeiou',name))
print(name_words)

name_upper = list(map(lambda s :s.upper(),name))
print(name_upper)

longest_word = reduce(lambda a,b : a if len(a) > len(b) else b ,name)
print(longest_word)

odd_count = reduce(lambda a, b: a + (b % 2 != 0), nums, 0)
print(odd_count)