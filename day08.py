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

# now = datetime.now()

# empty = 70000000 - struct['/']['size']
# target = 30000000 - empty

# best = 70000000

# for s in struct:
#     val = struct[s]['size']
#     if val > target and val < best:
#         best = val

# done = datetime.now()
# print("Answer to part 2:", best)
# print("Time taken:", done - now)
