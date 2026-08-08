# A tuple is an ordered, immutable (unchangeable) collection of items.
# It can contain elements of different data types (int, string, float, etc.)
# Defined using parentheses () or simply comma-separated values.
# len()
# count()
# index()
#sorted()/ reverse = True
#
t = ("a","b",33,4.66,5j+2)
# print(type(t))
# print(t)
# print(t[-1])
#
t1= 5,
print(t1)
# print(type(t1))
#
t2 = "a",66,4.55
print(t2)
#
# print(t[2])
# print(t1[0])
# print(t2[2])
# #
t5 = ()
# print(type(t5))
#
#
list = [1,2,"a","b"]
print(type(list))
t = tuple(list)
print(type(t))
print(t)
#
t1 = tuple(range(1,50,3))
print(t1)
print(t1[15])
print(t1[-5])

# print(t1[0])
# print(t1[5:10])
# print(t1[3:10])
# print(t1[::2])
# t[6]= 66 #error
#
a= (10,20,30)
b= (1,2,3)
c= a+b
print(c)
print(type(c))

d = a*3
print(d)
print(len(d))
print(d.count(10))
#
print(d.index(30))

g= (22,33,5,66,78,9,2)
# G = sorted(g)
# print(g)
# print(G)
# print(max(g))
# print(min(g))
#
# g1= sorted(g,reverse=True)
# print(g1)
#
# words = ('strawberry', 'fig', 'grape', 'melons','nut')
# w = sorted(words,key=len,reverse=True)
# print(w)
#
a = 10
b= 20
c= 30
d = 40
t_a = a,b,c,d
print(t_a)

t = ("maths","Science","English")
a,b,c = t
print(a)

t_details = ("pari",32,"banglore")
print(t_details[2])


data = ("QA", "ETL", "Python")
designation,operation,language = data
print(language)

def salary_data():
    return (25000, 45000, 80000)

min_sal, avg_sal, max_sal = salary_data()
print(avg_sal)  # Output: 200

user = ("Pari", "QA Engineer", "India")
print(f"{user[0]} Works as a{user[1]} in {user[2]}.")


t = (1, 2, [3, 4])
t[2].append(5)
print(t)

oopa = (33,5,7,[44,6],89)
oopa[3].append(100)
print(oopa)

my_tuple = (lambda x: x+2, lambda y: y*2)
print(my_tuple )
name = ("pari","zeeshu","reshu",["zozo","lolo"])
name[3].append("koko")
print(name)

a = 5
b = 10
a, b = b, a
print(a, b)

fruits = ["apple", "banana", "mango"]
for i, fruit in enumerate(fruits):
    print(i, fruit)


names = ["Pari", "Aarav", "Riya"]
roles = ["QA", "Dev", "Manager"]

for pair in zip(names, roles):
    print(pair)

veg = ["onion","tomato","peas","carrot"]
for i , veg in enumerate(veg):
    print(i,veg)

name = ["pari","pari","reshu","zeeshu"]
subject = ["Maths","science","english","hindi"]
score = [99,79,66,59]

for pair in zip(name,subject,score):
    print(pair)