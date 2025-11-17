# n=4
# if n>=1:
#     print("Given no. is +ve")

# n=int(input("Enter any value :"))
# if n>=1:
#     print(f'given number {n} is +ve')
# else:
#     print(f'given number {n} is either zero or -ve')

# n=int(input("Enter any value :"))
# if n>=1:
#     print(f'given number {n} is +ve')
# elif n==0:
#     print(f'given number {n} is  zero')

# n=int(input("Enter any value :"))
# if n>=1:
#     print(f'given number {n} is +ve')
# elif n==0:
#     print(f'given number {n} is  zero')
# else:
#     print(f'given number {n} is -ve')

# age=float(input("Enter age : "))
# if 0<age<18:
#     print("Child")
# elif 17<age<60:
#     print("Adult")
# elif 59<age<100:
#     print("Senior citizen")
# else:
#     print("Please enter a valid age")

# hin=float(input("Enter marks of Hindi : "))
# if 0<=hin<=100 :
#     eng=float(input("Enter marks of English : "))
#     if 0<=eng<=100 :
#         ms=float(input("Enter marks of Maths : "))
#         if 0<=ms<=100 :
#             msc=float(input("Enter marks of Moral Science : "))
#             if 0<=msc<=100 :
#                 avg=(hin+eng+ms+msc)/4
#                 print(avg)
#                 if 0<=avg<35 :
#                     print("Fail")
#                 elif 35<=avg<45 :
#                     print("3rd Division")
#                 elif 45<=avg<60 :
#                     print("2nd Division")
#                 else :
#                     print("1st Division")
#             else :
#                 print("You have entered an invalid marks.")
#         else :
#             print("You have entered an invalid marks.") 
#     else:
#         print("You have entered an invalid marks.")
# else:
#     print("You have entered an invalid marks.")

# a=float(input("Enter a number : "))
# b=float(input("Enter a number : "))
# c=float(input("Enter a number : "))
# if(a>b and a>c) :
#     print(a)
# elif(b>c and b>c) :
#     print(b)
# else :
#     print(c)

# n=float(input("Enter a number : "))
# sqrt=n**0.5
# print(f'Squareroot of {n} is {sqrt}')

# base=float(input("Enter base of triangle : "))
# height=float(input("Enter height of triangle : "))
# area=1/2*base*height
# print(f'Area of triangle is {area}')

# side=float(input("Enter of square : "))
# area=side*side
# print(f'Area of square is {area}')

# year=int(input("Enter year : "))
# if (year%4==0 and year%100!= 0) or year%100==0 :
#     print(f'{year} is leap year')
# else:
#     print(f'{year} is not a leap year')

# s='python'
# for i in s:
#     print(i)

# l=[1,2,3,4,5]
# for i in l:
#     print(i+5)

# t=(1,2,3,'python')
# for i in t:
#     print(i)

# d={'x':10,'y':20,'z':30}
# for i in d:
#     print(i)

# d={'x':10,'y':20,'z':30}
# for i in d:
#     print(i,'=',d[i])

# s={1,2,3,4,'python'}
# for i in s:
#     print(i)



# s = set()

# n = int(input("Enter a number: "))
# s.add(n)
# n = int(input("Enter a number: "))
# s.add(n)
# n = int(input("Enter a number: "))
# s.add(n)
# n = int(input("Enter a number: "))
# s.add(n)
# n = int(input("Enter a number: "))
# s.add(n)

# print(s)

# s=input("Enter any string : ")
# s=s.replace(' ','')
# print(s)
# print(s.isalpha())

# s=input("Enter any string : ")
# s=s.replace(' ','')
# if s.isalpha() :
#     print("Alphabet")
# else :
#     print("not alpha")

#WAP TO COUNT NUMBER OF VOWELS AND CONSONANTS.
# s=input("Enter any string : ")
# s=s.replace(' ','')
# v=c=0
# if s.isalpha():
#     s=s.lower()
#     for i in s:
#         if i in ('a','e','i','o','u'):
#             v=v+1
#         else:
#             c=c+1
#     print('Vowel',v)
#     print('consonant',c)
# else:
#     print("Please enter correct string.")

#WAP TO PRINT N NATURAL NUMBERS.
# verTicaALLY
# n=int(input("Enter value : "))
# for i in range(1,n+1):
#     print(i)

#VERTICLLY
# n=int(input("Enter value : "))
# for i in range(1,n+1):
#     print(i,end=' ')

#sum of n natural numbers
# n=int(input("Enter value : "))
# for i in range(1,n+1):
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i)

# n=int(input("Enter value : "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end='=')
# print(sum)

#WAP TO PRINT N EVEN NUMBERS.
#horizontally
# n=int(input("Enter value : "))
# for i in range(1,n+1):
#     print(2*i)

#vertically
# n=int(input("Enter value : "))
# for i in range(1,n+1):
#     if i<n:
#        print(2*i,end=',')
#     else:
#         print(2*i)

#sum of even numbers
n=int(input("Enter value : "))
sum=0
for i in range(1,n+1):
    sum=sum+2*i
    if i<n:
       print(2*i,end='+')
    else:
        print(2*i,end='=')
print(sum)

#sum of n odd numbers
n=int(input("Enter value : "))
sum=0
for i in range(1,n+1):
    sum=sum+(2*i-1)
    if i<n:
       print((2*i-1),end='+')
    else:
        print((2*i-1),end='=')
print(sum)


# a=float(input("Enter side of triangle: " ))
# b=float(input("Enter side of triangle: " ))
# c=float(input("Enter side of triangle: " ))
# if(a ==b==c):
#     print("The triangle is equlateral traingle")
# elif(a==b or b==c or a==c):
#     print("The triangle is isosceles traingle")
# else:
#     print("The triangle is scalene traingle")

# h=float(input("Enter marks of Hindi : "))
# if 33<=h<=100:
#     e=float(input("Enter marks of English : "))
#     if 33<=e<=100:
#         m=float(input("Enter marks of maths : "))
#         if 33<=m<=100:
#             p=((h+e+m)/300)
#             if 40<=p<=100:
#                 print("Pass",p)
#             else:
#                 print("Fail",p)
#         else:
#             print("Fail in maths")
#     else:
#         print("Fail in English")
# else:
#     print("Fail in hindi")    

# un=input("Enter username : ")
# c=0
# for i in un:
#     c=c+1
# if c<10:
#     print("Valid username")
# else:
#   print("Invalid username")

n=int(input("enter value"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)  

n=int(input("enter value"))
sum=0
for i in range(1,n+1,2):
    sum=sum+i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)  



# n=int(input("enter value"))
# for i in range(1,n+1):
#     print("*")

