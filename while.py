# # NO. OF DIGITS
# n=int(input("Enter number : "))
# td=0
# while n>0: 
#     td=td+1
#     n=n//10
# print('total digit = ',td)

# # ARMSTRONG NUMBER
# n=int(input("Enter number : "))
# m=p=n
# td=sum=0
# while n>0:
#   td=td+1
#   n=n//1
# while m>0:
#   ld=m%10
#   sum=sum+ld**td
#   m=m//10
# if p==sum:
#   print(f'given number {p} is armstrong')
# else:
#   print(f'given number {p} is not armstrong')

# n = 129382342434234
# print(len(str(n)))

# # PALLINDROME
# s=input("Enter any value : ")
# if s==s[::-1] :
#     print(f'given value {s} is pallndrome')
# else:
#     print("Not pallindrome")

# # FACTOR
# n=int(input("Enter any value : "))
# l=[]
# for i in range(2,n):
#     if n%i==0:
#         l.append(i)
# print(l)

# n=int(input("Enter any value : "))
# i,l=2,[]
# while i<n:
#     if n%i==0:
#         l.append(i)
#     i+=1
# print(f'factor of given number{n} is {l}')

# n=int(input("Enter value : "))
# i=1
# while i<=n:
#     if i==5:
#         print(i)
#         continue
#     else:
#         print(i)
#     i=i+1

while(True):
    print("1.Add\n 2.Sub\n 3.Div\n 4.Multi\n 5.exit")
    n=int(input("Enter a number "))
    if n in (1,2,3,4,5):
       if n in (1,2,3,4):  
        if n==1:
           numbers=int(input("How many values you want to input "))
           l=[]
           for i in range(1,numbers+1):
              value=int(input(f'enter {i} number'))
              l.append(value)
           sum=0
           for i in l:
              sum=sum+i
           print(f'Addition of {l} is {sum}')
              
    else:
        break
else:
    print("Please enter valid choice")