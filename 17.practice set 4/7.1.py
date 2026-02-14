

def fibonacci(n):
    '''print the first n number of fibonacci numbers'''
    def fib(k):
        if k<=1:
            return 1
        return fib(k-2)+fib(k-1)
    for i in range(n):
        print(fib(i), end=" ")
fibonacci(8)
print(fibonacci.__doc__)
