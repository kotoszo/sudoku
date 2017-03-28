#                Sudoku by Tamás Richter and Ákos Nagy                 #
#                            CODECOOL 2017                             #
########################################################################


########################################################################
#                         IMPORTED AND MISC.                           #

from random import randint as rnd
from random import shuffle
from os import system
import time


class bcolors:
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

########################################################################
#                                 MAIN                                 #


wannaplay = True

while wannaplay:

    moves = []
    difficulty = welcomeScreen()
    z = [[False for _ in range(9)] for _ in range(9)]
    print(z)
    m = initBoard(makeStage())
    system('clear')

    while not playerHasWon(m):

        printGameState(m)
        print()
        getInput(m)

    system('clear')
    printGameState(m)
    print("\nCongratulations! You won!")
    stillWantsToPlay = input("Wanna play again? 'y' for yes, " +
                             "anything else to quit: ")
    if stillWantsToPlay.lower() != 'y':
        wannaplay = False
