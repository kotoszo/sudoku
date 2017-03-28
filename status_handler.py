def is_clean(col):
    # a list (of a column or a row of the board)
    # returns whether it contains every number from 1-9 without duplicates.

    clean = True

    clean = (len(col) != len(set(col)))
    [clean = False if i not in col for i in range(1, 10)]

    return clean


def subMatrixesAreClean(matrix):
    # Checks whether every submatrix is clean on the board
    clean = True

    for y in range(0, 7, 3):
        for x in range(0, 7, 3):

            subMatrix = [matrix[y + j][x + i] for i in range(3) for j in range(3)]
            print(subMatrix)

            if len(subMatrix) != len(set(subMatrix)):
                clean = False

            for i in range(1, 10):
                if i not in subMatrix:
                    clean = False

    return clean


def playerHasWon(matrix):

    won = True

    for i in range(9):
        column = [x[i] for x in matrix]
        row = matrix[i]

        if not (is_clean(row) and is_clean(column)):
            won = False

    if not subMatrixesAreClean(matrix):
        won = False

    return won
