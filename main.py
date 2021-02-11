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
    print('Multiplayer mode! Enter \"Rock\", \"Paper\", or \"Scissors\".')
    restart = 'y'

    while restart == 'y':
        player_1_input = input('Player one: type your move:\n').lower()
        player_2_input = input('Player two: type your move:\n').lower()

        while player_1_input == player_2_input:
            if (player_1_input in comparisons) and (player_2_input in comparisons):
                print('Tie! Input next moves:')
            else:
                print("Invalid selection.")
            player_1_input = input('Player one: type your move:\n').lower()
            player_2_input = input('Player two: type your move:\n').lower()
            
        if (player_1_input in comparisons) and (player_2_input in comparisons):
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
    print('Singleplayer mode! Enter \"Rock\", \"Paper\", or \"Scissors\".')
    restart = 'y'

    options = ['rock', 'paper', 'scissors']
    while restart == 'y':
        player_1_input = input('Type your move:\n').lower()

        cpu_input = random.choice(options)

# Same code as above but with cpu titles, and slight other strings altered. 
# Find a way to reuse this code instead of copying it

# ------------------------------------------------------
        while player_1_input == cpu_input:
            if (player_1_input in comparisons) and (cpu_input in comparisons):
                print('You chose {}.'.format(player_1_input))
                print('Computer chose {}.'.format(cpu_input))
                print('Tie! Input next move!:')
            else:
                print("Invalid selection.")
            player_1_input = input('Type your move:\n').lower()
            cpu_input = random.choice(options)
            
        print('You chose {}.'.format(player_1_input))
        print('Computer chose {}.'.format(cpu_input))

        if (player_1_input in comparisons) and (cpu_input in comparisons):
            if cpu_input == comparisons[player_1_input]:
                print('{} beats {}, player 1 wins!'.format(player_1_input, cpu_input))
            elif player_1_input == comparisons[cpu_input]:
                print('{} beats {}, computer wins!'.format(cpu_input, player_1_input))
        else:
            print("Invalid selection.")

        restart = input('Type "y" to play again.\n')
    print("Thanks for playing!")
# ------------------------------------------------------