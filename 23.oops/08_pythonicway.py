class person:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    def age(self):
        return self._age
    def age(self,new_age):
        if new_age>=0 and new_age<=150:
            self._age=new_age
        else:
            print("Invalid age")
p = person("sai", 23)
print(p._age)          # Outputs: 23
p.age(34)              # Calls setter, validates, updates _age
print(p._age)          # Outputs: 34
p.age(-34)             # Prints: Invalid age (no change)
# print(p._age)          # Outputs: 34 (unchanged)

        