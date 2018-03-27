# p54, guessTheNumber.py, @20170108;

import random
secretNumber = random.randint(1,20)
print('I am thinking a number between 1 and 20.')

# The player can guesses 6 times;
for guessesTaken in range(1,7):
    print('Take a guess:')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

# Final words for the game;
if guess == secretNumber:
    print('Good job, You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, The number is ' + secretNumber)
