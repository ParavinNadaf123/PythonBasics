a= 330
b=390
if a>b:
    print("a is greater than b")
else:
    print("b is greater than b")

 #✅ 1. Check if a number is positive, negative, or zero
x=int(input("enter the number:"))
if x >0:
    print("the given number is positive")
elif x<0:
    print("the given number is negative")
else:
    print("the given number is zero")

#check the largest number of 3
p=int(input("enter the number p:"))
q=int(input("enter the number q:"))
r=int(input("enter the number r:"))

if p>=q and p>=r:
    print("p is greater")
elif q>=r and q>=p:
    print("q is greater")
else:
    print("r is greater")

#grade on marks
marks=float(input("enter the marks :"))

if marks >=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Grade D")
else:
    print("Fail")

 # leap year
year = int(input("Enter the year :"))
if (year % 4 == 0 and  year % 100 != 0) or (year % 400==0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#✅ 5. Check if a number is even or odd
num=int(input("Enter the num:"))
if (num %2==0):
    print("the number is even ")
else:
    print("the number is odd")

#


