l = ["pari","zeeshu","reshu"]
print(l)
print(type(l))

a=[]
print(a)
print(type(a))
#
# num_list = eval(input("Enter the numbers:"))
# print(num_list)
# print(type(num_list))

b = list(range(0,10))
print(b)
print(type(b))

n = "pari"
d=list(n)
print(d)

s = "my name is pari"
k = s.split()
print(k)
print(type(k))

h= [12,20,33,220]
print(h[-1])
# print(h[4])  --IndexError: list index out of range
print(h[3])
print(h[0:4])
print(h[3:5])

even = list(range(2,50,2))
print(even)


print(even[5:15:3])

h[0] = 100
print(h)
# h[4] = 50
# print(h) --IndexError: list assignment index out of range
h[2] = 40
print(h)

o = list(range(0,11))
print(o)
i = 0
while i < len(o):
    print(o[i])
    i= i+1



for n in o:
    if n %2 ==0:
        print(n)


g= [0,99,1,1,4,6,7,8,99,6,6]
print(g.count(1))
print(g.count(6))
print(g.index(99))
print(g.index(7))

d = []
d.append("a")
d.append("b")
d.append("c")
d.append("d")
print(" the list d contains",d)

r = []
for i in range(50):
    if i%10 == 0:
        r.append(i)
print(r)

f = ["orange","apple","kiwi","banana"]
print(f)
f.append("grape")
print(f)

f.insert(2,"blueberry")
print(f)

veg = ["onion","tomato","carrot","raddish","chilles"]
print(veg)
veg.insert(5,"potatoes")
print(veg)
veg.append("ladyfinger")
print(veg)
order1 = ["vadapav","panipuri","tea","momos","panipuri"]
order2 = ["dosa","paddu"]
# order2.extend("paneer tikka")
order1.extend(order2)
print(order1)
order1.remove("panipuri")
print(order1)
print(order1.pop())
print(order1.pop())
print(order1.pop())
print(order1)
j = [4,5,2,3,3]
print(j.pop())
print(j)
print(j.pop(1))
print(j)

# sorting and reversing
# reverse
x =  [1,2,9,8,7]
x.reverse()
print(x)
veg.reverse()
print(veg)
# sort
x.sort()
print(x)
veg.sort()
print(veg)

m = [99,98,77,55,76,90]
m.sort()
print(m)

w = [10,30,48,55,77,98,6]
w.sort()
print(w)

w.sort(reverse= True)
print(w)

s = ["t","f","l","e","w"]
s.sort(reverse= False)
print(s)
s.sort(reverse= True)
print(s)

target = [22,34,56,8998,99,2]
target_sorted = sorted(target)
print(target_sorted)
print(target)

# key=len means: “Sort the items by their length”
words = ['strawberry', 'fig', 'grape', 'melons','nut']
words.sort(key=len)
print(words)

name = ["pari","zeeshaan","paravinsultan","hussain"]
name.sort(key=len)
print(name)

r = [10,20,90,40,60]
e = r
print(r)
print(e)
print(id(r))
print(id(e))
r[3]=55
print(r)
print(e)

# slice operator

g= [77,98,65,46,85,54]
y = g[:]
print(g)
print(y)
g[3]=7
print(g)
print(y)


v = ["c","q","p"]
print(v)
z = v.copy()
v[1]=9
print(z)
print(v)
z[0]=88
print(z)
print(v)

b1 = [10,20,40]
b2 = [90,30,"x"]
v1 = b1 + b2
print(v1)
v2 = b1 + [30]
print(v2)
v3 = b2 * 2
print(v3)

rev_w1=[]
w1 = [10,30,48,55,77,98,6]
i = len(w1)-1
print(i)

while i >= 0:
    rev_w1.append(w1[i])
    i = i-1

print("Original list:", w1)
print("Reversed list:", rev_w1)

w1 = [10,30,48,55,77,98,77,30]
unique_num=[]
for n in w1:
    if n not in unique_num:
        unique_num.append(n)

print("Original List:", w1)
print("Without Duplicates (manual):", unique_num)


m1 = [99, 98, 77, 200, 76, 90, 101]

# Assume the first number is the largest
max_num = m1[0]

# Go through each number in the list
for i in m1:
    if i > max_num:
        max_num = i  # Update if current number is bigger

print("The largest number is:", max_num)

