# Python program to implement linear search

list = [5, 6, 8, 3, 9]
print(f'Given list is: {list}')


while True: 
    num = int(input('Which number you want to search from the list?: '))
    if num in list:
        break
    else:
        print('The number given by you is not in the list.')
        print('Please type any one number from the list given')

for i in range(len(list)):
    if list[i] == num:
        print(f'{num} is present at the {list.index(num)} index.')
        break
else:
    print(f'{num} is not present in the list')

