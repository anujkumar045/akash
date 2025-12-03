#MAP()
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# l3=[3,2,4,1]
# def add(x,y,z):
#     return x+y+z
# res=map(add,l1,l2,l3)
# print(res)
# print(tuple(res))

# l1=[1,2,3,4,5]
# l2=[5,6,7,8]
# l3=[3,2,4]
# def add(x,y,z):
#     return x+y+z
# res=map(add,l1,l2,l3)
# print(res)
# print(tuple(res))

#SQUARE USING MAP()
# l1=[1,2,3,4]
# def square(n):
#     return n**2
# res=map(square,l1)
# print(tuple(res))

#SUAREROOT USING MAP()
# l1=[1,2,3,4]
# def squarert(n):
#     return n**0.5
# res=map(squarert,l1)
# print(tuple(res))

#FILTER()
# l=[1,2,3,4,5]
# def greater3(n):
#     if n>=3:
#         return n
# res=filter(greater3,l)
# print(list(res))

'''even'''
l=[1,2,3,4,5]
def greater3(n):
    if n%2==0:
        return n
res=filter(greater3,l)
print(list(res))

'''odd''                                                                                                                                                                                                                                          '''
l=[1,2,3,4,5]
def greater3(n):
    if n%2!=0:
        return n    
res=filter(greater3,l)
print(list(res))
