# Class: Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc

# Object: Specific instance created from the template (class.). Eg. Form which contains the data for John Doe

class sai:
    company="HP"

    def get_salary(self):#self is important here because self is a way to refer the object of the class which is being created
        #we should have to write self compulsary in all the code when creating the class and objects
        return 18000

e1=sai()#we are creating the object here we can name it as we want 
#syntax= object name = class name ()
print(e1.get_salary()) #to print we have the syntax of object name.function()

e2=sai()
print(e2.get_salary())
print(e2.company)


# class sai:
#     age=19

#     def fun(self):
#         return 21
# e1=sai()
# print(e1.fun())
# print(e1.age)

# class employe:
#     company="Asus"

#     def get_info(self):
#         return 34000
# e1=employe()
# print(e1.get_info())
# print(e1.company)
