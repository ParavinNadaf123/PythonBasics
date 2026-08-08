# Different classes with same method.

class Resume:
    def print_Doc(self):
        print("printing resume")

class Invoice:
    def print_Doc(self):
        print("printing Invoice")

def printer(doc):
    doc.print_Doc()

printer(Resume())
printer(Invoice())

#===============================================Example 2: Upload System
class Image:
    def upload(self):
        print("Image uploading")

class Video:
    def upload(self):
        print("Video uploading")

def upload_file(file):
    file.upload()

upload_file(Image())
upload_file(Video())


# ==================================== Example 3: Delivery Service

class BikeDelivery:
    def deliver(self):
        print("Deliver bike")

class DroneDelivery:
    def deliver(self):
        print("deliver drone")

def send(item):
    item.deliver()

send(BikeDelivery())
send(DroneDelivery())

class OTP:
    def verify(self):
        print("OTP Verified")

class Fingerprint:
    def verify(self):
        print("Fingerprint verified")

def authetication(method):
    method.verify()


authetication(OTP())
authetication(Fingerprint())

#========================Example 5: Report Generation

class SalesReport:
    def build(self):
        print("sales report build")

class AuditReport:
    def build(self):
        print("Audit report build")

def generate(report):
    report.build()


generate(SalesReport())
generate(AuditReport())


# ===============================----------------------------------------------------

class ChromeScreenshot:
    def capture(self):
        print("capture chrome screen shot")

class MobileScreenshot:
    def capture(self):
        print("capture Mobile screen shot")

class DesktopScreenshot:
    def capture(self):
        print("Capture  desktop screenshot")

def take_screenshot(device):
    device.capture()

take_screenshot(ChromeScreenshot())
take_screenshot(MobileScreenshot())
take_screenshot(DesktopScreenshot())

# ===================================================================
class FileReader:
    def read(self):
        print("Read the file")

class CSVReader:
    def read(self):
        print("Read the CSV file")

class ExcelReader:
    def read(self):
        print("Read the Excel file")

class JSONReader:
    def read(self):
        print("Read the JSON file")


def file_reader(file):
    file.read()

file_reader(ExcelReader())
file_reader(JSONReader())
file_reader(CSVReader())

# =====================================
class ConsoleLogger:
    def log(self):
        print("Log the console")

class FileLogger:
    def log(self):
        print("Log file")

class DatabaseLogger:
    def log(self):
        print("log the database")

def write_log(logger):
    logger.log()

write_log(FileLogger())
write_log(DatabaseLogger())
write_log(ConsoleLogger())


class UITest:
    def execute(self):
        print("execute the UI Test")


class APITest:
    def execute(self):
        print("execute the API Test")

class DBTest:
    def execute(self):
        print("execute the DB Test")

def run(test):
    test.execute()

run(APITest())
run(UITest())
run(DBTest())

class ImplicitWait:
    def wait(self):
        print("Implicit wait")

class ExplicitWait:
    def wait(self):
        print("Explicit wait")

class FluentWait:
    def wait(self):
        print("Fluent Wait")

def apply_wait(strategy):
    strategy.wait()

apply_wait(ImplicitWait())
apply_wait(ExplicitWait())
apply_wait(FluentWait())