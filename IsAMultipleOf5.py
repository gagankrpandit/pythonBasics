# Python program to check whether the given integer is a multiple of 5

while True:
    num = int(input('Enter number: '))
    if num % 5 == 0:
        print('Is a multiple of 5')
        break
    else:
        print('Is not a multiple of 5')
        continue
