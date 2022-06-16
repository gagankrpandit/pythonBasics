import random
c = 6
print('I am thinking of a number between 1 and 20, take a guess. You have 6 chances to guess right.')
secretNumber = random.randint(1, 20)
print(secretNumber)
for i in range(1, 7):
    print('take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('you guessed too low')
    elif guess > secretNumber:
        print('you guessed too high')
    elif guess == secretNumber:
        print(f'you guessed it right! in {i}th time')
        break
    
    print(c - i, 'chances left!')
    if (c - i) == 0:
        print('you couldn\'t guess it')
