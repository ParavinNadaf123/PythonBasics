# class car:
#     name = "Audi"
#     gen = "5"
#
# c1 = car()
# print(c1.name)
# print(c1.gen)
# #
# class movie:
#     name = "Don"
#     year = "2020"
#
# m1= movie()
# print(m1.name)
# m2 = movie()
# print(m2.year)

#
# class Student:
#     name = 'karan'
#     age = 10
#     def __init__(self,fullname,surname):
#         self.name= fullname
#         self.secName = surname
#         print("adding new data")
#
#
# s1 = Student("Karan","shah")
# # print(s1.age)
# print(s1.name)
# print(s1.secName)



class Employee:
    # e_name = "pari"
    # e_id = 112
    # e_salary = 10000
    def __init__(self,fullname,emp_id,emp_sal):
        self.name = fullname
        self.id = emp_id
        self.salary = emp_sal
e1 = Employee("pari",112,10000)
# print(e1.e_salary)
print(e1.name)
print(e1.id)
print(e1.salary)

class Laptop:
    # brand ="dell"
    # process = "i3"
    # price = 70000
    def __init__(self,brandName,laptopProcesor,laptop_price):
        self.brand = brandName
        self.processor= laptopProcesor
        self.price = laptop_price
        # print("calling contruction")

l1 = Laptop("lenovo","i7",1000000)
# print(l1.brand)
print(l1.brand)
print(l1.processor)
print(l1.price)

