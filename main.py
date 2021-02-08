comparisons = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

print('Enter \"Rock\", \"Paper\", or \"Scissors\".')
restart = 'y'

while restart == 'y':
    player_1_input = input('Player one: type your move:\n').lower()
    player_2_input = input('Player two: type your move:\n').lower()

    while player_1_input == player_2_input:
        print('Tie! Input next moves:')
        player_1_input = input('Player one: type your move:\n').lower()
        player_2_input = input('Player two: type your move:\n').lower()
        
    if player_1_input and player_2_input in comparisons:
        if player_2_input == comparisons[player_1_input]:
            print('{} beats {}, player 1 wins!'.format(player_1_input, player_2_input))
        elif player_1_input == comparisons[player_2_input]:
            print('{} beats {}, player 2 wins!'.format(player_2_input, player_1_input))
    else:
        print("Invalid selection.")
    restart = input('Type "y" to play again.\n')

print("Thanks for playing!")