class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def get_info(self):
        print(f"my name is {self.name} and i am {self.age} old")
e1=person("sai charan", 19)
e1.get_info()
        