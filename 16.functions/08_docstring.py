# in python if we write something in triple quotes there are declared as the comments but if we write the same things in the starting of the functions then we can able to saw there are known as docstring
# comments are not visible in the excecution of the program but docstring are made to visible in the output 
def name(a, b):
    '''my name is sai charan i am from ongole i have completed'''
    c=a+b
    return c
print(name.__doc__) #here the output will be my name is sai charan i am from ongole i have completed



def sum(a,b):
    '''aot is one of the goated anime of all time because the story runs around a person name eren yeager who sacrifies himself to save the human kind with out expecting anything in return and finally acheieves it with the cost of his life'''
    c=(a+b)
    return c
print(sum.__doc__)