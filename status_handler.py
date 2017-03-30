def player_has_won(matrix):

    for row in matrix:
        for item in row:
            if item == '.':
                return False

    return True
