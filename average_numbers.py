# Python program to find out the average of a set of integers

num = input('enter some numbers separated with comma: ')
num = num.split(',')
sum = 0

for i in range(len(num)):
    sum = sum + int(num[i])
avg = sum/len(num)
print(f'Average of numbers is: {avg}')
