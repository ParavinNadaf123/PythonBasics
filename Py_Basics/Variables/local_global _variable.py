# x=10  #Global variable
#
# def call_num():
#     print("inside function ,x = ",x)
#
# call_num()
# print("outside function , x=",x)
#
# #==========================Local variable
#
#
# def show():
#     y= 20 #local variable
#     print("inside function ,y = ",y)
#
# show()
# print("outside function ,y = ",y)
#
#
# #==================overwriting the global variable insed funt without global keyword
#
# z=30
#
# def update():
#     z=40
#     print("inside function ,z = ", z)
# update()
#
# print("outside function ,z = ", z)
#
#
# #==================modifying global variable inside funct using global keyword
#
# q=5

def modify_num():
    global q
    q=100
    print("inside function ,q = ", q)

modify_num()
print("outside function ,q = ", q)
#
#
# #nested funt and scope

def outer():
    c = 60

    def inner():
        print("inside function ,c = ", c)
    inner()

outer()

#============

def outer():
    outer_var = "I'm from outer!"

    def inner():
        print("Inner function says:", outer_var)

    inner()

outer()
#
#
#
