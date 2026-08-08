# 🔹 What Are Dunder Methods?
# Dunder methods (like __len__(), __contains__()) are:
#
# Also called magic methods
#
# Part of Python’s data model
#
# Allow custom objects to work with built-in Python features (len, for, in, etc.)
#
# | Method           | Description                     | Commonly Triggered By  |
# | ---------------- | ------------------------------- | ---------------------- |
# | `__len__()`      | Returns number of items in list | `len(my_list)`         |
# | `__contains__()` | Checks if item exists in list   | `'x' in my_list`       |
# | `__iter__()`     | Returns iterator for the list   | `for item in my_list:` |
# 🧪 Code Examples (Simple + Behind-the-Scenes)
# ✅ __len__() – Behind len()

my_list = [10, 20, 30]

print(len(my_list))          # 3
print(my_list.__len__())     # 3 ← same thing, works but not recommended
# 📌 Explanation:
#
# When you call len(my_list), Python internally calls my_list.__len__()
#
# ✅ __contains__() – Behind in

my_list = ['apple', 'banana']

print('apple' in my_list)           # True
print(my_list.__contains__('apple'))  # True ← same as above
# 📌 Explanation:
#
# 'apple' in my_list triggers my_list.__contains__('apple')
#
# ✅ __iter__() – Behind for If_Elif_Else

my_list = [1, 2, 3]

# Standard way
for item in my_list:
    print(item)

# Behind the scenes
iterator = my_list.__iter__()
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# 📌 Explanation:
#
# for item in my_list: uses my_list.__iter__() to get an iterator
#
# next() is used to go through that iterator
#
# 🚫 Should You Call Dunder Methods Directly?
# Generally: No
#
# ✅ Use:
# len(my_list)        # instead of my_list.__len__()
# 'apple' in my_list  # instead of my_list.__contains__('apple')
# for x in my_list    # instead of manual iterator
# Dunder methods are for Python internals and for custom class design, not daily use.