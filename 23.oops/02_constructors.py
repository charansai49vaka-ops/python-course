# constructor is used to allote the somany number of information in a single line without nedded of returning values somany number of times
# basically we write constructor using __init__ function 

class employee:

    def __init__(self,salary,age,company,bond,name):#it is the constructor we created it using __init__
        self.salary=salary
        self.age=age
        self.company=company
        self.bond=bond
        self.name=name
    def fun(self):
        return self.name#it is used to print only the name of the employee


    def get_info(self):
        # return self.salary
        # return self.age
        # return self.company
        # return self.bond
        # return self.name
        print(f"the name of the emplayee is {self.name}.His age is {self.age}.he work in the company of {self.company},with a salary of {self.salary},along with a bond of years{self.bond}")
    
e1=employee(34000,19,"hp",5,"sai charan") #giving the values in a single line without even need of repeating return again and again
e1.get_info() #used to print f-string
e1.fun()
print(e1.fun())#print name using the function fun 

