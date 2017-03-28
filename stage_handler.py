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
            m[0 + y][3 + x] = m[1 + y][0 + x]
            x += 1
        y += 0
        x = 0
        for i in range(3):
            m[1 + y][3 + x] = m[2 + y][0 + x]
            x += 1
        y, x = 0, 0
        for i in range(3):
            m[2 + y][3 + x] = m[0 + y][0 + x]
            x += 1
    x = 3
    y = 0
    for i in range(1):
        for i in range(3):
            m[0 + y][3 + x] = m[1 + y][0 + x]
            x += 1
        y = 0
        x = 3
        for i in range(3):
            m[1 + y][3 + x] = m[2 + y][0 + x]
            x += 1
        y, x = 0, 3
        for i in range(3):
            m[2 + y][3 + x] = m[0 + y][0 + x]
            x += 1

    y = 0
    x = 0
    # középső oszlopok
    for i in range(3):
        for i in range(3):
            m[3 + y][2 + x] = m[0 + y][0 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][0 + x] = m[0 + y][1 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][1 + x] = m[0 + y][2 + x]
            y += 1
        y -= 3
        x += 3
    x = 0
    y = 3
    # lsó oszlopok
    for i in range(3):
        for i in range(3):
            m[3 + y][2 + x] = m[0 + y][0 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][0 + x] = m[0 + y][1 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][1 + x] = m[0 + y][2 + x]
            y += 1
        y -= 3
        x += 3
    return m


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
