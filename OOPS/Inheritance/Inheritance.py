


class parent():
    print("Its parent class")

class child(parent):
    print("Its child class")

c = child()

class Animal():

    def eat(self):
        print("Animal eats")

    def sleep(self):
        print("Animal Sleeps")

class Dog(Animal):

    def sound(self):
        print("Dog braks Bow Bow")

class Cat(Animal):

    def sound(self):
        print("Cats says meow meow")

d = Dog()
c=Cat()

d.eat()
d.sound()
d.sleep()

c.sound()
c.sleep()
c.eat()


class Person():

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

class  student(Person):
        def show(self):
            print("Name is ",self.name," and gender is ",self.gender)

s = student("pari","female")
s.show()


# Example 1: Without super()

class parent():

    def __init__(self):
        print("parent construction called")

class child(parent):

    def __init__(self):
        print("student constuction called")

c = child()

#Example 2: With super()

class Parent():

    def __init__(self):
        print("calling parent consturction")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Calling child constuction")

c = Child()

class Person():
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks = marks


s=Student("Pari",99)
print(s.name)
print(s.marks)

class Company():

    def __init__(self,name,age,id,salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

class Employee(Company):

    def __init__(self,name,age,id,salary,marks,course):
        super().__init__(name,age,id,salary)
        self.marks = marks
        self.course = course

e = Employee("pari","33","CER070",30000,89,"SQL")
print(e.name)
print(e.id)
print(e.course)

class Hospital():

    def __init__(self,hospital_name,location):
        self.hospital_name = hospital_name
        self.location = location

class Patient(Hospital):

    def __init__(self,hospital_name,location,patient_name,disease):
        super().__init__(hospital_name,location)
        self.patient_name = patient_name
        self.disease = disease

p = Patient("KIMS","HUNLI","Kiran","Typhoid")
print(p.patient_name)
print(p.hospital_name)
print(p.disease)


class Book():

    def __init__(self,title,author):
        self.title = title
        self.author = author

class LibraryBook(Book):

    def __init__(self,title,author,book_id,shelf_no):
        super().__init__(title,author)
        self.book_id = book_id
        self.shelf_no = shelf_no

l = LibraryBook("vimal","bharati","123kol",121)
print(l.author,l.title)
print(l.book_id)

class Account:
    def __init__(self,account_no,holder_name):
        self.account_no = account_no
        self.holder_name = holder_name

class SavingsAccount(Account):
    def __init__(self,account_no,holder_name,balance,interest_rate):
        super().__init__(account_no,holder_name)
        self.balance = balance
        self.interest_rate = interest_rate


s = SavingsAccount(123,"pari",3000,11.5)
print(s.holder_name)

class Profession:

    def __init__(self,name,city):
        self.name = name
        self.city = city



class Teacher(Profession):

    def __init__(self,name,city,subject,experience):
        super().__init__(name,city)
        self.subject = subject
        self.experience = experience

t = Teacher("pari","Banglore","Science",5)
print(t.experience)

class College:
    def __init__(self,college_name,city):
        self.college_name = college_name
        self.city = city

class Student(College):
    def __init__(self,college_name,city,student_name,course,marks):
        super().__init__(college_name,city)
        self.student_name = student_name
        self.course = course
        self.marks = marks
s= Student("KIIMS","Hubli","pari","MBBS","88.99")
print(s.student_name,s.college_name,s.course)

#3. Single Inheritance

class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name

class Customer(Bank):

    def __init__(self,bank_name,customer_name,account_no):
        self.customer_name = customer_name
        self.account_no = account_no

c = Customer("SBI","Pari","1234LKJH0987")
print(c.customer_name,c.account_no)

class Vehicle:

    def start_engine(self):
        print("start_engine method")

class Car(Vehicle):

    def drive(self):
        print("drive method ")

c = Car()
c.start_engine()
c.drive()

class Grandfather:

    def land(self):
        print("Land belongs to Grandfather")

class Father(Grandfather):

    def house(self):
        print("House belong to Father")

class Son(Father):

    def bike(self):
        print("Bike is belongs to Son")

s = Son()
s.bike()
s.house()
s.land()


class Company:

    def company_name(self):
        print("The company name is Cervello")

class Manager(Company):

    def team_name(self):
        print("The team name is Kenvue")

class TeamLead(Manager):

    def employee_count(self):
        print("The employee count is 25")

t = TeamLead()

t.employee_count()
t.team_name()
t.company_name()

class animal:
    def sound(self):
        print("Animal makes sound ")

class Dog(animal):

    def sound(self):
        print("Dog braks")

d = Dog()
d.sound()

class payment:

    def pay(self):
        print("payment processing")


class UPI(payment):

    def pay(self):
        print("paymeny UPI processing ")

u = UPI()
u.pay()



class Employee:

    def work(self):
        print("employee working")


class Developer(Employee):

    def work(self):
        super().work()
        print("Developer writing code ")

d = Developer()
d.work()


class Browser:
    def open(self):
        print("Browser opening")

class Chrome(Browser):
    def  open(self):
        super().open()
        print("Chrome browser opening")

c = Chrome()
c.open()


class person:
    def work(self):
        print("Person working")


class Teacher(person):
    def work(self):
        super().work()
        print("Teacher working")

class Pricipal(Teacher):
    def work(self):
        super().work()
        print("Principal working")

p = Pricipal()
p.work()







