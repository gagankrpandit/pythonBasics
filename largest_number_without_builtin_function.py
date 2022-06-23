# Python program to find the largest number in a list without using built-in functions

list_ = [34, 54, 67, 43, 132, 88, 65, 89, 97, 342]

big = list_[0]
for i in range(len(list_)):
    if list_[i] > big:
        big = list_[i]
    else:
        list_[i] = big
print(f'largest number is {list_[i]}')

