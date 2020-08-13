"""Rock, paper, scissors game with computer oponent.
"""
from random import randint

# get random choice to represent computer's play
choices = ['Rock', 'Paper', 'Scissors']
computer_choice = choices[randint(0,2)]

# get user choice
player_choice = input('Rock, Paper, or Scissors?  ')

# compare choices and determine win lose tie
if player_choice == computer_choice:
    print('{} = {}: tie.'.format(computer_choice, player_choice))
elif player_choice == 'Rock':
    if computer_choice == 'Paper':
        print('Paper covers Rock: you lose.')
    elif computer_choice == 'Scissors':
        print('Rock smashes Scissors: you win.')
elif player_choice == 'Scissors':
    if computer_choice == 'Paper':
        print('Scissors cut Paper: you win.')
    elif computer_choice == 'Rock':
        print('Rock smashes Scissors: you lose.')
elif player_choice == 'Paper':
    if computer_choice == 'Scissors':
        print('Scissors cut Paper: you lose.')
    elif computer_choice == 'Rock':
        print('Paper covers Rock: you win.')
else:
    # reprompt for choice if entry invalid
    print('Please choose Rock, Paper, or Scissors:  ')
