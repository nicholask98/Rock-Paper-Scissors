import random

comparisons = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

# vvvv Multi vs Single prompt vvvv
multiplayer = True
game_type = input('For single-player type: "s"\nFor multiplayer type: "m"\n')

while (game_type != 's') and (game_type != 'm'):
    game_type = input('For single-player type: "s"\nFor multiplayer type: "m"\n')
if game_type == 'm':
    multiplayer = True
elif game_type == 's':
    multiplayer = False

# vvvv For Multiplayer Games vvvv

if multiplayer == True:
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

# vvvv For Singleplayer Games vvvv

elif multiplayer == False:
    print('Single player')


'''
Next to-do:

Create a bot using random module for a single player to play against.
Prompt the user at the beginning if they want to play a single player
or multiplayer game. wrap around if elif 

'''