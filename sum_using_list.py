# Python program to display the sum of n numbers using a list

sum = []
num = int(input('how many numbers?: '))
d = 0

for i in range(num):
    n = input(f'Enter number {i+1}: ')
    n = int(n)
    d = d + n
sum.append(d)
print(f'The sum of the number in the list is: {sum[0]}')
