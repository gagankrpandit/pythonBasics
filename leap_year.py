# Python program to check leap year

year = int(input('Enter year: '))

while year % 100 == 0:
    if year % 400 == 0:
        print('leap year')
        break
    else:
        print('not a leap year')
        break

while year % 100 != 0:
    if year % 4 == 0:
        print('leap year')
        break
    else:
        print('not a leap year')
        break
