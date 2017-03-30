from os import system
import time
import getch

bcolors = {
    'UNDERLINE': '\033[4m',
    'ENDC': '\033[0m',
    'YELLOW': '\033[93m',
    "BLACK": '\033[30m'
}


def print_game_state(m):
    '''Prints the board with grids and stuff.'''

    system('clear')
    j = 0
    for a in m:
        i = 0
        if j % 3 == 2 and j != 8:
            for x in a:
                print(bcolors['UNDERLINE'] + str(x) + bcolors['ENDC'], end=' ')
                if i % 3 == 2 and i != 8:
                    print(bcolors['UNDERLINE'] + '|' + bcolors['ENDC'], end=' ')
                i += 1
        else:
            for x in a:
                print(str(x), end=' ')
                if i % 3 == 2 and i != 8:
                    print('|', end=' ')
                i += 1
        j += 1
        print()


def welcome_screen():
    '''Initial welcome message and difficulty input request.'''

    system('clear')
    print("Welcome to Sudoku!")
    time.sleep(1)

    difficulty = 0
    while difficulty not in range(1, 10):
        try:
            print("Please choose a difficulty level from 1-9")
            difficulty = int(getch.getch())
        except:
            print("Invalid input.")
    return difficulty
