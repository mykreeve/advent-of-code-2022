from datetime import datetime

filename = "input/day08input.txt"
file = open(filename, "r")
file = file.readlines()

grid = {}
seen = []

now = datetime.now()
for y, f in enumerate(file):
    f = f.replace('\n', '')
    for x, p in enumerate(f):
        grid[x, y] = int(p)

for x in range(len(f)):
    curr = None
    for y in range(len(f)):
        if (curr == None or grid[x, y] > curr):
            curr = grid[x, y]
            if (x, y) not in seen:
                seen.append((x, y))
    curr = None
    for y in range(len(f)-1, -1, -1):
        if (curr == None or grid[x, y] > curr):
            curr = grid[x, y]
            if (x, y) not in seen:
                seen.append((x, y))

for y in range(len(f)-1, -1, -1):
    curr = None
    for x in range(len(f)):
        if (curr == None or grid[x, y] > curr):
            curr = grid[x, y]
            if (x, y) not in seen:
                seen.append((x, y))
    curr = None
    for x in range(len(f)-1, -1, -1):
        if (curr == None or grid[x, y] > curr):
            curr = grid[x, y]
            if (x, y) not in seen:
                seen.append((x, y))


# for y in range(99):
#     for x in range(99):
#         if (x, y) in seen:
#             print('*', end='')
#         else:
#             print('.', end='')
#     print(' ', end='')
#     for x in range(99):
#         print(grid[x, y], end='')
#     print()

done = datetime.now()
print("Answer to part 1:", len(seen))
print("Time taken:", done - now)

now = datetime.now()

best = 0

for x in range(len(f)):
    for y in range(len(f)):
        val = []
        compare = grid[x, y]
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            steps = 1
            posx = x
            posy = y
            while posx >= 0 and posx < len(f) and posy >= 0 and posy < len(f) and grid[posx, posy] <= compare:
                posx = posx + d[0]
                posy = posy + d[1]
                if posx < 0 or posx >= len(f) or posy < 0 or posy >= len(f):
                    steps -= 1
                    break
                # print(x, y, d, posx, posy, steps, grid[posx, posy])
                if grid[posx, posy] >= compare:
                    break
                steps += 1
            # print('===', x, y,  d, steps)
            val.append(steps)
        # print(x, y, val, val[0] * val[1] * val[2] * val[3])
        calc = val[0] * val[1] * val[2] * val[3]
        if calc > best:
            best = calc
            # print(x, y, calc)

done = datetime.now()
print("Answer to part 2:", best)
print("Time taken:", done - now)
