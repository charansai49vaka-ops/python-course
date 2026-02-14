class point:
    def __init__(self, x , y):
        self.x=x
        self.y=y
    # def printpointer(self, p):
    def printpointer(self):
        print(f"x is {self.x} and y is {self.y}")
    def __sub__(self, p):
        return point((self.x-p.x), (self.y-p.y))
    

p1=point(4,2)
p2=point(4,5)
p=p1-p2
p.printpointer()

# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def printpointer(self):  # Fixed indentation
#         print(f"x is {self.x} and y is {self.y}")
    
#     def __add__(self, p):  # Add this method for + button!
#         return point(self.x + p.x, self.y + p.y)  # Returns new Point!
    
#     def __sub__(self, p):
#         return point(self.x - p.x, self.y - p.y)

# p1 = point(4,2)  # Real objects!
# p2 = point(4,5)
# p = p1 - p2     # Works now!
# p.printpointer()  # Prints: x is 8 and y is 7

        