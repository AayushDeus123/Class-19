#Rock, Paper, Scissor with computer
import random

while True: 
    opt = ('Rock','Paper','Scissor')
    user = input('\nChoose:\nRock\nPaper\nScissor\n')
    comp = random.choice(opt)
    
    print('\nYou have chosen' ,user, 'and computer has chosen' ,comp)
    if comp == user:
        print('\nSo the game is a draw')
    elif comp == 'Rock' and user == 'Paper':
        print('\nSo you Win!')
    elif comp == 'Rock' and user == 'Scissor' 
        print('So you Lose!')
    elif comp == 'Paper' and user == 'Scissor':
        print('\nSo you Win!')
    elif comp == 'Paper' and user == 'Rock':
        print('S you Lose!')
    elif comp == 'Scissor' and user == 'Rock':
        print('So you Win')
    elif comp == 'Scissor' and user == 'Paper':
        print('So you Lose!')
    else:
        print('Choose:\nRock\nPaper\nScissor\n')