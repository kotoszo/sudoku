def makeStage():
    # List, what contains numbers, between 1 and 9 and then shuffle it.
    l = [x for x in range(1, 10)]
    shuffle(l)

    # Generates empty 'places'
    m = [[None for _ in range(9)] for _ in range(9)]
    y, x = 0, 0
    k = 0
    # The upperleft block
    for i in range(3):
        for i in range(3):
            m[y][x] = l[k]
            x += 1
            k += 1
        x = 0
        y += 1

    # The uppermiddle block
    x, y = 0, 0
    for i in range(3):
        m[y][3 + x] = m[1 + y][x]
        x += 1
    x = 0
    for i in range(3):
        m[1 + y][3 + x] = m[2 + y][x]
        x += 1
    y, x = 0, 0
    for i in range(3):
        m[2 + y][3 + x] = m[y][x]
        x += 1

    # The upperright block
    y = 0
    for i in range(1):
        for i in range(3):
            m[y][6 + x] = m[1 + y][x]
            x += 1
        y = 0
        x = 3
        for i in range(3):
            m[1 + y][6 + x] = m[2 + y][x]
            x += 1
        y, x = 0, 3
        for i in range(3):
            m[2 + y][6 + x] = m[y][x]
            x += 1

    # The middle columns, what copies coordinates
    y, x = 0, 0
    for i in range(3):
        for i in range(3):
            m[3 + y][2 + x] = m[y][x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][0 + x] = m[y][1 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][1 + x] = m[y][2 + x]
            y += 1
        y -= 3
        x += 3

    # The lower columns, what copies coordinates
    x = 0
    y = 3
    for i in range(3):
        for i in range(3):
            m[3 + y][2 + x] = m[y][x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][0 + x] = m[y][1 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][1 + x] = m[y][2 + x]
            y += 1
        y -= 3
        x += 3
    return m


#
def initBoard(m):
    already_chosen = []

    for i in range(difficulty * 7):
        x = rnd(0, 8)
        y = rnd(0, 8)
        toBeRemoved = [y, x]
        while to_be_removed in already_chosen:
            x = rnd(0, 8)
            y = rnd(0, 8)
            toBeRemoved = [y, x]

        alreadyChosen.append(toBeRemoved)
        m[y][x] = ' '
        z[y][x] = True

    return m
