class BaseTest:

    def __init__(self,browser,url):
        self.browser = browser
        self.url = url

    def setup(self):
        print("Setup browser and open URL")



    def teardown(self):
        print("close browser")


class LoginTest(BaseTest):
    def __init__(self,browser,url,username,password):
        super().__init__(browser,url)
        self.username = username
        self.password = password

    def setup(self):
        print("Open login page")


    def run_test(self):
        # super().teardown()
        # super().setup()
        print("running tests")

    def display(self):
        print("Browser:",self.browser)
        print("URL:",self.url)
        print("username:",self.username)
        print("password:",self.password)


l = LoginTest("google","wwww.amazon.com","pari","123admin")
l.setup()
l.run_test()
l.teardown()
l.display()

class DatabaseConnection:
    def __init__(self,db_name,host):
        self.db_name = db_name
        self.host = host

    def connect(self):
        print("Connected for ETL validation")


class ETLValidation(DatabaseConnection):
    def __init__(self,db_name,host,source_table,target_table):
        super().__init__(db_name,host)
        self.source_table = source_table
        self.target_table = target_table

    def connect(self):  # overriding
        super().connect()
        print("Connected for ETL validation")

    def validate_data(self):
        super().connect()
        print("data validated")

e = ETLValidation("kenvue","Ken123","kenvue","JandJ")
e.validate_data()



class APIBase:

    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def send_request(self):
        print("The request sent")


class UserAPI(APIBase):

    def __init__(self, base_url, token, user_id):
        super().__init__(base_url, token)
        self.user_id = user_id

    def send_request(self):
        super().send_request()
        print("Fetching user API data")

    def get_user_details(self):
        self.send_request()
        print("The user details")


u = UserAPI("http://www.api.com", "API123", "Pari098")
u.get_user_details()


class ReportGenerator:

    def __init__(self,report_name,created_by):
        self.report_name = report_name
        self.created_by = created_by

    def generate(self):
        print("The report generated")

class TestReport(ReportGenerator):

    def __init__(self,report_name,created_by,total_tests,passed_tests,failed_tests):
        super().__init__(report_name,created_by)
        self.total_tests = total_tests
        self.passed_tests = passed_tests
        self.failed_tests = failed_tests

    def generate(self):
        super().generate()
        print("Total Tests:", self.total_tests)
        print("Passed Tests:", self.passed_tests)
        print("Failed Tests:", self.failed_tests)


t = TestReport("Test Case Report","pari",30,28,2)
t.generate()

class Browser:

    def open(self):
        print("The browser opened")

class ChromeBrowser(Browser):

    def open(self):
        super().open()
        print("The chrome browser opened ")


class HeadlessChrome(ChromeBrowser):
    
    def open(self):
        super().open()
        print("The headless browser open")

    def run_headless(self):
        print("running headless mode")
        

h = HeadlessChrome()
h.open()
h.run_headless()