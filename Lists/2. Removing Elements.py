# Method	Description   	Notes / Differences
# 1.remove(x)	Removes first occurrence of value x	           Raises error if not found
# 2.pop([i])	Removes and returns item at index i (last if not specified)	        Use pop() to get and delete together,, By default, removes the last item
# 3.clear()	Removes all items from list         	Use to empty a list
#___________________remove()
#remove by value , Removes 1st occurance
lst = ["name",22,99.8,True,None,(2+3j)]
lst.remove(None)
print(lst)
# lst.remove(889)

fruits = ["apple","banana","orange","apple","kiwi","orange","banana"]
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.remove("banana")
print(fruits)


# POP++++++++++++++++++++++++
#remove by index
#remove last occurance
color=["blue","pink","red","blue"]
print(color)
color.pop()
print(color)
color.pop(2)
print(color)



#++++++++++++++++++++++clear++++++++++

vegetables=["tomato","carrot","potato","radish"]
print(vegetables)
vegetables.clear()
print(vegetables)
