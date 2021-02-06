'''
print('Enter \"Rock\", \"Paper\", or \"Scissors\".')

player_1_input = input('Player one: type your move:\n').lower()
player_2_input = input('Player two: type your move:\n').lower()

while player_1_input == player_2_input:
    print('Tie! Input next moves:')
    player_1_input = input('Player one: type your move:\n').lower()
    player_2_input = input('Player two: type your move:\n').lower()

if player_1_input == 'rock':
    if player_2_input == 'scissors':
        print('Rock beats scissors, congrats Player One!')
    elif player_2_input == 'paper':
        print('Paper beats rock, congrats Player Two!')
    else: 
        print('Something went wrong. Play again PLEASE')
elif player_1_input == 'scissors':
    if player_2_input == 'paper':
        print('Scissors beats paper, congrats Player One!')
    elif player_2_input == 'rock':
        print('Rock beats scissors, congrats Player Two!')
    else: 
        print('Something went wrong. Play again PLEASE')
elif player_1_input == 'paper':
    if player_2_input == 'rock':
        print('Paper beats rock, congrats Player One!')
    elif player_2_input == 'scissors':
        print('Scissors beats paper, congrats Player Two!')
    else: 
        print('Something went wrong. Play again PLEASE')
else:
    print('Something went wrong. Play again PLEASE')

print('Would you like to play again?')


'''

# --------------------------------------------------------

print('Enter \"Rock\", \"Paper\", or \"Scissors\".')

player_1_input = input('Player one: type your move:\n').lower()
player_2_input = input('Player two: type your move:\n').lower()

# Notes for later:
# Create a section that tests player_1_input against player_2_input
# Ideas:
#  - Maybe assign temporary variables with the values inputted 
#    by the users and then return a number 1, or 0 for the winner
#  - Need a function that compares Rock Paper and Scissors outside
#    of their relation to the users. Pass in the variables of the 
#    user input and output the winner. I know we haven't learned
#    functions yet, but maybe there's a way to accomplish that same
#    goal without functions........ FIGURE IT OUT