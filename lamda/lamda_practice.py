# 6️⃣ Add 5 to each element using map()
from functools import reduce

num = [1,2,4,6,7,889,55,77,33]
add_num = list(map(lambda a : a +5,num))
print(add_num)

# 7️⃣ Filter words ending with “a”

word = ["pari","tara","lara","javed","gilli"]
a_word = list(filter(lambda w : w.endswith('a'),word))
print(a_word)

# 8️⃣ Multiply all numbers using reduce()
num = [1,2,4,6,7]
mul_num = reduce(lambda a,b : a*b,num)
print(mul_num)

# 9️⃣ Combine map + filter

result = list(map(lambda a : a * 2 , filter(lambda a : a%2 == 0,num )))
print(result)

# biggest of given number
num = [1,2,4,6,7]
# biggest_num = list(map(lambda x, y : x if x > y else y ,num))
biggest_num = reduce(lambda x, y : x if x > y else y ,num)
print(biggest_num)