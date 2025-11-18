# NO. OF DIGITS
n=int(input("Enter number : "))
td=0
while n>0: 
    td=td+1
    n=n//10
print('total digit = ',td)

# ARMSTRONG NUMBER
n=int(input("Enter number : "))
m=p=n
td=sum=0
while n>0:
  td=td+1
  n=n//1
while m>0:
  ld=m%10
  sum=sum+ld**td
  m=m//10
if p==sum:
  print(f'given number {p} is armstrong')
else:
  print(f'given number {p} is not armstrong')

n = 129382342434234
print(len(str(n)))

# PALLINDROME
s=input("Enter any value : ")
if s==s[::-1] :
    print(f'given value {s} is pallndrome')
else:
    print("Not pallindrome")

# FACTOR
n=int(input("Enter any value : "))
l=[]
for i in range(2,n):
    if n%i==0:
        l.append(i)
print(l)

n=int(input("Enter any value : "))
i,l=2,[]
while i<n:
    if n%i==0:
        l.append(i)
    i+=1
print(f'factor of given number{n} is {l}')