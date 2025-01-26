#Random Number Generator number game 
import random
play = True
print('I will generate random number between 10 to 20')
print('As soon as you guess it, the game ends')
rand = str(random.randint(10 , 20))

while play:
    guess = (input('Guess your number : '))
    if guess == rand:
        print('\nYou have guessed correctly!')
        break
    else:
        print('\nYou have guessed incorrectly, try again')
        