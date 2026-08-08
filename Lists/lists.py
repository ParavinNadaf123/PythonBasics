#A list in Python is an ordered, mutable collection, allows duplicate, that can hold any type of object
 #Method	Description
# append()	Add single element
# extend()	Add all elements from iterable
# insert()	Insert element at index
# remove()	Remove first occurrence of value
# pop()	Remove and return element
# clear()	Empty the list
# index()	Find index of value
# count()	Count occurrences
# sort()	Sort in place
# reverse()	Reverse in place
# copy() Return a shallow copy

lst = ["name",22,99.8,True,None,(2+3j)]
print(lst)
lst[0:1]=["looloo",5444]
print(lst)

fruits=["mango","cherry","apple"]
print(fruits)
fruits[0:1]=("banana","kiwi")
print(fruits)


my_set = {1, 2, 3}
my_set.add([4, 5])  # List is NOT hashable


