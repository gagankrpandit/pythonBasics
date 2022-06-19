# Python program to display all the multiples of 3 within the range 10 to 50

num = 3
aList = []
for i in range(10, 51):
    if i % num == 0:
        aList.append(i)
    else:
        pass
print(f'Multiples of {num} are:\n{aList}')
