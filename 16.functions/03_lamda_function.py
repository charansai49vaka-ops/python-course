# lamda functions in python is used to decrease the size of the code 
# it helps developer to decrease the size of the code and helps to decrease the size as well

square=lambda x:x*x  #lambda is a python keyword

print(square(4))

'''it is as good as
def square(x):
    return x*x
'''
sum=lambda a, b:a+b
print(sum(2, 16))
'''
it is as good as
def sum(a, b):
    return a+b
'''
minus=lambda a,b:a-b
print(minus(20, 18))


name=lambda x:x*x
print(name(10))


sum=lambda a,b:a+b
print(sum(10,18))

minus=lambda a,b:a-b
print(minus(10,5))

multi=lambda a,b:a*b
print(multi(10,2))

div=lambda a,b:a/b
print(div(10, 5))