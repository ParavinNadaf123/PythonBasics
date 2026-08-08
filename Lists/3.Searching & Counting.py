# | Method          | Purpose                                |
# | --------------- | -------------------------------------- |
# | `list.index(x)` | Finds **first index** of value `x`     |
# | `list.count(x)` | Counts how many times value `x` occurs |

# list.index(value, start=0, end=len(list))
# list.count(value)
#____________________________________index--------------------------
color = ["red","blue","indigo","purple","black","red","purple"]

print(color.index("purple"))
print(color.index("red"))#index() returns the first occurrence of 'red'
print(color.index("blue",1)) #search starting from index 4

#____________________________________count---------------
fruits=["banana","apple","leechi","cheery","orange","apple"]
print(fruits.count("apple"))