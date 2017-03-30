
def subMatrixesAreClean(matrix):
    # Checks whether every submatrix is clean on the board
    clean = True

    for y in range(0, 7, 3):
        for x in range(0, 7, 3):

            subMatrix = [matrix[y + j][x + i] for i in range(3) for j in range(3)]

            if len(subMatrix) != len(set(subMatrix)):
                clean = False

            for i in range(1, 10):
                if i not in subMatrix:
                    clean = False

    return clean


def playerHasWon(matrix):

    won = True

    for row in matrix:
        for item in row:
            if item == '.':
                return False

    return won
