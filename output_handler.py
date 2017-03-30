from os import system
import time
import curses
import getch

bcolors = {
    'UNDERLINE': '\033[4m',
    'ENDC': '\033[0m',
    'YELLOW': '\033[93m',
    "BLACK": '\033[30m'
}


def printGameState(m):
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


def welcomeScreen():
    system('clear')
    print("Welcome to Sudoku!")
    time.sleep(1)
    print("Please choose a difficulty level from 1-10: ")
    difficulty = getch.getch()

    while int(difficulty) not in range(1, 11):
        print("Invalid input!")
        difficulty = input("Please choose a difficulty (1-10): ")

    return int(difficulty)
