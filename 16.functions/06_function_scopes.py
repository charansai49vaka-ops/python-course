'''in functions basically there is two types of variables .
there are local variables and global variables
Local variables are the variables which are written inside the function 
It can not be modified
global variables are the varibles which are written outside the function 
ones a global variable is written then there is no way the variable value is changes
'''
def sai(a, b):
    c=a+b
    return c  #this is a local variable
    print(c)
    
print(sai(10, 2))
c=18  # this is a global variable
print(c)

