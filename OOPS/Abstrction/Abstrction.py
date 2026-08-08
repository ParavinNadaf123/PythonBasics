from abc import ABC,abstractmethod

class Vehical(ABC):  #Vehicle = Parent class + blueprint.

    @abstractmethod
    def start(self):
        print("The vehical starting ...")

class car(Vehical):  #Car inherits Vehicle.
    def start(self):
        print("Car starts with key")
        # pass

class bike(Vehical):
    def start(self):
        print("Bike starts with self-start")
        # pass

c = car()
c.start()
#
b = bike()
b.start()

# v= Vehical()
# v.start() No actual implementation.

# Rule 1:
# Abstract class can have normal methods also. ( with out @abstractmethod also works)
# Rule 2:At least one abstract method makes class abstract.
# Rule 3:Child class must implement all abstract methods.

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("The dog braks bow bow")

class Cat(Animal):
    def sound(self):
        print("The cat says meow meow")

d = Dog()
d.sound()

c= Cat()
c.sound()
# =================================
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,r):
        self.r = r

    def area(self):
        # area_of_circle = (3.14 * r * r)
        print("The area of circl is ",3.14 * self.r* self.r)

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        # area_of_square = (l*b)
        print("The area of square is ", self.side * self.side)

C1 = Circle(5)
C1.area()

S1 = Square(4)
S1.area()

# ====================================

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self,salary):
        self.salary = salary

    def calculate_salary(self):
        print(" FullTimeEmployee : fixed salary = ",self.salary)


class PartTimeEmployee(Employee):

    def __init__(self,salary,hour):
        self.salary = salary
        self.hour = hour

    def calculate_salary(self):
        print(" PartTimeEmployee : hourly pay × hours = ",self.hour * self.salary)

f = FullTimeEmployee(50000)
f.calculate_salary()

p = PartTimeEmployee(10000,6)
p.calculate_salary()


# ============================================================
class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email sent" )

class SMSNotification(Notification):
    def send(self):
        print("SMS sent")

class WhatsAppNotification(Notification):
    def send(self):
        print("WhatsApp sent")

e = EmailNotification()
e.send()

sms = SMSNotification()
sms.send()
w = WhatsAppNotification()
w.send()

# ==========================
class Login(ABC):

    @abstractmethod
    def authenticate(self):
        pass

class GoogleLogin(Login):
    def authenticate(self):
        print(" GoogleLogin authenticate done")


class FacebookLogin(Login):
    def authenticate(self):
        print("FacebookLogin authenticate done ")


class OTPLogin(Login):
    def authenticate(self):
        print("OTPLogin authenticate done ")


g = GoogleLogin()
g.authenticate()

f = FacebookLogin()
f.authenticate()

o = OTPLogin()
o.authenticate()

# ==========================================================

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print("Paid",amount," using UPI")

class CreditCard(Payment):
    def pay(self,amount):
        print("Paid",amount ," using CreditCard")

class NetBanking(Payment):
    def pay(self,amount):
        print("Paid",amount,"  using NetBanking")


u = UPI()
u.pay(1000)

cc = CreditCard()
cc.pay(4777)

n = NetBanking()
n.pay(7000)

# ===============================
class BaseTest(ABC):

    @abstractmethod
    def open_browser(self):
        pass

    @abstractmethod
    def close_browser(self):
            pass

class ChromeTest(BaseTest):
    def open_browser(self):
        print("Chrome browser opened")

    def close_browser(self):
            print("Chrome browser closed")


class FirefoxTest(BaseTest):
    def open_browser(self):
        print("Firefox  browser opened")
    def close_browser(self):
            print("Firefox  browser closed")

c1 = ChromeTest()
c1.open_browser()
c1.close_browser()

f = FirefoxTest()
f.open_browser()
f.close_browser()


# from abc import ABC, abstractmethod
#
# class Test(ABC):
#
#     @abstractmethod
#     def run(self):
#         pass
#
# t = Test()