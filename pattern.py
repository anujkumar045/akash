# n=5
# for i in range(1,6):
#     print("*"*5)

# n=int(input("enter value"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)


# n=int(input("enter value"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

# n=int(input("enter value"))
# for i in range(1,n+1):
#     print("* "*i)

# n=int(input("enter value"))
# for i in range(n):
#     print(" "*i+"*"*(n-i))
    
# n=int(input("enter value"))
# for i in range(n):
#     print(" "*i+"* "*(n-i))

# n=int(input("enter value"))
# for i in range(n):
#     print("*"*(n-i))
    
# n=int(input("enter value"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*i)
    
# n=int(input("enter value"))
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+"*"*i)
    
# n=int(input("enter value"))
# for i in range(1,n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i)
    
# n=int(input("Enter any number : "))
# for i in range(n):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()

# n=int(input("Enter any number : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# even number right angled triangle 
# n=int(input("Enter any number : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(2*j,end=' ')
#     print()

# odd number right angled triangle 
# n=int(input("Enter any number : "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(2*j-1,end=' ')
#     print()

#for order of alphabet
# x='A'
# print(ord(x))
# print(ord(x)+1)
# print(chr(ord(x)+1))

# alphabet in vertical way
# n=int(input("Enter value : "))
# ch=input("Enter starting character : ")
# for i in range(n):
#     print(ch)
#     ch=chr(ord(ch)+1)

# alphabet square
# n=int(input("Enter value : "))
# for i in range(n):
#     ch='A'
#     for j in range(n):
#       print(ch,end=' ')
#       ch=chr(ord(ch)+1)
#     print()

# alphabet square
# n=5
# i=1
# while i<=n:
#     ch='A'
#     j=1
#     while j<=n:
#         print(ch,end=' ')
#         ch=chr(ord(ch)+1)
#         j=j+1
#     print()
#     i=i+1

#  natural number square
# n=int(input("Enter value : "))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(j,end=' ')
#         j=j+1
#     i=i+1
#     print()
#     # i=i+1

# n=int(input("Enter value :"))
# for _ in range(1,n+1):
#     for i in range(1,n+1):
#         print(i,end=' ')
#     print()

#natiural number right angled triangle
# n=int(input("Enter value :"))
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(i,end=' ')
#     print()

#even number right angled triangle
# n=int(input("Enter value :"))
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(2*i,end=' ')
#     print()

#odd number right angled triangle
# n=int(input("Enter value :"))
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(2*i-1,end=' ')
#     print()

#floyd triangle
# n=int(input("Enter value :"))
# y=1
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(y,end=' ')
#         y=y+1
#     print()


# n=int(input("Enter value: "))
# for i in range(1,n):
#     for j in range(1,i+1):
#         if j==1:
#             print(" "*(n-i),j)
#         else:
#             print(" ",j,end="")
#     print()


# n=int(input("Enter value : "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#     print()
#     j=j+1
# i=i+1