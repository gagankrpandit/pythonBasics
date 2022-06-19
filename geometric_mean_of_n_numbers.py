# Python program to find the geometric mean of n numbers

import random
from time import gmtime

loopRange = int(input('For how many numbers you want Geometric Mean? '))

list = []
i = 0
while i < loopRange:
    num = random.randint(2, 9)
    list.append(num)
    i = i + 1
print(list)

prdct = 1
for i in range(loopRange):
    prdct = prdct * list[i]
print(prdct)

power = 1/loopRange
GM = pow(prdct, power)

print(f'The Geometric Mean is: {GM}')
