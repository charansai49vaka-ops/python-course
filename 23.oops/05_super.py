# super function is used to call the parent class from child class 
# basically super class is written in the child class
# the syntax of super function is super().......
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("any sound")

class dog(animal):
    def speak(self):
        super().speak()
        print("Bark!")

e1=dog("husky")
e1.speak()  #here we only print dog class but we also see that the thind which is present in the animal class also print

class animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("generic sound")
class dog(animal):
    def sound(self):
        super().sound()
        print("Bark!")
e2=dog("Husky")
e2.sound()
        