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

# class student:
#     def __init__(self,name,age,grade):
#         self.n=name
#         self.a=age
#         self.g=grade
#     def display(self):
#         print(self.n,self.a,self.g)
# obj=student('Anuj','21','B.E.')
# obj.display()                #to call assigned values inside the class
# print(obj.n,obj.a,obj.g)     #to access/call outside the class
# student().display()

"""# variables which are object dependent(which change on changing of objects) are called as instance variable.
#ex : name,email,contact
#variables which are not object dependent are called as class variable.
#ex : s.name,schoolcentercode
#variables which are fully independent are called local variable.
#ex : personalized 
#Instance of class is called object"""

'''Instance Variable'''
class student:
    def __init__(self,name,contact):
        self.n=name
        self.c=contact      #declaration inside constructor
        print(self.n,self.c) #calling inside constructor
    def add_new(self,roll_no):
        self.r=roll_no           #declaration inside instance method
    def display(self):
        print(self.n,self.c,self.r,self.email)     #calling inside instance method
obj=student('Anuj',7543080248)
obj.add_new('CS0020')
obj.email='anuj@gmail.com'   #declaration outside of the class
obj.display()
print(obj.n,obj.c,obj.r,obj.email)  #calling outside of the class
obj1=student('V',9890808367)

"""Class Variable"""
'''Declaration and calling of class is using name of class.'''
class student:
    school_name='SHSS'
    def __init__(self,name,roll_no):
        self.n=name
        self.r=roll_no
        student.school_city='Bhopal'
        print(student.school_city,student.school_name)
    def add_new(self):
        student.school_code=101
        print(student.school_city,student.school_name,student.school_code,student.contact)
student.contact=123455678
obj=student('Anuj',123)
obj.add_new()
print(student.contact,student.school_name,student.school_city,student.school_code)
print(obj.contact,obj.school_name,obj.school_city,obj.school_code)#This is accessable but we can't call
                                                                    #using object in class variable method.

"""Local variable"""
'''Variable which are call in scope is called local variable.'''
class student:
    def __init__(self):
        x=10
        print(x)
    def new(self):
        y=20
        z=y+10
        print(z)
        #print(x)
obj=student()
obj.new()