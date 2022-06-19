# Python program to find the average of 10 numbers using while loop

import random

num = []
i = 0
while i < 10:
    rand = random.randint(456, 876)
    num.append(rand)
    i = i + 1
print(f'The 10 numbers are: {num}')

sum = 0
for i in range(len(num)):
    sum = sum + num[i]
average = sum/len(num)
print(f'The average of 10 numbers is {average}')
