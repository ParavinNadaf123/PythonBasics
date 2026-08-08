# class student:
#     def hello():
#         print("hello")
#
# s1 = student()
# s1.hello()


class student:
    @staticmethod  #decorator
    def hello():
        print("hello")

s1 = student()
s1.hello()


class Bank:
    def __init__(self,balance,AcctNo):
        self.balance= balance
        self.accountNO= AcctNo

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount,"was debited ")
        print("Total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited ")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

b1 = Bank(10000,987)
# print(b1.accountNO,b1.balance)
b1.debit(1000)
b1.credit(2000)