# list comprehensions are used to decrease the size of code instead of writting of large for loops

# print starting 5 multiplication table
'''table=[]
for i in range(1, 11):
    table.append(5*i)
print(table)''' #instead of writting this code we can able to write this 
table=[5*i for i in range (1, 11)]
print(table)# it will minimize the code in the for loop without doing any additional work
#but if we want to add any thing in for loop again it will becomes difficult

cas=[2*j for j in range(1, 11)]
print(cas)