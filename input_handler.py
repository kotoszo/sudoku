import time
import getch
import string
from stage_handler import makeStage
from os import system


def getInput(matrix, z, moves, highlighted):
    s = getch.getch()
    matrix[highlighted[0]][highlighted[1]] = matrix[highlighted[0]][highlighted[1]][5]
    if str(s) not in string.digits:
        if s == "w" and highlighted[0] > 0:
            highlighted[0] -= 1

        elif s == "d" and highlighted[1] < 8:
            highlighted[1] += 1

        elif s == "s" and highlighted[0] < 8:
            highlighted[0] += 1

        elif s == "a" and highlighted[1] > 0:
            highlighted[1] -= 1

        elif s.lower() == 'b':
            takeBackLastMove(matrix, moves)
        elif s.lower() == 'q':
            exit()
        return highlighted
    else:
        try:
            Number = s
            m = [["." for _ in range(9)] for _ in range(9)]
            y = highlighted[0]
            x = highlighted[1]
            if z[y][x]:

                if moveIsValid(matrix, y, x, Number):
                    matrix[y][x] = Number
                    moves.append([y, x, m[y][x]])

            else:
                raise TypeError
        except TypeError:
            print("You can't rewrite that field!")
            system('cvlc Vader_noo.wav vlc://quit')
        finally:
            return highlighted


def moveIsValid(matrix, m_y, m_x, number):

    row = matrix[m_y][:]
    col = [matrow[m_x] for matrow in matrix]

    if (number in col) or (number in row):
        print("Row or column already contains that number!")
        time.sleep(2)
        return False

    m_y -= m_y % 3
    m_x -= m_x % 3

    subMatrix = []
    for i in range(3):
        for j in range(3):
            subMatrix.append(matrix[m_y + i][m_x + j])

    subMatrix = [matrix[m_y + i][m_x + j] for j in range(3) for i in range(3)]

    if str(number) in subMatrix:
        print("Submatrix already contains that number!")
        time.sleep(2)
        return False

    return True


def takeBackLastMove(m, moves):
    if len(moves) > 0:
        move = moves[len(moves) - 1]
        m[move[0]][move[1]] = move[2]
        moves.pop(len(moves) - 1)
