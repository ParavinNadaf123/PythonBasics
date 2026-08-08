class payment:
    def pay(self):
        print("processing payment")


class UPI(payment):
    def pay(self):
        print("Payment vai UPI")

class card(payment):
    def pay(self):
        print("Paying via crad")

UPI().pay()
card().pay()
# =============================================

class Notification:
    def send(self):
        print("sending notification")

class Email(Notification):
    def send(self):
        print("Sending Notification via email")

class SMS(Notification):
    def send(self):
        print("Sending notification via SMS")

Email().send()
SMS().send()

class Export:
    def generate(self):
        print("Generating file")

class PDF(Export):
    def generate(self):
        print("Generating PDF")

class Excel(Export):
    def generate(self):
        print("Generating excel")

PDF().generate()
Excel().generate()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++/?/

class User:
    def login(self):
        print("Login as user")

class Admin(User):
    def login(self):
        print("Login as Admin")

class client(User):
    def login(self):
        print("Login as client")

Admin().login()
client().login()

#Question 1: Browser Launch

class Browser:
    def launch(self):
        print("lunch the browser")

class Chrome(Browser):
    def launch(self):
        print("lunch the chrome")

class Firefox(Browser):
    def launch(self):
        print("launch the firefox ")

class Edge(Browser):
    def launch(self):
        print("launch the edge ")

Chrome().launch()
Edge().launch()
Firefox().launch()


class Validator:
    def validate(self):
        print("Validating the logic")

class EmailValidator(Validator):
    def validate(self):
        print("Email validating")

class PasswordValidator(Validator):
    def validate(self):
        print("Password validating")

class OTPValidator(Validator):
    def validate(self):
        print("OTP validating")


EmailValidator().validate()
OTPValidator().validate()

# ==================================

class APIRequest:
    def send(self):
        print("API Request sent")

class GetRequest(APIRequest):
    def send(self):
        print("get API request ")

class PostRequest(APIRequest):
    def send(self):
        print("Post API request")

class DeleteRequest(APIRequest):
    def send(self):
        print("delete the API request")

GetRequest().send()
PostRequest().send()


# =====================================

class Report:
    def generate(self):
        print("genearte the report")

class HTMLReport(Report):
    def genarate(self):
        print("generate the HTML report")
class JSONReport(Report):
    def genarate(self):
        print("generate the JSON report")
class XMLReport(Report):
    def genarate(self):
        print("generate the XML report")

HTMLReport().genarate()
JSONReport().genarate()
XMLReport().genarate()


class Database:
    def connect(self):
        print("Database connected")

class MySQLDB(Database):
    def connect(self):
        print("MYSQLDB connected")

class OracleDB(Database):
    def connect(self):
        print("MYSQLDB connected")


class MongoDB(Database):
    def connect(self):
        print("MongoDB connected")

MySQLDB().connect()
MongoDB().connect()
