# Sudoku by Tamás Richter and Ákos Nagy                 #
# CODECOOL 2017                             #
#


#
# IMPORTED AND MISC.                           #

from output_handler import *
from stage_handler import *
from status_handler import *
from os import system
from input_handler import *
import time

#
# MAIN                                 #

wannaplay = True
highlighted = [0, 0]
y = highlighted[0]
x = highlighted[1]

while wannaplay:

    moves = []
    difficulty = welcomeScreen()
    z = [[False for _ in range(9)] for _ in range(9)]
    m = initBoard(makeStage(), difficulty, z)
    system('clear')

    while not playerHasWon(m):

        m[highlighted[0]][highlighted[1]] = bcolors['YELLOW'] + \
            str(m[highlighted[0]][highlighted[1]]) + bcolors['ENDC']
        printGameState(m)
        print()
        highlighted = getInput(m, z, moves, highlighted)

    system('clear')
    printGameState(m)
    print("\nCongratulations! You won!")
    stillWantsToPlay = input("Wanna play again? 'y' for yes, " +
                             "anything else to quit: ")
    if stillWantsToPlay.lower() != 'y':
        wannaplay = False
