from datetime import datetime
from copy import deepcopy

filename = "input/day18input.txt"
file = open(filename, "r")
file = file.readlines()

grid = {}

now = datetime.now()

for f in file:
    grid[tuple([int(x) for x in f.replace('\n', '').split(',')])] = '#'

newgrid = deepcopy(grid)

for item in grid:
    if grid[item] == '#':
        for x in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]:
            new = (item[0] + x[0], item[1] + x[1], item[2] + x[2])
            if new not in newgrid:
                newgrid[new] = '.'

count = 0

for item in newgrid:
    if newgrid[item] == '.':
        for x in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]:
            new = (item[0] + x[0], item[1] + x[1], item[2] + x[2])
            if new in newgrid and newgrid[new] == '#':
                count += 1

done = datetime.now()
print("Answer to part 1:", count)
print("Time taken:", done - now)

now = datetime.now()


def get_opts(pos, grid):
    opts = []
    for x in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]:
        new = (pos[0] + x[0], pos[1] + x[1], pos[2] + x[2])
        if new not in grid and new[0] <= highest and new[0] >= lowest and new[1] <= highest and new[1] >= lowest and new[2] <= highest and new[2] >= lowest:
            opts.append(new)
    return opts


mins = [min([n[y] for n in grid]) for y in [0, 1, 2]]
maxs = [max([n[y] for n in grid]) for y in [0, 1, 2]]

lowest = min(mins) - 1
highest = max(maxs) + 1

opts = [(lowest, lowest, lowest)]

while len(opts) > 0:
    pos = opts.pop(0)
    new_opts = get_opts(pos, grid)
    for n in new_opts:
        if n not in opts:
            opts.append(n)
    grid[pos] = '.'

count = 0

for item in grid:
    if grid[item] == '.':
        for x in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]:
            new = (item[0] + x[0], item[1] + x[1], item[2] + x[2])
            if new in grid and grid[new] == '#':
                count += 1

done = datetime.now()
print("Answer to part 2:", count)
print("Time taken:", done - now)
