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

hin=float(input("Enter marks of Hindi : "))
if 0<=hin<100 :
    eng=float(input("Enter marks of English : "))
    if 0<=eng<100 :
        ms=float(input("Enter marks of Maths : "))
        if 0<=ms<100 :
            msc=float(input("Enter marks of Moral Science : "))
            if 0<=msc<100 :
                avg=(hin+eng+ms+msc)/4
                print(avg)
                if 0<=avg<35 :
                    print("Fail")
                elif 35<=avg<45 :
                    print("3rd Division")
                elif 45<=avg<60 :
                    print("2nd Division")
                else :
                    print("1st Division")
            else :
                print("You have entered an invalid marks.")
        else :
            print("You have entered an invalid marks.") 
    else:
        print("You have entered an invalid marks.")
else:
    print("You have entered an invalid marks.")