
def sub_matrixes_are_clean(matrix):
    # Checks whether every submatrix is clean on the board

    for y in range(0, 7, 3):
        for x in range(0, 7, 3):

            subMatrix = [matrix[y + j][x + i] for i in range(3) for j in range(3)]

            if len(subMatrix) != len(set(subMatrix)):  # Checks duplicates
                return False

            for i in range(1, 10):  # Checks whether every number is present
                if i not in subMatrix:
                    return False

    return True  # If it reached this far, it's clean.


def player_has_won(matrix):

    for row in matrix:
        for item in row:
            if item == '.':
                return False

    return True
