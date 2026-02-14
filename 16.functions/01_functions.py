# functions are the most important operations in python
# basically functions are used to to take the input and produce output 
# Functions are reusable which is help the programmer to decrease the size iof the code as mucn as we want
# we write functions using def in the starting line of the code
# in function there is return which helps the user to allote a particular data as much we want

def hero(a, b, c):
    s=(a+b+c)/3   #average of three numbers
    print(s)     #it will not at all print because we didn't allote the values which are used to print like a,b,c
hero(3,4,5)  #it will helps the code to take the values for a,b,c 
hero(5,6,7) 
#here hero is the name of the function we can able to keep any thing as the function name


'''code2:'''
def num(a,b,c,d):
    c=(a+b+c+d)/4
    return c
o1=num(3,4,5,6)
o2=num(7,8,9,10)
print(o1)   #return helps when we want to allote a particular value as we want to another  like giving o1 and o2
print(o2)


def sum(a,b):
    a=(a+b)/2
    print(a) 
sum(1,2)

def name(a,b,c,d):
    sc=(a+b+c+d)/4
    return sc
re=name(3,4,5,6)
print(re)