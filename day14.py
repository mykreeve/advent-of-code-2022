from datetime import datetime

filename = "input/day14input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()

grid = {}

minx = 500
maxx = 500
miny = 0
maxy = 0
for f in file:
    f = f.replace('\n', '')
    f = f.split(' -> ')
    for e in f:
        e = e.split(',')
        e = (int(e[0]), int(e[1]))
        if e[0] < minx:
            minx = e[0]
        if e[0] > maxx:
            maxx = e[0]
        if e[1] < miny:
            miny = e[1]
        if e[1] > maxy:
            maxy = e[1]

for y in range(miny, maxy+2):
    for x in range(minx-1, maxx+2):
        grid[(x, y)] = '.'

for f in file:
    f = f.replace('\n', '')
    f = f.split(' -> ')
    prev = None
    for e in f:
        if not prev:
            prev = e
            continue
        prevx, prevy = prev.split(',')
        prevx = int(prevx)
        prevy = int(prevy)
        currx, curry = e.split(',')
        currx = int(currx)
        curry = int(curry)
        if prevx == currx:
            if prevy < curry:
                for y in range(prevy, curry+1):
                    grid[(prevx, y)] = '#'
            if prevy > curry:
                for y in range(curry, prevy+1):
                    grid[(prevx, y)] = '#'
        if prevy == curry:
            if prevx < currx:
                for x in range(prevx, currx+1):
                    grid[(x, prevy)] = '#'
            if prevx > currx:
                for x in range(currx, prevx+1):
                    grid[(x, prevy)] = '#'
        prev = e


def print_grid(grid):
    for y in range(miny, maxy+2):
        for x in range(minx-1, maxx+2):
            print(grid[(x, y)], end='')
        print()


def pick_move(pos, grid):
    (x, y) = pos
    if (x, y+1) not in grid:
        # print('falls off bottom')
        return (0, 0)
    if grid[(x, y+1)] == '.':
        # print('can move down')
        return (x, y+1)
    if grid[(x-1, y+1)] == '.':
        # print('can move down and left')
        return (x-1, y+1)
    if grid[(x+1, y+1)] == '.':
        # print('can move down and right')
        return (x+1, y+1)
    # print('cannot move further')
    return None


full = False
while full == False:
    pos = (500, 0)
    while pick_move(pos, grid):
        pos = pick_move(pos, grid)
        if pos == (0, 0):
            break
    if pos == (0, 0):
        full = True
    else:
        grid[pos] = 'o'
        # print_grid(grid)

tot = 0
for g in grid:
    if grid[g] == 'o':
        tot += 1

done = datetime.now()
print("Answer to part 1:", tot)
print("Time taken:", done - now)

now = datetime.now()


def new_print_grid(grid):
    for y in range(miny, maxy+3):
        for x in range(minx-11, maxx+12):
            print(grid[(x, y)], end='')
        print()


for y in range(miny, maxy+2):
    for x in range(minx-200, maxx+202):
        if (x, y) not in grid:
            grid[(x, y)] = '.'


for x in range(minx-200, maxx+202):
    grid[(x, maxy+2)] = '#'


while grid[(500, 0)] != 'o':
    pos = (500, 0)
    while pick_move(pos, grid):
        pos = pick_move(pos, grid)
    else:
        grid[pos] = 'o'

tot = 0
for g in grid:
    if grid[g] == 'o':
        tot += 1

done = datetime.now()
print("Answer to part 2:", tot)
print("Time taken:", done - now)
