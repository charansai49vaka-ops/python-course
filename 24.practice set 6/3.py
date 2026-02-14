class animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print("some sound")
class dog(animal):
    def speak(self):
        print("Bark!")

e1=dog("husky")
e1.speak()

a=animal("rakesh")
a.speak()