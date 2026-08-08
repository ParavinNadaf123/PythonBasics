

class PiggyBank:

    def __init__(self):
        self.__money = 0   # private variable


    def add_money(self,amount):
         self.__money += amount


    def show_money(self):
       print("Money",self.__money)

p = PiggyBank()
p.add_money(100)
p.add_money(50)

p.show_money()


class BankAccount():

    def __init__(self):
        self.__balance = 1000

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
             self.__balance -= amount
        else:
            print("Insufficient")

    def show_balance(self):
        print("The current balance ",self.__balance)


b = BankAccount()

b.deposit(500)
b.withdraw(2000)
b.show_balance()

class Mobile:

    def __init__(self,pin):
        self.__pin = pin

    def unlock(self,entered_pin):
        if  entered_pin == self.__pin:
            print("Phone Unlocked")
        else:
            print(" wroung pin , try again ")

m = Mobile("987")
m.unlock("987")


class Employee:

    def __init__(self):
        self.__salary = 30000

    def get_salary(self):
        print("The current salary is ",self.__salary)

    def set_salary(self , new_salary):
        if new_salary > 0 :
            self.__salary = new_salary
        else:
            print( "Invalid salary")

e = Employee()
e.get_salary()


e.set_salary(40000)
e.get_salary()

class Login:

    def __init__(self):
        self.__password = "admin123"

    def login(self,password):
        if self.__password == password:
            print("Correct password")
        else:
            print("Incorrect password")

    def change_password(self,old_password,new_pasword):
        if self.__password == old_password:
            self.__password = new_pasword
            print("The passwrod is changed succesfully from ",old_password ,"to",new_pasword)
        else:
            print("Old password is incorrect. Cannot change password")


l = Login()
l.login("admin123")
l.change_password("admin123","admin321")
l.login("admin321")

class Product:

    def __init__(self):
        self.__price = 1000

    def update_price(self,price):
        if price > 0:
            self.__price = price
            print("Price updated to", self.__price)

        else:
            print("Price cannot be 0 or negative, Invalid price")


pr = Product()
# pr.update_price(-1000)
# pr.update_price(100)
pr.update_price(100)

class ATM:

    def __init__(self):
        self.__balance = 2000

    def deposit(self,deposit_amount):
        self.__balance += deposit_amount

    def withdraw(self,withdraw_amount):
        if withdraw_amount <= self.__balance:
            self.__balance -= withdraw_amount
        else:
            print("can not withdrawing more than balance")

    def check_balance(self):
        print("The current balance ",self.__balance)

a = ATM()
# a.check_balance()
a.deposit(1000)
a.withdraw(5000)
a.check_balance()
a.withdraw(500)
a.check_balance()
