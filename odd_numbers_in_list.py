# Python program to find the odd numbers in an array

num = [33, 45, 48, 74, 57, 88]
newList = []

for i in range(len(num)):
    if num[i] % 2 == 0:
        pass
    else:
        newList.append(num[i])
print(f'Odd numbers in the list are: {newList}')
