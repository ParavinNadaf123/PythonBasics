# help you arrange or reverse the order of elements in a list
# In-place sorting (modifies original list)
# Non-destructive sorting (returns a new sorted list)
# These methods are key when dealing with reports, tables, or data analysiS
# Method	Purpose
# sort()	Sort list in-place
# sorted()	Returns a new sorted list
# reverse()	Reverses the order in-place
#SYNTAX-----------------------------------
# list.sort(key=None, reverse=False)
# sorted(list, key=None, reverse=False)
# list.reverse()

#USECASE-------------
# Scenario	Method
# Sort numbers or strings	== sort() or sorted()
# Keep original list unchanged	=== sorted()
# Sort by length or custom logic===	Use key
# Flip order of items	== reverse()

# 🔹 Example 1: sort() – In-place ascending sort
nums=[9,5,3,8,1,0]
nums.sort() #sort() directly changes nums — no new list is created.
print(nums)


# 🔹 Example 2: sorted() – Returns a new sorted list
# Original list stays unchanged
marks=[88,22,44,77,56,98,11]
marks_sorted=sorted(marks)
print(marks)
print(marks_sorted)

# 🔹 Example 3: reverse() – Reverse the current order
# Reverses the list as-is, not sorted — just flips order.
colors = ['red', 'blue', 'green',"yellow"]
colors.reverse()
print(colors)

a= [11,33,55,9,77]
a.reverse()
print(a)
# 🔹 Example 4: sort() in descending order
# reverse=True sorts from highest to lowest.
nums = [5, 2, 9, 1]
nums.sort(reverse=True)
print(nums)

#_____________________
# key=len means: “Sort the items by their length”
words = ['strawberry', 'fig', 'grape', 'melons','nut']
words.sort(key=len)
print(words)


