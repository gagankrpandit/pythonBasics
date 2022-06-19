# Python program to display the given integer in reverse manner

i = int(input('Enter number: '))
rev = 0

while i > 0:
    rev = (rev * 10) + (i % 10)
    i = i // 10
print(f'The reverse is {rev}')
