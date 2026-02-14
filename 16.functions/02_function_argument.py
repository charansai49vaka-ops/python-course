# in python there are three types of arguments 
# there are 1. Positional arguments
#           2. Default arguments
#           3. Keyword Arguments 

#       POSITIONAL ARGUMENTS
# in postional argument we should have to allote the value 
def add(a, b):
    x=a+b
    return x
print(add(5,3))  #here we are able to allote the values as we can able to see

#     DEFAULT ARGUMENTS
# in default argument we can able to allote the values using f-string in the def statement 
def self(name="sai charan"):
    print(f"My name is:{name}")
self()   #it will use to print the f-string
self("Bankai")

#   KEYWORD ARGUMENTS
# in keyword we can able to allote the values as we want like giving in a order we want

def add(a,b,c):
    x=(a+b+c)/3
    return x
o1=add(b=2,c=3,a=1)
o2=add(c=2,a=3,b=1)
o3=add(a=2,b=3,c=1) #here we can able to write the values as much as we want 
print(o1)
print(o2)
print(o3)


def na(a,b):
    s=(a+b)
    return s
print(na(10,8))

def suu(name1="virat"):
    print(f"my name is {name1}")
suu()
suu("Kholi")

def fah(a,b,c,d):
    scc=(a+b+c+d)
    return scc
o1=fah(a=3,c=4,b=2,d=4)
print(o1)