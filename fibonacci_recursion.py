# Python program to find the Nth term in a Fibonacci series using recursion

def fibonacci(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fibonacci(x-1)
print(fibonacci(4))
