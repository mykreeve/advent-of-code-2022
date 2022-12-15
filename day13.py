from datetime import datetime
import json

filename = "input/day13input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()

pairs = []
pair = []

for f in file:
    f = f.replace('\n', '')
    if f:
        item = json.loads(f)
        pair.append(item)
    if len(pair) == 2:
        pairs.append(pair)
        pair = []


def assess_pair(left, right):
    if not isinstance(left, list) and not isinstance(right, list):
        return right - left
    if not isinstance(left, list) and isinstance(right, list):
        return assess_pair([left], right)
    if isinstance(left, list) and not isinstance(right, list):
        return assess_pair(left, [right])
    else:
        for one, two in zip(left, right):
            if (compare := assess_pair(one, two)) != 0:
                return compare
        return len(right) - len(left)


tot = 0
for int, p in enumerate(pairs):
    left = p[0]
    right = p[1]
    ass = assess_pair(left, right)
    if ass > 0:
        tot += int + 1

done = datetime.now()
print("Answer to part 1:", tot)
print("Time taken:", done - now)

now = datetime.now()

pos2 = 1
pos6 = 2
for p in pairs:
    for o in p:
        if assess_pair(o, [[2]]) > 0:
            pos2 += 1
        if assess_pair(o, [[6]]) > 0:
            pos6 += 1

done = datetime.now()
print("Answer to part 2:", pos2 * pos6)
print("Time taken:", done - now)
