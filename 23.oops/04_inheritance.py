# inheritance is the one of the most important function present in the pyhton programming 
# inheritance is defined as the creating a child node from parent node where all the funtion present in the parent class will get to the child class 
# it helps not to write a same code again and again
# class animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print("Generic animal sound")
# class dog(animal):
#     def speak(self):
#         print("Bark!")


# e1=dog("husky")
# print(e1.name)
# e1.speak()
# a1=animal("puppy")
# a1.speak()



class animal:
    def __init__(self, name):
        self.name=name
    def sound(self):
        print("genenric sound")

class dog(animal):
    def sound(self):
        print("Bark!")
e1=dog("Husky")
print(e1.name)
e1.sound()
a1=animal("john")
print(a1.name)
a1.sound()


    
        
