from functools import reduce

add= lambda a,b :(a + b)
print(add(1,2))

square = lambda  b:(b*b)
print(square(6))

cube = lambda c:(c*c*c)
print(cube(7))

even_check = lambda y : y%2==0
print(even_check(8))

check_len = lambda x : len(x)
print(check_len("Paravinsultan"))

numbers = [12,34,56,78,95]

sq = list(map(lambda x : x *x ,numbers))
print(sq)

n = [2,3,46,7,8,9,66]
cb = list(map(lambda z :z*z*z,n))
print(cb)

check_even =list(map(lambda t : t %2 == 0,numbers))
print(check_even)

check_odd = list(map(lambda l : l%2 !=0,numbers))
print(check_odd)

product = reduce(lambda x,y : x*y,numbers)
print("Product of all is :", product)

summation = reduce(lambda e,f:e+f,numbers)
print("summation of all is ",summation)




