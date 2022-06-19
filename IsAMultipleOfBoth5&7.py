# Python program to check whether the given integer is a multiple of 5

while True:
    num = int(input('Enter number: '))
    if num % 5 == 0 and num % 7 == 0:
        print(f'{num} Is a multiple of both 5 and 7')
        break

    else:
        print('Is not a multiple of 5 and 7')
        continue
