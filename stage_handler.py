from random import shuffle
from random import randint as rnd
from output_handler import bcolors


def make_stage():
    '''Creates a 9x9 matrix of random numbers'''

    l = [x for x in range(1, 10)]
    m = [[None for _ in range(9)] for _ in range(9)]
    shuffle(l)
    l = [str(i) for i in l]
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
    for i in range(3):
        m[y][3 + x] = m[1 + y][x]
        x += 1
    y += 0
    x = 0
    for i in range(3):
        m[1 + y][3 + x] = m[2 + y][x]
        x += 1
    y, x = 0, 0
    for i in range(3):
        m[2 + y][3 + x] = m[y][x]
        x += 1
    x = 3
    y = 0
    for i in range(3):
        m[y][3 + x] = m[1 + y][x]
        x += 1
    y = 0
    x = 3
    for i in range(3):
        m[1 + y][3 + x] = m[2 + y][x]
        x += 1
    y, x = 0, 3
    for i in range(3):
        m[2 + y][3 + x] = m[y][x]
        x += 1

    y = 0
    x = 0
    # középső oszlopok
    for i in range(3):
        for i in range(3):
            m[3 + y][2 + x] = m[y][x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][x] = m[y][1 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][1 + x] = m[y][2 + x]
            y += 1
        y -= 3
        x += 3
    x = 0
    y = 3
    # lsó oszlopok
    for i in range(3):
        for i in range(3):
            m[3 + y][2 + x] = m[y][x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][x] = m[y][1 + x]
            y += 1
        y -= 3
        for i in range(3):
            m[3 + y][1 + x] = m[y][2 + x]
            y += 1
        y -= 3
        x += 3
    return m


def init_board(m, difficulty, z):
    '''Initalizes a full 9x9 board by removing 7*difficulty numbers
       from random places and replacing them with dots.

       Args:
       m: the 9x9 matrix,
       difficulty: guess,
       z: the matrix used to mark the initial numbers so that they can't be rewritten.
    '''

    already_chosen = []

    for i in range(difficulty * 7):
        x = rnd(0, 8)
        y = rnd(0, 8)
        to_be_removed = [y, x]
        while to_be_removed in already_chosen:
            x = rnd(0, 8)
            y = rnd(0, 8)
            to_be_removed = [y, x]

        already_chosen.append(to_be_removed)
        m[y][x] = "."
        z[y][x] = True

    return m
