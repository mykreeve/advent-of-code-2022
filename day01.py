from datetime import datetime

filename = "input/day01input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()
elves = []
current = 0
for f in file:
    f = f.replace('\n', '')
    if f:
        current += (int(f))
    else:
        elves.append(current)
        current = 0

done = datetime.now()
print("Answer to part 1:", max(elves))
print("Time taken:", done - now)

now = datetime.now()

elves.sort()

done = datetime.now()
print("Answer to part 2:", elves[-1] + elves[-2] + elves[-3])
print("Time taken:", done - now)
