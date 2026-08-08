# Same operator behaves differently.
# Example 1: Integer Multiplication

# Operator Overloading in Python
#
# Operator overloading means giving special meaning to operators (+, -, *, ==, <) for objects.
#
# Python does this using magic methods (dunder methods) like:
#
# __add__() → +
# __sub__() → -
# __mul__() → *
# __eq__() → ==
# __lt__() → <


# 1. Add two products (+)

class Product:
    def __init__(self,price):
        self.price = price

    def __add__(self, other):
        return self.price + self.price

p1 = Product(100)
p2 = Product(50)

print(p1 + p2)

#=======================  2. Subtract account balance (-)
class Wallet:
    def __init__(self,amount):
        self.amount = amount

    def __sub__(self, other):
        return self.amount - other.amount


w1 = Wallet(100)
w2 = Wallet(50)

print(w1 - w2)



# ====================================

class Item:
    def __init__(self,price):
        self.price = price

    def __mul__(self, quantity):
        return self.price * quantity

i = Item(100)

print(i * 6)

class Student:
    def __init__(self,marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(90)
s2 = Student(30)
s3 = Student(90)

print(s1 == s2)
print(s1 == s3)


class File:

    def __init__(self,size):
        self.size = size

    def __lt__(self, other):
        return self.size < other.size

f1 = File(20)
f2 = File(50)

print(f1 < f2)

class testsuite:
    def __init__(self,tests):
        self.tests = tests

    def __add__(self, other):
        return  self.tests + other.tests

su1 = testsuite(20)
su2 = testsuite(70)

print(su1 + su2)


class Log:
    def __init__(self,text):
        self.text = text

    def __add__(self, other):
        return self.text + "\n" + other.text

l1 = Log("Login success")
l2 = Log("Payment success")

print(l1 + l2)


class TestTime:
    def __init__(self,time):
        self.time = time

    def __add__(self, other):
        return self.time + other.time

t1 = TestTime(10)
t2 = TestTime(10)

print("The total time took to  test" , t1 + t2,"minuties")

class TestData:
    def __init__(self,testdata):
        self.testdata = testdata

    def __add__(self,other):
        return self.testdata + other.testdata

td1 = TestData(["pari","Nadaf",33])
td2 = TestData(["zeeshan","nadaf",3])

print(td1 + td2)

class BuildVersion:
    def __init__(self,buildVersion):
        self.buildVersion = buildVersion

    def __lt__(self, other):
        return self.buildVersion > other.buildVersion

bv1 = BuildVersion(33.4)
bv2 = BuildVersion(44.5)

# print(bv1<bv2)
print(bv1>bv2)

class BugTracker:
    def __init__(self,bugatsp1):
        self.bugatsp1 = bugatsp1

    def __add__(self, other):
        return self.bugatsp1 + other.bugatsp1

bt1 = BugTracker(6)
bt2 = BugTracker(3)

print("bug counts from two sprints:",bt1+bt2)

class query:
    def __init__(self,condition):
        self.condition = condition

    def __add__(self, other):
        return  self.condition + " " + other.condition
q1 = query("select * from table 1 ")
q2 = query("where name = 'S%'")

print(q1 + q2)
