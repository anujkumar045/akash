n=5
for i in range(1,6):
    print("*"*5)

n=int(input("enter value"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

        *

n=int(input("enter value"))
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

n=int(input("enter value"))
# for i in range(1,n+1):
#     print("* "*i)

n=int(input("enter value"))
for i in range(n):
    print(" "*i+"*"*(n-i))
    
n=int(input("enter value"))
for i in range(n):
    print(" "*i+"* "*(n-i))

n=int(input("enter value"))
for i in range(n):
    print("*"*(n-i))
    
n=int(input("enter value"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)
    
n=int(input("enter value"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)
    
n=int(input("enter value"))
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)
    
n=int(input("Enter any number : "))
for i in range(n):
    for j in range(1,n+1):
        print(j,end=' ')
    print()

n=int(input("Enter any number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

n=int(input("Enter any number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j,end=' ')
    print()

n=int(input("Enter any number : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end=' ')
    print()

x='A'
print(ord(x))
print(ord(x)+1)
print(chr(ord(x)+1))

n=int(input("Enter value : "))
ch=input("Enter starting character : ")
for i in range(n):
    print(ch)
    ch=chr(ord(ch)+1)

n=int(input("Enter value : "))
for i in range(n):
    ch='A'
    for j in range(n):
      print(ch,end=' ')
      ch=chr(ord(ch)+1)
    print()