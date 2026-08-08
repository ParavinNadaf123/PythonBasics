# Definition: A set is an unordered collection of unique elements in Python.
#
# Sets do not allow duplicates and are mutable (elements can be added or removed).
#
# Sets are defined using curly braces {} or the set() constructor.

#add()- Adds ONE single element to the set
# Takes only one item


# update()
# Adds MULTIPLE elements to the set
# Accepts iterables (list, tuple, set, string)

numbers = {1, 2, 3, 4, 5}
print(numbers)


name = {"pari","reshu","razia"}
print(name)
print(type(name))

code = {"pari","nadaf",33,4.11,4+8j}
print(code)
print(type(code))
# code[2]= "hubli" error
# print(code)

list = [2,3,66,7]
list_set = set(list)
print(list_set)
print(type(list_set))
# my_set = {1,[7,9]}
# print(my_set) TypeError: unhashable type: 'list'

empty_set = set()
print(empty_set)  # Output: set()

fruits = {"apple","kiwi","orange"}
fruits.add("mango")
print(fruits)
fruits.remove("apple")
print(fruits)


my_set = {1, 2, 3}
my_set.add((4, 5))  # Tuple is hashable
# my_set.add([7,8])
# my_set.add({22,4})
print(my_set)


# Using int in a set
my_set = {1, 2, 3}
print(my_set)

# Using int as dictionary key
my_dict = {1: "One", 2: "Two"}
print(my_dict)
# function in sets
x = {1,2,3,4}
x.add(10)
print(x)
p = [20,30,40]
j = ("pari","zeeshu")
g = {33,44}
x.update(p)
x.update(j)
x.update(g)
print(x)

d = {77,88,99}
t = d.copy()
print(t)
t.remove(99)
print(t)


y = {100,102,103}
y.discard(100)
print(y)
y.discard(200)
print(y)
e = {"pari","lala","popo"}
e.clear()
print(e)

q= {1,2,3,4,5}
s ={10,20,30,1,2}
print(q.union(s))
print(q|s)

print(q.intersection(s))
print(q & s)


w = {4,5,6,7}
v= {8,9,6,5}
print(w-v)
print(v-w)


# 1️⃣ remove()
# Removes a specific element
# 👉 Use when you are sure the element exists.


# 🔹 2️⃣ discard()

# Removes a specific element (safe version)
# ✔ If element is not present → NO error
# 👉 Use when element may or may not exist.


# 🔹 3️⃣ pop()

# Removes and returns a RANDOM element
# ⚠ Set is unordered → removed element is not predictable
# ❌ If set is empty → error
# 👉 Use when you don’t care which element is removed.

# 🔹 4️⃣ clear()
# Removes ALL elements from the set
# ✔ Always safe
# ✔ No error
#
# 👉 Use when you want to reset the set



#
# # set
# s = {1,2,3}
# print(type(s))
# s1 = { }
# print(type(s1))
# s2 = set()
# print(type(s2))
#
# s3 = {1,2,3,"pari",11.5,2+5j}
# print(s3)
#
# for i in s3:
#     print(i)
#
# s4 = set([1,33,4,55,67,55])
# print(type(s4))
# print(s4)
#
# s4.add(100)
# print(s4)
# s4.add(99)
# print(s4)
#
# s5={11,22,33,99}
# print(s5)
# # s5.add(77,54) TypeError: set.add() takes exactly one argument (2 given)
# # print(s5)
#
# # Adds ONE single element to the set
# # Takes only one item
#
# s4.update((1000,99))
# print(s4)
#
# veg = {"potato","carrot","tomato"}
# veg.update({"chilli"})
# print(veg)
#
# veg.update(["chilli"])
# print(veg)
#
# # veg.update(("chilli"))
# # print(veg)
#
# veg.update((10,99))
# print(veg)
#
# new_veg = ["raddish","capsicum"]
# veg.update(new_veg)
# print(veg)
#
# s6 = {11,"pari","zeeshu","11.78"}
# s6.add((77,54))
# print(s6)
#
# # s6.add(["reshu","tara"]) #TypeError: unhashable type: 'list'
#
# # print(s6)
#
# fruit = {"apple","mango","banana","kiwi"}
# print(fruit)
# # fruit.remove("chiku")
# # print(fruit)
#
# # fruit.pop()
# # print(fruit)
#
# # fruit.discard("apple","banana") TypeError: set.discard() takes exactly one argument (2 given)
# fruit.discard(("kiwi"))
# print(fruit)
#
# fruit.discard(("orange"))
# print(fruit)
#
# obj = {"table","chair","phone"}
# obj.pop()
# print(obj)
#
# # obj1= set()
# # obj1.pop()
# # print(obj1) KeyError: 'pop from an empty set'
#
# # obj.clear()
# # print(obj)
#
# # obj1 = obj.copy()
# # print(obj1)

obj = {"table","phone","chair","blanket"}
obj1 = {"bottle","daiper","bag","phone","table"}

print(obj.union(obj1))
print(obj.intersection(obj1))
print(obj.difference(obj1))
print(obj.symmetric_difference(obj1))

a = {1,2,3,6}
b = {3,4,5,}


print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
# print(a.symmetric_difference(b))
# print(a.isdisjoint(b))
print(a.issuperset(b)) #false #Checks whether one set contains ALL elements of another set
# Returns True if every element of B is present in A-

c={22,33,44}
d = {55,66,77}

print(c.isdisjoint(d)) # Checks whether two sets have NO common elements Returns True if intersection is empty
# set[0]="popo"


# expected_fields = {"id", "name"}
# api_fields = {"id", "name", "email", "age"}
#
# assert api_fields.issuperset(expected_fields)
