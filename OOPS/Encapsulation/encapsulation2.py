from tokenize import Token


class ConfigManager:
    def __init__(self,url,browser):
        self.__url = url
        self.__browser = browser

    def get_url(self):
        print("The url is ",self.__url)

    def get_browser(self):
        print("Current browser is:", self.__browser)

    def set_browser(self,browser):
       if browser in ("chrome","firefox","edge"):
           self.__browser = browser
           print("Browser updated to :",self.__browser)
       else:
           print("Invalid browser")


c = ConfigManager("https://google.com", "firefox")
c.get_url()
c.get_browser()

c.set_browser("edge")
c.get_browser()

c.set_browser("safari")



class APILogin:
    def __init__(self):
        self.__token = None

    def generate_token(self,username,password):
        if (username  == "admin") and  (password == "123"):
            self.__token = "token123"
            print("The generated token is ",self.__token)
        else:
            print("Invalid credentail")



    def get_token(self):
        print("The current token",self.__token)

    def reset_token(self):
        self.__token = None
        print("Token reset")


a = APILogin()

a.get_token()                     # None
a.generate_token("admin","123")
a.get_token()                     # token_123
a.reset_token()                   # Token reset
a.get_token()                     # None


class Database:
    def __init__(self):
        self.__host = "localhost"
        self.__username = "admin"
        self.__password = "123"

    def connect(self):
        print("The connection done")

    def change_password(self,old,new):
        if self.__password == old :
            self.__password = new
            print("The updated password ",self.__password)
        else:
            print("Incorrect Password")



    def show_host(self):
        print("The host is ",self.__host)

db = Database()
db.connect()
db.change_password("123","456")
db.show_host()

class DriverManager:
    def __init__(self):
        self.__driver_status = "closed"

    def open_driver(self):
        if self.__driver_status == "closed":
            self.__driver_status = "open"
            print("The driver status is open from closed")
        else:
            print("Cannot open as it is already open")


    def close_driver(self):
        if self.__driver_status == "open":
            self.__driver_status = "close"
            print("The driver status is close from open")
        else:
            print("Cannot closed as it is already closed")

    def get_status(self):
        print("The driver status is ",self.__driver_status)

d = DriverManager()
d.open_driver()
d.get_status()

d.close_driver()
d.get_status()

class TestData:
    def __init__(self):
        self.__test_users = ["pari","zeeshan","reshu","razia"]

    def add_user(self,user):
            if  user not in self.__test_users :
                self.__test_users.append(user)
                print("The updated list of user after adding user ",self.__test_users)

    def remove_user(self,user):
            if user   in self.__test_users :
                self.__test_users.remove(user)
                print("The updated list of user after removing user", self.__test_users)
            else:
                print("Not in list ")

    def show_users(self):
        print("The current list of user ",self.__test_users)

t = TestData()
t.show_users()
t.add_user("javed")
t.show_users()
t.remove_user("hasan")
t.show_users()

class Wallet:

    def __init__(self):
        self.__money = 500

    def add_money(self,amount):
        if amount > 0:
            self.__money += amount
            print("The amount in wallet after adding:", self.__money)
        else:
            print("Invalid amount. Cannot add zero or negative money.")
    def spend_money(self,amount):
        if amount <= 0:
            print("Invalid amount. Spend amount must be greater than 0.")
        elif amount <= self.__money:
            self.__money -= amount
            print("The amount in wallet after spending:", self.__money)
        else:
            print("Cannot spend more than available money.")

    def show_money(self):
        print("The amount in wallet", self.__money)

w = Wallet()


w.show_money()
w.add_money(100)
w.add_money(-50)
w.spend_money(1000)
w.spend_money(-20)
w.spend_money(200)
w.show_money()


class Laptop:
    def __init__(self):
        self.__battery = 100

    def use_battery(self,percent):
        if percent <= 0:
            print("Invalid battery usage")
        elif self.__battery - percent >= 0:
            self.__battery -= percent
            print("The battery after use",self.__battery)
        else:
            print("Battery cannot go below 0")


    def charge_battery(self,percent):
        if percent <= 0:
            print("Invalid battery usage")
        elif self.__battery + percent <= 100:
            self.__battery += percent
            print("The battery after charging",self.__battery)
        else:
            print("Battery cannot exceed 100")



    def show_battery(self):
        print("The battery percentage",self.__battery)

l = Laptop()
l.use_battery(30)
l.show_battery()

l.charge_battery(20)
l.show_battery()

