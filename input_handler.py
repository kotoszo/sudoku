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
                y = int(s[0]) - 1
                x = int(s[1]) - 1
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


def takeBackLastMove():
    if len(moves) > 0:
        move = moves[len(moves) - 1]
        m[move[0]][move[1]] = move[2]
        moves.pop(len(moves) - 1)
    else:
        print("There are no moves to be taken back!")
        time.sleep(2)
