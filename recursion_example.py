# Python program to print the numbers from a given number n till 0 using recursion

def rec(n):
    if n < 0:
        pass
    else:
        print(n)
        rec(n-1)

rec(6)
