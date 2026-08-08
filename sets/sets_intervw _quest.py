# 2️⃣ How do you remove duplicates from a list using a Set?

number = [1,2,3,4,5,6,7,2,6,4]
unique_num = set(number)
print(unique_num)


s = {1, 2, 3}

s.add(4)
print(s) # Add single element
s.update([5, 6]) # Add multiple
print(s)

s.remove(2)      # Remove element (error if not found)
print(s)

s.discard(3)    # No error if not found
print(s)

# 3️⃣ Why can’t we store a list inside a set?
#
# 🗣 Answer:
# Because lists are mutable (changeable) and unhashable.

# my_set = {1, 2, 3}
# my_set.add([4, 5])  # ❌ Error: unhashable type: 'list'