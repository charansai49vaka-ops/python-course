# operator overloading is used to give extra meaning to the exists operator without changing it's previous meaning

class number:  #creating a class here with class name as number 
    def __init__(self,a,b):  #here we are now creating a constructor using __init__ and add two a,b parameters 
        self.a=a
        self.b=b
    def __add__(self,other):  #Here we are creating a new function named __add__ 
        a=self.a+other.a  #here we are adding 1,2
        b=self.b+other.b #here we are adding 3,4
        res=number(a,b) #creating a object using the syntax objectname=classname (parameters)
        return res #returning the object
    def __str__(self): #here creating a function named __str__ becaused we have to print the values in (a,b) formate
        return f"({self.a}, {self.b})"  #this is a f-string 
n1=number(1,3) #this is a self
n2=number(2,4) #this is a other 
n3=n1+n2 #adding n1+n2
print(n3)
        
class number:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __sub__(self,other):
        a=self.a-other.a
        b=self.b-other.b
        res=number(a,b)
        return res
    def __str__(self):
        return f"({self.a},{self.b})"
n1=number(4,5)
n2=number(1,3)
n3=n1-n2
print(n3)