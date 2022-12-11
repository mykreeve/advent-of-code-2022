from datetime import datetime
import math
from copy import deepcopy

filename = "input/day11input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()

monkey_states = []
monkey_behaviours = []
monkey_throws = []

current_monkey = 0
for f in file:
    f = f.replace('\n', '')
    if 'Monkey' in f:
        monkey_states.append([])
        monkey_behaviours.append({})
        monkey_throws.append(0)
    elif 'Starting items' in f:
        f = f.replace('Starting items: ', '').replace(' ', '')
        f = f.split(',')
        for item in f:
            monkey_states[current_monkey].append(int(item))
    elif 'Operation' in f:
        f = f.replace('Operation: new = old ', '').replace(' ', '')
        monkey_behaviours[current_monkey]['operation'] = f
    elif 'Test:' in f:
        f = f.replace('  Test: divisible by ', '')
        f = int(f)
        monkey_behaviours[current_monkey]['test_divisor'] = f
    elif 'true:' in f:
        f = f.replace('    If true: throw to monkey ', '')
        f = int(f)
        monkey_behaviours[current_monkey]['true'] = f
    elif 'false:' in f:
        f = f.replace('    If false: throw to monkey ', '')
        f = int(f)
        monkey_behaviours[current_monkey]['false'] = f
    else:
        current_monkey += 1


def do_assess(item, behaviour, worry, mults):
    func = behaviour['operation']
    opt = func[0]
    func = func[1:]
    if func == 'old':
        func = item
    func = int(func)
    if opt == '+':
        item = item + func
    if opt == '*':
        item = item * func
    if worry:
        item = math.floor(item // 3)
    else:
        item = item % (mults)

    if item % (behaviour['test_divisor']) == 0:
        ret = behaviour['true']
    else:
        ret = behaviour['false']
    return item, ret


def assess_score(throws):
    best1 = 0
    best2 = 0

    for m in throws:
        if m > best1:
            best2 = best1
            best1 = m
        elif m > best2:
            best2 = m

    return best1 * best2


original_states = deepcopy(monkey_states)
original_throws = deepcopy(monkey_throws)

round = 0
while round < 20:
    round += 1
    for pos, monkey_assessor in enumerate(monkey_states):
        while len(monkey_assessor) > 0:
            item = monkey_assessor.pop(0)
            new_item, pass_to = do_assess(item, monkey_behaviours[pos], True, 0)
            monkey_throws[pos] += 1
            monkey_states[pass_to] = monkey_states[pass_to] + [new_item]
        monkey_states[pos] = []

score = assess_score(monkey_throws)

done = datetime.now()
print("Answer to part 1:", score)
print("Time taken:", done - now)

now = datetime.now()

monkey_states = deepcopy(original_states)
monkey_throws = deepcopy(original_throws)

mult = 1
for m in monkey_behaviours:
	mult = mult * m['test_divisor']

round = 0
while round < 10000:
    round += 1
    prev_throws = deepcopy(monkey_throws)
    for pos, monkey_assessor in enumerate(monkey_states):
        while len(monkey_assessor) > 0:
            item = monkey_assessor.pop(0)
            new_item, pass_to = do_assess(item, monkey_behaviours[pos], False, mult)
            monkey_throws[pos] += 1
            monkey_states[pass_to] = monkey_states[pass_to] + [new_item]
        monkey_states[pos] = []

    # print(round, monkey_throws)

score = assess_score(monkey_throws)

done = datetime.now()
print("Answer to part 2:", score)
print("Time taken:", done - now)
