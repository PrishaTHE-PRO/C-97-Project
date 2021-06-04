import random
number=random.randint(1,9)
chances=0
print('guess a number between 1 and 9')
while chances<5:
    guess = int(input('enter your number'))

    if guess==number:
        print('congrats you won!')
    elif guess<number:
        print('guess a higher number',guess)
    else:
        print('guess a lower number', guess)

    chances=chances+1
if not chances<5:
    print('you loose :(')