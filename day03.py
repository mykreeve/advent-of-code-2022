from datetime import datetime
from re import I

filename = "input/day03input.txt"
file = open(filename, "r")
file = file.readlines()


def get_priority(item):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alpha.index(item) + 1

def get_common(a,b):
    common = []
    for item in a:
        if b.find(item) >= 0:
            if item not in common:
                common.append(item)
    return ''.join(common)


now = datetime.now()
priority = 0
for f in file:
    f = f.replace('\n', '')
    length = int(len(f)/2)
    upper = f[:length]
    lower = f[length:]
    found = 0
    for item in upper:
        if lower.find(item) >= 0 and found == 0:
            found += 1
            priority += get_priority(item)

done = datetime.now()
print("Answer to part 1:", priority)
print("Time taken:", done - now)

now = datetime.now()
priority = 0
pos = 0
working = []
for f in file:
    f = f.replace('\n', '')
    pos += 1
    working.append(f)
    if pos == 3:
        val = get_common(get_common(working[0], working[1]), working[2])
        priority += get_priority(val)
        pos = 0
        working = []

done = datetime.now()
print("Answer to part 2:", priority)
print("Time taken:", done - now)
