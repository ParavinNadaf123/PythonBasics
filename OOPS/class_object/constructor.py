#
# class Student:
#     school = "ABC School"   # Class attribute ,school is common for all students.
#     name = "any"
#
#     def __init__(self,fullname,salary):
#         self.name = fullname # # Instance attribute
#         self.salary = salary
#
#     def hello(self):
#         print("Hello All", self.name)
#
#     def get_salary(self):
#          return self.salary
#
# s1 = Student("Pari",30000)
# s2 = Student("koko",20000)
#
# print(s1.name,s1.salary)
# print(s2.name,s2.salary)
# print(Student.school)
# (s1.hello())
# print(s1.get_salary())
from fontTools.misc.cython import returns


class Std:
    # name = "pari"
    # marks = 99
    # def __init__(self,fullname,subj1,subj2,subj3):
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks= marks

        # self.subj1= subj1
        # self.subj2 = subj2
        # self.subj3 = subj3

    def get_avg (self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is :", sum / 3)


s1 = Std("pari",[88,57,98])
print(s1.get_avg())
