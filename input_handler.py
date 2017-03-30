import time
import getch
import string
from os import system
import vlc


def get_input(matrix, z, moves, highlighted):
    '''Input section. It requires a matrix, a list where are the numbers are missing,
        the 'history' of the game and the coordinates of the of the player'''
    # Character input without hitting enter.
    s = getch.getch()

    # Removes the color, so restores the original form of the number.
    # (If you move away from your last position, ofc)
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
            # With dots, the 'map' is filled, where is no number from the basic matrix.
            # m = [["." for _ in range(9)] for _ in range(9)]
            y = highlighted[0]
            x = highlighted[1]
            if z[y][x]:

                if move_is_valid(matrix, y, x, Number):
                    matrix[y][x] = Number
                    moves.append([y, x, matrix[y][x]])

            else:
                raise TypeError
        except TypeError:
            print("You can't rewrite that field!")
            # NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
            vlc.MediaPlayer("Vader_noo.wav").play()
            time.sleep(2)
        finally:
            return highlighted


# Checks wheter you can do it or not.
def move_is_valid(matrix, m_y, m_x, number):
    '''Fills the row list with the numbers from the rows. (wow)'''
    row = matrix[m_y][:]
    # Same, but with the columns.
    col = [matrow[m_x] for matrow in matrix]

    # ...
    if (number in col) or (number in row):
        print("Row or column already contains that number!")
        vlc.MediaPlayer("Vader_noo.wav").play()
        time.sleep(2)
        return False

    # Wherever you are, it will jumo back to the block's starting coordinates
    # e.g. if y is 3 and x is 3 it will change it to y 0 and x 0
    m_y -= m_y % 3
    m_x -= m_x % 3
    # It will copy all the elements from the matrix into the sub_matrix
    sub_matrix = [matrix[m_y + i][m_x + j] for j in range(3) for i in range(3)]

    # just read it.
    if str(number) in sub_matrix:
        print("Submatrix already contains that number!")
        vlc.MediaPlayer("Vader_noo.wav").play()
        time.sleep(2)
        return False

    return True


def take_back_last_move(matrix, moves):
    ''' If you want to delete your last move '''
    if len(moves) > 0:
        move = moves[len(moves) - 1]
        matrix[move[0]][move[1]] = move[2]
        moves.pop(len(moves) - 1)
