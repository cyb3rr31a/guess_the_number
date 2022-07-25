# Guess the Number Game
import random

guesses = 0

print('Hello. What is your name?')
name = input()

num = random.randint(1, 20)
print('Well ' + name + ', I am thinking of a number between 1 and 20.')

for guesses in range(6):
    print('Take a guess.')
    guess = int(input())

    if guess > num:
        print('Too high.')
    elif guess < num:
        print('Too low.')
    else:
        break

    if guess == num:
        guesses = str(guesses + 1)
        print('Good job,' + name + '! You guessed my number in ' + guesses + ' guesses!')
    else:
        num = str(num)
        print('Nope. The number I was thinking of was ' + num + '.')
