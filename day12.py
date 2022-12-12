from datetime import datetime
import heapq
from copy import deepcopy

filename = "input/day12input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()

grid = {}

height_lookup = 'SabcdefghijklmnopqrstuvwxyzE'

for y, f in enumerate(file):
    f = f.replace('\n', '')
    for x, ch in enumerate(f):
        grid[x, len(file)-y-1] = height_lookup.index(ch)
        if ch == 'S':
            start = (x, len(file)-y-1)
        if ch == 'E':
            end = (x, len(file)-y-1)


def get_options(pos):
    opts = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    height = grid[pos]
    for d in dirs:
        if (pos[0]+d[0], pos[1]+d[1]) in grid:
            if grid[(pos[0]+d[0], pos[1]+d[1])] <= height + 1:
                opts.append((pos[0]+d[0], pos[1]+d[1]))
    return opts


visited = []
queue = []
heapq.heappush(queue, (0, start))

while len(queue) > 0:
    (time, pos) = heapq.heappop(queue)
    opts = get_options(pos)
    if pos == end:
        journey = time
        break
    for o in opts:
        if o not in visited:
            heapq.heappush(queue, (time+1, o))
            visited.append(o)

done = datetime.now()
print("Answer to part 1:", journey)
print("Time taken:", done - now)

now = datetime.now()

possible_starts = []
for d in grid:
    if (grid[d]) == 1:
        possible_starts.append(d)

gridcopy = deepcopy(grid)

best = 999999
to_do = len(possible_starts)

for p in possible_starts:
    grid = deepcopy(gridcopy)
    grid[start] = 1

    visited = []
    queue = []
    heapq.heappush(queue, (0, p))

    journey = 999999
    while len(queue) > 0:
        (time, pos) = heapq.heappop(queue)
        opts = get_options(pos)
        if pos == end:
            journey = time
            break
        for o in opts:
            if o not in visited:
                heapq.heappush(queue, (time+1, o))
                visited.append(o)

    to_do -= 1
    if journey < best:
        best = journey
    print('.', end='')
    if to_do % 100 == 0:
        print(to_do)

print()

done = datetime.now()
print("Answer to part 2:", best)
print("Time taken:", done - now)
