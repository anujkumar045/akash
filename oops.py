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

# class student:
#     def __init__(self):
#         print("Constructor called")
#         print(id(self))    #self is a reference parameter which hold the current address of current class of current object
# obj1=student
# print(id(obj1),id(student))
# obj2=student()  
# print(id(obj2),id(student))

#'''physical existance of any layout is called object'''
#'''dummy layout is called is called class'''

# class student:
#     x=10
#     y=20
#     def __init__(self):
#         print("Constructor Called")
#         print(id(self))
#     def __init__(self):
#         print("Hello")
# obj=student  #here it is internal constructor
# obj1=student()  #here it is external constructor #parenthesis is responsible for calling  external constructor
# print(id(obj),id(obj1)) #on chg int cons to external cons. address varies
#                       #for initial information external constructor is made
#                       #constructor is automatically called on creating object
# obj1.__init__()       #using this function the constructor which has recently made will be executed

# # Calling of object by using internal constructor
# class student:
#     school='DUV'
#     school_city='Areraj'
#     def detail():
#         print("from student class")
# obj=student
# print(obj.school,student.school)
# print(obj.school_city,student.school_city)
# obj.detail()
# student.detail()

# # Calling of object by using extrenal constructor
# class student:
#     school='DUV'
#     school_city='Areraj'
#     def detail(self): #parameter should be any value i.e. self,x,a,s,d,l but self is recommended because of instance method
#         print("from student class")
# obj=student()
# print(obj.school,student.school)
# print(obj.school_city,student.school_city)
# obj.detail()

class student:
    def __init__(self,name,age,grade):
        self.n=name
        self.a=age
        self.g=grade
    def display(self):
        print(self.n,self.a,self.g)

obj=student('Anuj','21','B.E.')
obj.display()                #to call assigned values inside the class
print(obj.n,obj.a,obj.g)     #to access/call outside the class
student().display()