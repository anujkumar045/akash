# class student:
#     '''Ths is demo class'''
#     pass
# print(dir(student))
# print(student.__doc__)  #__doc__ is a variable

# class student:
#     '''This is demo class'''
#     x=10
#     y=19
#     def show():
#         print("Hello")
# print(student.__dict__)   #__dict__ is a variable

# class student:
#     '''This is demo class'''
#     x=10
#     y=19
#     def display():
#         print("Hello")
# print(dir(student))      #__init__() is a method that is known as constructor
# print(id(student))
# obj=student()           #external constructor is called  when object is made
# print(id(obj))
# obj2=student              #id of obj will be same # internal constructor is called
# print(id(obj2))

class student:
    def __init__(self):
        print("Constructor called")
        print(id(self))    #self is a reference parameter which hold the current address of current class
obj1=student
print(id(obj1),id(student))
obj2=student()  
print(id(obj2),id(student))