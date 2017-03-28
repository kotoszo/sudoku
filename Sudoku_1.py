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
#                               FUNCTIONS                              #


def columnIsClean(col):
    # Beadsz neki egy oszlopot listaként ~>
    # az oszlopban van-e ismétlés, és 1-9ig benne van-e minden szám

    clean = True

    if len(col) != len(set(col)):
        clean = False

    for i in range(1, 10):
        if i not in col:
            clean = False

    return clean


def rowIsClean(r):
    # Ugyanaz mint a fentebbi, csak sort vizsgál oszlop helyett
    clean = True

    if len(r) != len(set(r)):
        clean = False

    for i in range(1, 10):
        if i not in r:
            clean = False

    return clean


def subMatrixesAreClean(matrix):
    # Ugyanaz mint a fentebbi csak kis 3x3as szutykokra
    clean = True

    for y in range(0, 7, 3):
        for x in range(0, 7, 3):

            subMatrix = []
            for j in range(3):
                for i in range(3):
                    subMatrix.append(matrix[y + j][x + i])

            if len(subMatrix) != len(set(subMatrix)):
                clean = False

            for i in range(1, 10):
                if i not in subMatrix:
                    clean = False

    return clean


def playerHasWon(matrix):

    won = True

    for i in range(9):
        column = []
        for x in matrix:
            column.append(x[i])
        row = matrix[i]

        if not (rowIsClean(row) and columnIsClean(column)):
            won = False

    if not subMatrixesAreClean(matrix):
        won = False

    return won


def moveIsValid(m, m_y, m_x, number):

    r = m[m_y][:]
    c = [x[m_x] for x in m]

    c = [x for x in c if x != ' ']
    r = [x for x in m[m_y] if x != ' ']

    if not (number in c or number in r):

        m_y -= m_y % 3
        m_x -= m_x % 3

        subMatrix = []
        for j in range(3):
            for i in range(3):
                subMatrix.append(m[m_y + j][m_x + i])

        if number in subMatrix:
            print('Invalid move!')
            time.sleep(2)
            return False
        else:
            return True
    else:
        print('Invalid move!')
        time.sleep(2)
        return False


def printGameState(m):
    system('clear')
    j = 0
    for a in m:
        i = 0
        if j % 3 == 2 and j != 8:
            for x in a:
                print(bcolors.UNDERLINE + str(x) + bcolors.ENDC, end=' ')
                if i % 3 == 2 and i != 8:
                    print(bcolors.UNDERLINE + '|' + bcolors.ENDC, end=' ')
                i += 1
        else:
            for x in a:
                print(str(x), end=' ')
                if i % 3 == 2 and i != 8:
                    print('|', end=' ')
                i += 1
        j += 1
        print()


def getInput(matrix):
    s = input("[row] [column] [number] OR 'back' to undo OR 'quit': ").split(' ')
    print()
    if s[0].lower() == 'back' and len(s) == 1:
        takeBackLastMove()
    elif s[0].lower() == 'quit' and len(s) == 1:
        exit()
    else:
        try:
            if len(s) < 3:
                raise ValueError
            else:
                y = int(s[0])-1
                x = int(s[1])-1
            if (x in range(0, 9) and y in range(0, 9)):
                Number = int(s[2])
                if Number > 0 and Number < 10:
                    if z[y][x]:
                        if moveIsValid(m, y, x, Number):
                            moves.append([y, x, m[y][x]])
                            m[y][x] = Number
                    else:
                        raise TypeError
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("Invalid input!")
            time.sleep(2)
        except TypeError:
            print("You can't rewrite that field!")
            time.sleep(2)


def makeStage():
    l = [x for x in range(1, 10)]
    m = [[None for _ in range(9)] for _ in range(9)]
    shuffle(l)
    y, x = 0, 0
    k = 0
    for i in range(3):
        for i in range(3):
            m[y][x] = l[k]
            x += 1
            k += 1
        x = 0
        y += 1
    # idaáig
    x = 0
    y = 0
    for i in range(1):
        for i in range(3):
            m[0+y][3+x] = m[1+y][0+x]
            x += 1
        y += 0
        x = 0
        for i in range(3):
            m[1+y][3+x] = m[2+y][0+x]
            x += 1
        y, x = 0, 0
        for i in range(3):
            m[2+y][3+x] = m[0+y][0+x]
            x += 1
    x = 3
    y = 0
    for i in range(1):
        for i in range(3):
            m[0+y][3+x] = m[1+y][0+x]
            x += 1
        y = 0
        x = 3
        for i in range(3):
            m[1+y][3+x] = m[2+y][0+x]
            x += 1
        y, x = 0, 3
        for i in range(3):
            m[2+y][3+x] = m[0+y][0+x]
            x += 1

    y = 0
    x = 0
    # középső oszlopok
    for i in range(3):
        for i in range(3):
            m[3+y][2+x] = m[0+y][0+x]
            y += 1
        y -= 3
        for i in range(3):
            m[3+y][0+x] = m[0+y][1+x]
            y += 1
        y -= 3
        for i in range(3):
            m[3+y][1+x] = m[0+y][2+x]
            y += 1
        y -= 3
        x += 3
    x = 0
    y = 3
    # lsó oszlopok
    for i in range(3):
        for i in range(3):
            m[3+y][2+x] = m[0+y][0+x]
            y += 1
        y -= 3
        for i in range(3):
            m[3+y][0+x] = m[0+y][1+x]
            y += 1
        y -= 3
        for i in range(3):
            m[3+y][1+x] = m[0+y][2+x]
            y += 1
        y -= 3
        x += 3
    return m


def welcomeScreen():
    system('clear')
    print("Welcome to Sudoku!")
    time.sleep(1)

    difficulty = input("Please choose a difficulty level from 1-10: ")

    while difficulty not in ['1', '2,', '3', '4', '5',
                             '6', '7', '8', '9', '10']:
        print("Invalid input!")
        difficulty = input("Please choose a difficulty (1-10): ")

    return int(difficulty)


def initBoard(m):
    alreadyChosen = []

    for i in range(difficulty * 7):
        x = rnd(0, 8)
        y = rnd(0, 8)
        toBeRemoved = [y, x]
        while toBeRemoved in alreadyChosen:
            x = rnd(0, 8)
            y = rnd(0, 8)
            toBeRemoved = [y, x]

        alreadyChosen.append(toBeRemoved)
        m[y][x] = ' '
        z[y][x] = True

    return m


def takeBackLastMove():
    if len(moves) > 0:
        move = moves[len(moves) - 1]
        m[move[0]][move[1]] = move[2]
        moves.pop(len(moves) - 1)
    else:
        print("There are no moves to be taken back!")
        time.sleep(2)


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
