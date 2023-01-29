import collections

file = open('input/day20input.txt', 'r')
file = file.readlines()

original = []

for f in file:
    f = int(f.replace('\n', ''))
    original.append(f)

loop = collections.deque(original)
idc = collections.deque(range(0, length := len(loop)))

for idx in range(length):
    position = idc.index(idx)
    for deq in [loop, idc]:
        deq.rotate(position * -1)
        local_value = deq.popleft()
        if deq == loop:
            current_value = local_value
        deq.rotate(current_value * -1)
        deq.appendleft(local_value)

pos = loop.index(0)
loop.rotate(-pos)
sum = 0
loop.rotate(-1000)
sum += loop[0]
loop.rotate(-1000)
sum += loop[0]
loop.rotate(-1000)
sum += loop[0]

print('Part 1: ', sum)

loop = collections.deque([*map(lambda n: n*811589153, original)])
idc = collections.deque(range(0, length := len(loop)))

for iter in range(10):
    for idx in range(length):
        position = idc.index(idx)
        for deq in [loop, idc]:
            deq.rotate(position * -1)
            local_value = deq.popleft()
            if deq == loop:
                current_value = local_value
            deq.rotate(current_value * -1)
            deq.appendleft(local_value)

pos = loop.index(0)
loop.rotate(-pos)
sum = 0
loop.rotate(-1000)
sum += loop[0]
loop.rotate(-1000)
sum += loop[0]
loop.rotate(-1000)
sum += loop[0]

print('Part 2: ', sum)
