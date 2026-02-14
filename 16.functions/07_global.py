# we can able to create a global variable inside the function by declaring the name of the functin as global
def sum(a , b):
    c=a+b
    global x  #it is the global variable which was present inside the function
    x=10
    return c
print(sum(10, 8))
print(x)