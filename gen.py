# x=range(1,100)
# print(list(x))
# print(id(list(x)))

# def natural_no(n):
#     i=1
#     while i<=n:
#         yield i            #yield is used in the place of return in generator
#         i=i+1
# x=int(input("Enter a number : "))
# res=natural_no(x)
# print(res)

# for i in res:
#     print(i)
# print(next(res))
# print(next(res))
# print("Hello")
# print(next(res))

# for _ in range(5):
#     print(next(res))
# print("hello")
# for _ in range(10):
#     print(next(res))

# for _ in range(5):
#     print(next(res))
# for _ in range(10):
#     try:
#         print(next(res))
#     except StopIteration:
#         print("all elements are iterated ,i.e. collection is empty .")
#         break

# l=[1,2,3,4,5]
# print(l)
# x=iter(l)
# print(x)

l=[1,2,3,4,5,5,6,7,8,9,23,45] #iterable
print(l)
x=iter(l)     #iterator
print(x)
# for i in x:
#     print(i)
for i in range(12):
    print(next(x))
    