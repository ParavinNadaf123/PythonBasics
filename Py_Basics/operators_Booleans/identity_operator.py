#is  and is not operator
x=[1,2]
y=x
z=[1,2]
print(x is y)
print(x is z)

print("memory location of x",id(x))
print("memory location of y",id(y))
print("memory location of z",id(z))

#is not operator
a = "hello"
b="hello"
c="hi"

print(a is not b)
print(a is not c)

print("memory location of a",id(a))
print("memory location of b",id(b))
print("memory location of c",id(c))