l.use_battery(100)
l.charge_battery(50)

class Student:

    def __init__(self):
        self.__marks = 70

    def set_marks(self,marks):
        if marks >=0 and marks <= 100:
            #    0 <= marks <= 100:
            self.__marks = marks
            print("The marks are set to ",self.__marks)
        else:
            print("Invalid marks ")

    def get_marks(self):
            print("The marks are ",self.__marks)



s = Student()
s.get_marks()
s.set_marks(80)
s.get_marks()

s.set_marks(110)
s.get_marks()

s.set_marks(-11)
s.get_marks()

class Subscription:
    def __init__(self):
        self.__plan = "Basic"

    def change_plan(self,new_plan):
        if new_plan in ("Basic","premium","Standard"):
            self.__plan = new_plan
        else:
            print("Invalid plan")

    def show_plan(self):
        print("The plan is ",self.__plan)

s1 = Subscription()
s1.show_plan()

s1.change_plan("Standard")
s1.show_plan()

s1.change_plan("gold")
s1.show_plan()


class Email:

    def __init__(self):
        self.__password = "admin123"

    def login(self,password):
        if password == self.__password:
            print("Correct passwrod")
        else:
            print("incorrect password")

    def reset_password(self,old_password,new_password):
        if  self.__password == old_password:
            self.__password = new_password
            print("The passwrod is changed succesfully from ", old_password, "to", new_password)
        else:
                print("Old password is incorrect. Cannot change password")


e = Email()
e.login("admin123")
e.reset_password("admin123", "lolo098")
e.login("lolo098")

class Cart:

    def __init__(self):
        self.__items = ["Bag","jeans","TiffinBox","t-shirt"]

    def add_item(self,new_items):
        # new_items= ["waterBottle","Jacket"]
        self.__items.extend(new_items)
        print("The items after adding items",self.__items)

    def remove_items(self,remove_items):
        if remove_items in self.__items:
            self.__items.remove(remove_items)
            print("Items after removeing",self.__items)
        else:
            print("Cannot remove non-existing item.")

    def show_items(self):
        print("The items in the list are ",self.__items)

c = Cart()
c.show_items()

c.add_item(["Mobile","Laptop"])
c.show_items()

c.remove_items("jeans")
c.show_items()

c.remove_items("Jacket")
c.show_items()

class BrowserSession:
    def __init__(self):
        self.__status = "close"

    def open(self):
        if self.__status == "close":
            self.__status = "open"
        else:
            print("Its is already open")

    def close(self):
        if self.__status == "open":
            self.__status = "close"
        else:
            print("Its already closed")

    def get_status(self):
        print("The current status of browser ",self.__status)

b = BrowserSession()
b.get_status()

b.open()
b.get_status()

b.close()
b.get_status()


class APIClient:

    def __init__(self):
        self.__request_count= 0
        self.max_request = 5

    def send_request(self):
        if self.__request_count < self.max_request :
            self.__request_count += 1
            print("API request sent ",self.__request_count)
        else:
            print("Request limit exceeded")



    def show_count(self):
        print("The current API request sent ",self.__request_count)

a = APIClient()
a.show_count()

a.send_request()
a.send_request()
a.send_request()
a.send_request()
a.send_request()
a.send_request()

a.show_count()

class DBPool:

    def __init__(self):
        self.__connections = 3

    def use_connection(self):
        if self.__connections > 0:
            self.__connections -= 1
            print("The avaliable connection are ",self.__connections)
        else:
            print("No connections available")


    def release_connection(self):
        if self.__connections < 3:
            self.__connections += 1
            print("The release connection are ",self.__connections)
        else:
            print("Connection released are rejected")


    def show_connections(self):
        print("The current db connection ",self.__connections)

dbp = DBPool()
dbp.use_connection()
dbp.use_connection()
dbp.use_connection()
dbp.use_connection()

dbp.release_connection()
dbp.release_connection()
dbp.release_connection()
dbp.release_connection()

dbp.show_connections()


class OTPSystem:
    def __init__(self):
        self.__otp= None

    def generate_otp(self):
        self.__otp = "8987"
        print("The generated OTP ",self.__otp)

    def verify_otp(self,user_otp):
        if  user_otp == self.__otp:
            print("The otp is correct matched",self.__otp)
        else:
            print("Incorrect OTP")


    def reset_otp(self):
        self.__otp = None
        print("The OTP is reset",self.__otp)


o = OTPSystem()
o.generate_otp()
o.verify_otp("9898")
o.reset_otp()