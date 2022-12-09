from datetime import datetime

filename = "input/day05input.txt"
file = open(filename, "r")
file = file.readlines()


now = datetime.now()
grid = []
for f in file:
    if '[' in f:
        f = f.replace(
            '\n', '').replace('\t', ' ')
        row = []
        for l, i in enumerate((f[1:len(f):2])):
            if l % 2 == 0:
                row.append(i)
        for p, r in enumerate(row):
            if len(grid) < p+1:
                grid.append([])
            if r != ' ':
                grid[p].append(r)

for f in file:
    if ('move' in f):
        f = f.replace('move ', '').replace(
            ' from ', ',').replace(' to ', ',').split(',')
        move = int(f[0])
        from_pos = int(f[1])-1
        to_pos = int(f[2])-1
        for i in range(move):
            grid[to_pos] = [grid[from_pos].pop(0)] + grid[to_pos]
        #     moving.append(grid[from_pos].pop(0))
        # grid[to_pos] = moving + grid[to_pos]
    # print(grid)
    # input('.')

solution = ''
for l in grid:
    solution += l[0]

done = datetime.now()
print("Answer to part 1:", solution)
print("Time taken:", done - now)

now = datetime.now()
grid = []
for f in file:
    if '[' in f:
        f = f.replace(
            '\n', '').replace('\t', ' ')
        row = []
        for l, i in enumerate((f[1:len(f):2])):
            if l % 2 == 0:
                row.append(i)
        for p, r in enumerate(row):
            if len(grid) < p+1:
                grid.append([])
            if r != ' ':
                grid[p].append(r)

for f in file:
    if ('move' in f):
        f = f.replace('move ', '').replace(
            ' from ', ',').replace(' to ', ',').split(',')
        move = int(f[0])
        from_pos = int(f[1])-1
        to_pos = int(f[2])-1
        moving = []
        for i in range(move):
            moving.append(grid[from_pos].pop(0))
        grid[to_pos] = moving + grid[to_pos]

solution = ''
for l in grid:
    solution += l[0]


done = datetime.now()
print("Answer to part 2:", solution)
print("Time taken:", done - now)
