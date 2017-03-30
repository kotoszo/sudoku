# Sudoku by Tamás Richter and Ákos Nagy                 #
# CODECOOL 2017                             #
#

# IMPORTS                           #
from output_handler import *
from stage_handler import *
from status_handler import *
from input_handler import *
from os import system
import getch
import vlc


# Start                               #
def main():
    wannaplay = True
    highlighted = [0, 0]
    # As long as you want to play
    while wannaplay:

        moves = []
        difficulty = welcome_screen()
        # List for the numbers what we took out.
        z = [[False for _ in range(9)] for _ in range(9)]
        m = init_board(makeStage(), difficulty, z)
        system('clear')

        while not player_has_won(m):

            # The belonging number for the givin coordinates, gonna be colored.
            # That means, the exact same number gonna be colored, where the player "stands"
            m[highlighted[0]][highlighted[1]] = bcolors['YELLOW'] + \
                str(m[highlighted[0]][highlighted[1]]) + bcolors['ENDC']

            print_game_state(m)
            highlighted = get_input(m, z, moves, highlighted)

        system('clear')
        print_game_state(m)
        print("\nCongratulations! You won!")
        vlc.MediaPlayer("yeah.wav").play()

        print("Wanna play again? 'y' for yes, anything else to quit.")
        still_wants_to_play = getch.getch()
        if still_wants_to_play.lower() != 'y':
            wannaplay = False


if __name__ == '__main__':
    main()
