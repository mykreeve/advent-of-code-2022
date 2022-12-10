from datetime import datetime
from copy import deepcopy

filename = "input/day09input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()
pos_head = [0, 0]
pos_tail = [0, 0]
instructions = []
for f in file:
    f = f.replace('\n', '')
    dir, steps = f.split(' ')
    steps = int(steps)
    instructions.append((dir, steps))

trans_dir = {'L': (-1, 0), 'U': (0, 1), 'R': (1, 0), 'D': (0, -1)}


def move_head(pos, dir):
    return (pos[0] + trans_dir[dir][0], pos[1] + trans_dir[dir][1])


def tail_needs_to_move(head, tail):
    if abs(head[0] - tail[0]) > 1:
        return True
    if abs(head[1] - tail[1]) > 1:
        return True
    return False


def move_tail(tail, head):
    tail = [tail[0], tail[1]]
    head = [head[0], head[1]]
    if (tail[0] > head[0]):
        tail[0] -= 1
        if (tail[1] < head[1]):
            tail[1] += 1
        elif (tail[1] > head[1]):
            tail[1] -= 1
        return tail
    elif (tail[0] < head[0]):
        tail[0] += 1
        if (tail[1] < head[1]):
            tail[1] += 1
        elif (tail[1] > head[1]):
            tail[1] -= 1
        return tail
    if (tail[1] > head[1]):
        tail[1] -= 1
        if (tail[0] < head[0]):
            tail[0] += 1
        elif (tail[0] > head[0]):
            tail[0] -= 1
        return tail
    elif (tail[1] < head[1]):
        tail[1] += 1
        if (tail[0] < head[0]):
            tail[0] += 1
        elif (tail[0] > head[0]):
            tail[0] -= 1
        return tail
    return tail


positions = [[0, 0]]
for i in instructions:
    dir, steps = i
    # print(i)
    for n in range(steps):
        pos_head = move_head(pos_head, dir)
        tail_assess = tail_needs_to_move(pos_head, pos_tail)
        if tail_assess:
            pos_tail = move_tail(pos_tail, pos_head)
        # print(pos_head, pos_tail)
        if pos_tail not in positions:
            positions.append(pos_tail)

# for y in range(100, -100, -1):
#     for x in range(-100, 100, 1):
#         if [x, y] in positions:
#             print('*', end='')
#         else:
#             print('.', end='')
#     print()


done = datetime.now()
print("Answer to part 1:", len(positions))
print("Time taken:", done - now)

now = datetime.now()

rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
        [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

positions = [[0, 0]]
for i in instructions:
    dir, steps = i
    for n in range(steps):
        new_rope = deepcopy(rope)
        new_rope[0] = move_head(rope[0], dir)
        for r in range(1, 10):
            step_assess = tail_needs_to_move(rope[r], new_rope[r-1])
            if step_assess:
                new_rope[r] = move_tail(rope[r], new_rope[r-1])
        if new_rope[9] not in positions:
            positions.append(new_rope[9])
        rope = deepcopy(new_rope)
    # print(i)

# print(len(positions))

done = datetime.now()
print("Answer to part 2:", len(positions))
print("Time taken:", done - now)
