# x=12 
# def f1(a ,b=x):
#     print((a,b))

# x=15
# f1(4)

# x=["abs","def"]
# a=lambda y:x+y
# y=["def","abs"]
# b=lambda y:x+y
# print(id(x) , id(y))

# def foo(x):
#     x=["def","abs"]
#     return id(x)


# q=["abs","def"]
# print(id(q)==foo(q))
a=["a","b","c"]
b=a.copy()
a.append("d")
print(a==b)

