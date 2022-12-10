from datetime import datetime

filename = "input/day10input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()

instructions = []
for f in file:
    f = f.replace('\n', '')
    if 'addx' in f:
        inst, val = f.split(' ')
    else:
        inst = f
        val = 0
    val = int(val)
    instructions.append((inst, val))

register = 1
time = 0
register_values = [1]
for i in instructions:
    if i[0] == 'addx':
        register_values += [register, register]
        register += i[1]
        time += 2
    else:
        register_values += [register]
        time += 1

important_vals = [20, 60, 100, 140, 180, 220]
tot = 0
for i in important_vals:
    tot += register_values[i] * i

done = datetime.now()
print("Answer to part 1:", tot)
print("Time taken:", done - now)

now = datetime.now()

register_values.pop(0)

pix = 0
shape = []
for r in register_values:
    if pix % 40 in [r-1, r, r+1]:
        shape += ['*']
    else:
        shape += ['.']
    pix += 1

done = datetime.now()
print("Answer to part 2:")
for x, d in enumerate(shape):
    print(d, end='')
    if (x + 1) % 40 == 0:
        print()
print("Time taken:", done - now)
