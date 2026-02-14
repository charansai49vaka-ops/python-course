class animal:
    def __init__(self,name):  #constructor
        self.name=name
    def speak(self):
        print("Generic sound")


class dog(animal):  # child class of animal
    def speak(self): #creating a function to print the sound of the dog
        print("Bark!")

class cat(animal):   #child class of animal
    def speak(self):
        print("Meow")

a1=animal("bankai")  #giving the name of the animal here 
a1.speak()  #prints the sound of the animal
a2=dog("husky")
a2.speak()
a3=cat("kitty")
a3.speak()


class animal:
    # def __init__(self):
        def sound(self):
            print("Generic sound")
class dog(animal):
    def sound(self):
        print("bark!")
class cat(animal):
    def sound(self):
        print("Meow")
e1=dog()
e1.sound()
e1=cat()
e1.sound()
a1=animal()
a1.sound()