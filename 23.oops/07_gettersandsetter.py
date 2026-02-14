# these are used to create to control how attributes of your class are accessed and modified
# we can able to access and use it as we want

class person:
    def __init__(self,name,age):
        self.name=name
        self._age=age  #convention:_age indicates it's intend
    def get_age(self): #getter for age
        return self._age
    def set_age(self, new_age): #Setter for age
        if new_age>=0 and new_age <=150:#validation
            self._age=new_age
        else:
            print("Invalid age")
p=person("sai",19)
print(p.get_age())
p.set_age(10)
print(p.get_age())
p.set_age(190)
# print(p.get_age())

        