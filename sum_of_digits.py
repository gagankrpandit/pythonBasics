# Python program to find the sum of the digits of an integer using while loop

int = int(input('Enter a positive integer: '))

if int < 0:
    print('You provided a negative integer!')
    int = int(input('Enter a positive integer: '))
else:
    pass

digit1 = 0
while int > 0: 
    digit = int % 10 
    digit1 = digit1 + digit
    int = int // 10 
print(f'The sum of numbers given in input is: {digit1}')
    
