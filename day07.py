from datetime import datetime

filename = "input/day07input.txt"
file = open(filename, "r")
file = file.readlines()

struct = {}

now = datetime.now()
for f in file:
    f = f.replace('\n', '')
    if '$ cd' in f:
        folder = f.replace('$ cd ', '')
        if folder == '/':
            loc = '/'
        elif folder == '..':
            temp = loc.rfind('/', 0, len(loc) - 1) + 1
            loc = loc[:temp]
        else:
            loc = loc + folder + '/'
    if loc not in struct:
        struct[loc] = {'files': [], 'size': 0}
    if '$' not in f and 'dir ' not in f:
        [size, name] = f.split(' ')
        size = int(size)
        struct[loc]['files'].append({'size': size, 'name': name})
        struct[loc]['size'] += size

for s in struct:
    for oth in struct:
        if s in oth and s != oth:
            struct[s]['size'] += struct[oth]['size']

cumulative = 0

for s in struct:
    if struct[s]['size'] < 100000:
        # print(s, struct[s]['size'])
        cumulative += struct[s]['size']


done = datetime.now()
print("Answer to part 1:", cumulative)
print("Time taken:", done - now)

now = datetime.now()

empty = 70000000 - struct['/']['size']
target = 30000000 - empty

best = 70000000

for s in struct:
    val = struct[s]['size']
    if val > target and val < best:
        best = val

done = datetime.now()
print("Answer to part 2:", best)
print("Time taken:", done - now)
