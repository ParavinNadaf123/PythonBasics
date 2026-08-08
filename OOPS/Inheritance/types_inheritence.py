# single
class A:

    def show(self):
        print("Class A")

class B(A):

    def show(self):
        pass

obj_b = B()
obj_b.show()


# =====================


#multiLevel  inheritence


class A:

    def show(self):
        print("Class A")

class B(A):

    def show(self):
        print("Class B")

class C(B):

    def show(self):
        print("Class C")

obj_c = C()
obj_c.show()
#=================================================================

 # Multiple inheritance
class Father():

    def skill1(self):
        print("Driving")

class Mother:

    def skill2(self):
        print("Cooking")

class Child(Father,Mother):
    pass

c = Child()
c.skill1()
c.skill2()


# Method Overriding ===========================================

class Animal:

    def sound(self):
        print("Animal makes sound ")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog braks ")

d = Dog()
d.sound()

class Employee:
     def work(self):
         print("Employee works")

class Teacher(Employee):
    def work(self):
        super().work()
        print("Teacher Teaches")

t = Teacher()
t.work()

# ============================================================
class Mobile:

    def __init__(self,brand,price):
        self.brand = brand
        self.price =price

    def call(self):
        print("Calling ")

class SmartPhone(Mobile):

    def __init__(self,brand,price,camera_mp):
        super().__init__(brand,price)
        self.camera_mp = camera_mp

    def browse(self):
        print("Browser")

s=SmartPhone("Iphone","80000","90MP")
s.call()
s.browse()

print(s.brand,s.price)

class Animal:

    def eat(self):
        print("Animal Eats")

    def sleep(self):
        print("Animal Sleeps ")

class Lion(Animal):

    def hunt(self):
        print("Lion Hunts deer")

l = Lion()
l.hunt()
l.eat()
l.sleep()


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):

    def __init__(self,name,age,salary,department):
        super().__init__(name,age)
        self.salary = salary
        self.department = department


e = Employee("Pari",33,30000,"QA")
print(e.name,e.department,e.salary,e.age)

class Company:
    def __init__(self,name,location,employees):
        self.name = name
        self.location = location
        self.employees=employees

    def work(self):
        print("Company is running projects")

class Employee(Company):
    def __init__(self,name,location,employees,emp_name,salary,role):
        super().__init__(name,location,employees)
        self.emp_name = emp_name
        self.salary = salary
        self.role = role

    def work(self):
        super().work()
        print("Employee is working on testing")

    def display(self):
        print("Company Name:", self.name)
        print("Location:", self.location)
        print("Employee ID:", self.employees)
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)
        print("Role:", self.role)

e = Employee("cervello","hubli","cer101","pari",70000,"QA")
e.work()
e.display()