RED = [.6 , .2 , .2, 50]
BLU = [.09, .18, .6, 50]
BCOLOR = [RED,BLU]

def iscolor(arr):
    if arr == RED:
        return 'Red'
    elif arr == BLU:
        return 'Blue'
    else:
        return 'unknown'

def getsxy(btn):
    '''make x and y numbers from str "x y"
    example: "4 2" -> x=4, y=2'''
    xy = btn.text
    xy = xy.split(' ')
    return int(xy[0]), int(xy[1])

def makexy(x, y):
    '''make str from x and y
    reverse from getsxy'''
    return str(x) + ' ' + str(y)

def find_end_dots(x,y):
    '''finds dots, which are end of vectors
    with possible victory sequence'''
    fdots = []
    if y - 3 >= 1:
        fdots.append((x, y - 3))
        if x - 3 >= 1: fdots.append((x - 3, y - 3))
        if x + 3 <= 6: fdots.append((x + 3, y - 3))
    if y + 3 <= 7:
        fdots.append((x, y + 3))
        if x - 3 >= 1: fdots.append((x - 3, y + 3))
        if x + 3 <= 6: fdots.append((x + 3, y + 3))
    if x - 3 >= 1: fdots.append((x - 3, y))
    if x + 3 <= 6: fdots.append((x + 3, y))

    return fdots

def find_end_steps(x,y,fdots):
    '''iteration tool, used to find direction
    to count and compare vector'''
    steps = []
    for dot in fdots:
        steps.append(
            (
                int((x - dot[0]) / -3),
                int((y - dot[1]) / -3)
            )
        )
    return steps