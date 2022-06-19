# Python program to find the sum of the digits of an integer using while loop

while True:
    num = input('Enter a positive integer: ')
    num = int(num)
    if num < 0:
        print('You provided a negative integer!')
    else:
        digit1 = 0
        while num > 0:
            digit = num % 10
            digit1 = digit1 + digit
            num = num // 10
        print(f'The sum of numbers given in input is: {digit1}')
        break
