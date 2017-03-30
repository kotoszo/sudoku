import time
import getch
import string
from stage_handler import makeStage


def getInput(matrix, z, moves, highlighted):
    s = getch.getch()
    print()
    matrix[highlighted[0]][highlighted[1]] = matrix[highlighted[0]][highlighted[1]][5]
    if str(s) not in string.digits:
        if s == "w":
            if highlighted[0] > 0:
                highlighted[0] -= 1
                return highlighted

        elif s == "d":
            if highlighted[1] < 8:
                highlighted[1] += 1
                return highlighted

        elif s == "s":
            if highlighted[0] < 8:
                highlighted[0] += 1
                return highlighted

        elif s == "a":
            if highlighted[1] > 0:
                highlighted[1] -= 1
                return highlighted

        elif s.lower() == 'b':
            takeBackLastMove(matrix, moves)
        elif s.lower() == 'q':
            exit()
    else:
        try:
            Number = int(s)
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
            time.sleep(2)
        finally:
            return highlighted


def moveIsValid(m, m_y, m_x, number):

    r = m[m_y][:]
    c = [x[m_x] for x in m]  # TO-DO: Merge these and the next two lines?

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


def takeBackLastMove(m, moves):
    if len(moves) > 0:
        move = moves[len(moves) - 1]
        m[move[0]][move[1]] = move[2]
        moves.pop(len(moves) - 1)
