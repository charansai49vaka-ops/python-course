# there are two types of attributes in python . There are 
# 1. class attributes
# 2. instance attributes
# if we have same value in both instance and class attribute the python will automatically print the value present in the instance variable 
# like company in the below example
# if we want to print the value present in the class attribute we use the syntax 
# print(classname.value)

class employee:
    company="Asus"  #it is a class attributes where we can able to use it by using only class name in the print statement
    def __init__(self,company):  #this is a constructor  and we are adding a company to it   IT IS A INSTANCE ATTRIBUTES
        self.company=company # getting the company name from this statement

    def fun(self):
        return self.company # it prints the company name
    def get_info(self):
        print(f"he is working in the {self.company} company") # this is a f-string which is used to print the inside thing by using this as good
e1=employee("infinix") #greating a object as e1 and calling class from it and gibing the name of the company as infinix for __init__ constructor
print(e1.company) #prints== infinix
e1.get_info() #prints the content present in the f-string
print(employee.company) # using class we can able to print class attributes 


#object introspection
print(dir(e1))

class employee:
    company="asus" 

    def __init__(self, name, age, company, bond, joining_year):
        self.name=name
        self.age=age
        self.company=company
        self.bond=bond
        self.joining_year=joining_year
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_company(self):
        return self.company
    def get_bond(self):
        return self.bond
    def get_joining_year(self):
        return self.joining_year
e1=employee("sai charan",19,"Tesla",4,2026)
print(e1.get_name())        
print(e1.get_age())        
print(e1.get_company())        
print(e1.get_bond())        
print(e1.get_joining_year())        
print(employee.company) #to print something present in the class attribute we should have to print it by using class name.class attribute
        