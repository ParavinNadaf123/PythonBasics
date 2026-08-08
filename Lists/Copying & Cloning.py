# ✅ 1. Definition
# Copying or cloning a list means creating a new list that
# contains the same elements as the original —
# so you can modify it without affecting the original.
#
# There are two main types of copy:
# Shallow copy: Duplicates the outer list only
# Deep copy: Duplicates everything — including nested lists
#
# | Method                | Type    | Notes                        |
# | --------------------- | ------- | ---------------------------- |
# | `list.copy()`         | Shallow | Pythonic and readable        |
# | `list[:]` (slicing)   | Shallow | Common and fast              |
# | `list()`              | Shallow | Constructor-based copy       |
# | `copy.deepcopy(list)` | Deep    | Needed for nested structures |

#
# 🧬 Syntax
# # Shallow copies
# copied_list = original.copy()
# copied_list = original[:]
# copied_list = list(original)

# # Deep copy
# import copy
# copied_list = copy.deepcopy(original)


# 💡 Use Cases
# | Situation                                             | Method                      |
# | ----------------------------------------------------- | --------------------------- |
# | You want to reuse the same data                       | Shallow copy                |
# | You want to modify one list without affecting another | Shallow or deep copy        |
# | You’re dealing with **nested lists**                  | Deep copy (`copy.deepcopy`) |
# ============================🔹 Example 1: list.copy() – Shallow Copy
fruits=["apple","banana","cherry"]
copied_fruits= fruits.copy()
copied_fruits.append("fig")
print(copied_fruits)
# Explanation:
# copied is a new list
# Changing copied does not affect old/exixting one
#========================------------🔹 Example 2: Slice Copy – [:]
color=["blue","red","orange"]
copied_color=color[:]

copied_color[0]= "black"
print(color)
print(copied_color)
# Explanation:
# [:] is a quick way to copy all elements in the list
# Still a shallow copy

#--------------🔹 Example 3: Using list()
#The list() constructor builds a new list from the original


fruits = ['apple', 'banana']
copied = list(fruits)
copied.append('mango')

print(fruits)  # ['apple', 'banana']
print(copied)  # ['apple', 'banana', 'mango']


#----------------------🔹 Example 4: Nested List + Shallow Copy
data = [[1, 2], [3, 4]]
shallow = data.copy()
shallow[0][0] = 99

print(data)     # [[99, 2], [3, 4]]
print(shallow)  # [[99, 2], [3, 4]]
# Explanation:
# Outer list is copied, but inner lists are shared
# So modifying nested items affects both
# ------------
# 🔹 Example 5: Deep Copy (solves nested problem)
# deepcopy() creates independent copies of inner lists too


import copy

data = [[1, 2], [3, 4]]
deep = copy.deepcopy(data)
deep[0][0] = 99

print(data)  # [[1, 2], [3, 4]]
print(deep)  # [[99, 2], [3, 4]]


