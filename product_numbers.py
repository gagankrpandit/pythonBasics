# Python program to find the product of a set of real numbers
from itertools import product

num = input('enter some numbers separated with comma: ')
num = num.split(',')
product = 1

for i in range(len(num)):
    product = product * int(num[i])

print(f'Product of numbers is: {product}')
