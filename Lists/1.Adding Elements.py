# | Method         | Description                              | Notes / Differences                        |
# | -------------- | ---------------------------------------- | ------------------------------------------ |
# | `append(x)`    | Adds **one item** to the end of the list | Adds whole object (e.g., list as a list)   |
# | `extend(iter)` | Adds **each element** from an iterable   | Flattens input, only works with iterables  |
# | `insert(i, x)` | Inserts item `x` at position `i`         | Slower, as it shifts elements to the right |


#++++++++++++++++++append+++++++++++
lst = ["name",22,99.8,True,None,(2+3j)]

lst.append(["surname",66])
print(lst)
print(len(lst))
print(lst[0])

# )))))))))))))))))))extend

lst.extend(["address",4+5j,22.667])
print(lst)

# append() → adds one item (even if it's a list or object)
# extend() → adds each item from another iterable (list, tuple, etc.)

# ++++++++++++++++++++++++++insert+++++++++++

lst[3]="email"
print(lst)
lst.insert(7,10)
print(lst)
lst.insert(11,"height")
print(lst)




