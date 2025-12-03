# def xyz():
#     print("Hello")
# xyz()

#add two values
#without reurn
# def add(x,y):
#     print(x+y)
# p=9
# q=8
# res=add(p,q)
# print(res)
# print(res)

##with return type
# def add(x,y):
#     z=x+y
#     return z
# p=9
# q=8
# res=add(p,q)

# def add(x,y):
#     z=x+y
#     return z
# p=9
# q=8
# res=add(p,q)
# print(res)

# print(print("Hello"))

# def add(x,y):
#     return(x+y)
# p=9
# q=8
# print(add(p,q))

#with argument with return
# def sub(x,y):
#     return(x-y)
# x=6
# y=2
# print(sub(x,y))

#with argument without return
# def mul(x,y):
#     print(x*y)
# p=int(input("Value:" ))
# q=int(input("value: "))
# mul(p,q)

#without argument with return
# def div():
#     return(p//q)
# p=8
# q=2
# print(div())

#without argument without return
# def add():
#     print(p+q)
# p=9
# q=5
# add()

#factorial using function
# def factorial(a):
#     ans=1
#     for i in range(1,a+1):
#         ans*=i
#     return ans
# num = int(input("Enter a number : "))
# answer=factorial(num)
# print(answer)


#print(n natural numbers)
# def print_nat():
#     li=[]
#     for i in range(11):
#         li.append(i)
#     return li

# numbers=print_nat()
# print(numbers)

#fibonacci series
# n=int(input("Enter value :"))
# fi=0
# se=1
# print(fi,se,end=' ')
# for i in range(n-2):
#     nx=fi+se
#     fi=se
#     se=nx
#     print(nx,end=" ")

# num=5
# fi=0
# se=1
# for i in range(num):
#     print(fi,end=" ")
#     fi,se =se,fi+se

#prime
# n=int(input("Enter a number : "))
# count=0
# for i in range(2,n):
#     if n%i==0:
#        count+=1
# if count==0:
#     print("Prime")
# else:
#     print("Not prime")

# n=int(input("Enter a number : "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#        count+=1
# if count==2:
#     print("Prime")
# else:
#     print("Not prime")

# n=int(input("Enter a number : "))
# ans=True
# for i in range(2,n):
#     if n%i==0:
#        print("Not a prime")
#        ans=False
#        break
# if ans==True:
#   print("prime")

#positional argument
# def add(x,y,z):
#     return x+y+z
# p,q,r=23,65,43
# res=add(89,89,56)
# res=add(int(input("Enter a number :")),int(input("Enter a number :")),int(input("Enter a number :")))
# print(res)

# #default positional argument
# def add(x=0,y=0,z=0):
#     return x+y+z
# # res=add()
# # res=add(10)
# # res=add(10,20)
# res=add(10,20,30)
# print(res)

#variable length positional argument
# def add(*args):
#     print(args)
#     print(type(args))
# add(10,20,19,20,30,23,32,33)

# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# sum_n=add(10,20,19,20,30,23,32,33)
# print(sum_n)

# def add(*n):
#     sum=0
#     for i in n:
#         for j in i:
#             sum=sum+j
#         return sum
# sum_n=add(eval(input("Enter any value :")))
# print(sum_n)

# def add(*n):
#     print(n)
#     print(type(n))
# add(*eval(input("Enter any value : ")))

#key-word argument
# def add(x,y,z):
#     print(z)
#     print(x)
#     print(y)
# p=10
# q=20 
# r=30
# add(z=p,y=q,x=r)

#default key-word argument
# def add(x=0,y=0,z=0):
#     print(z)
#     print(x)
#     print(y)
#     print(x+y+z)
# p=10
# q=20 
# r=30
# # add(z=p,y=q,x=r)
# add()
# add(p,q)

#variable length key-word argument
# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# add(x=10,y=20,z=30,p=5,q=4)

# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# add(**eval(input("Enter any dict : ")))

# calling of function is called unpacking while declaration of a function is called packing.

# def add(**kwargs):
#     #for i in kwargs.keys():
#         #print(i)
#     #for i in kwargs.values():
#         #print(i)
#     for i,j in kwargs.items():
#         print('key = ',i,'value = ',j)
# add(x=10,y=20,z=30,p=5,q=4)

# def add(x,y=0,*z,p,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)
# add(10,20,30,40,50,p=5,r=4,s=3,t=9)

# def add(x,*z,y=0,p,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)
# add(10,20,30,40,50,p=5,r=4,s=3,t=9)

# def add(x,p,*z,y=0,**q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)
# add(10,p=20,r=4,s=3,t=9)

# def natural_no(n):
#     for i in range(1,n+1):
#         print(i)
# n=int(input("Enter any number : "))
# natural_no(n)


# def natural_no(n):
#     sum=0
#     for i in range(1,n+1):
#         print(i)
#         sum=sum+i
#     print(sum)
# n=int(input("Enter any number : "))
# natural_no(n)

# def even_no(n):
#     for i in range(1,n+1):
#         print(2*i)
# n=int(input("Enter any number : "))
# even_no(n)

# def prime_num(n):
#     count=0
#     for i in range(1,n+1):
#         if( n%i==0):
#             count+=1
#     if count==2 :
#         print("prime")
#     else:
#         print("not prime")
# n=int(input("Enter a number :"))
# prime_num(n)
# n=int(input("Enter"))
# def prime_num(n):
#     count=0
#     for i in range(1,n+1):
#         if( n%i==0):
#             count+=1
#     if count>=2 :
#         return 'not_prime'
# print ('prime')
# n=int(input("Enter a number :"))
# print('prime')
# prime_num(n)

#local variable(access within a block of code)
# def display():
#     x=10       #local variable
#     print(x)
# display()
# print(x)

#local variable to global variable
# def display():
#     global x     #here x is globalised
#     x=10
#     print(x)
# display()
# print(x) 

# def display():
#     global x     #here x is globalised
#     x=10
#     print(x)
# print(x)          #x cannot be called whenever function is not called & also not globalized 
# display()            # x is not called global because here x is not accessable from block of code
# print(x)    

#global variable
# x=10
# def show():
#     print(x)
# print(x)
# show()
# print(x)

# x=10
# def show():
#     x=20
#     print(x)
# print(x)     #x=10 global 
# show()
# print(x)

# x=10
# def show():
#     print(x) #variable is same
#     x=20
#     print(x)
# show()

# x=10
# def show():
#     x=20
#     print(globals()['x'])
# show()

#non local
# def show():
#     x=10
#     def display():
#         print(x)
#     display()
# show()

def show():
    x=10
    def display():
        nonlocal x   #used to take value from local variable
        x=x+5
        print(x)
    display()
show()

def show():
    x=10
    def display():
        nonlocal x   #used to take value from local variable
        x=x+5
        print(x)
    display()
show()