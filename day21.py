from datetime import datetime

filename = "input/day21input.txt"
file = open(filename, "r")
file = file.readlines()

monkeys = {}

maths_symbols = ['+', '-', '*', '/']

now = datetime.now()

for f in file:
    f = f.replace('\n', '')
    f = f.split(': ')
    if any(x in f[1] for x in maths_symbols):
        monkeys[f[0]] = {'first': f[1][:4],
                         'second': f[1][7:], 'symbol': f[1][5:6]}
    else:
        monkeys[f[0]] = int(f[1])

unresolved = len(monkeys)

while unresolved > 0:
    unresolved = len(monkeys)
    for m in monkeys:
        if isinstance(monkeys[m], int):
            unresolved -= 1
        else:
            if isinstance(monkeys[monkeys[m]['first']], int) and isinstance(monkeys[monkeys[m]['second']], int):
                if monkeys[m]['symbol'] == '+':
                    monkeys[m] = int(monkeys[monkeys[m]['first']] +
                                     monkeys[monkeys[m]['second']])
                elif monkeys[m]['symbol'] == '-':
                    monkeys[m] = int(monkeys[monkeys[m]['first']] -
                                     monkeys[monkeys[m]['second']])
                elif monkeys[m]['symbol'] == '*':
                    monkeys[m] = int(monkeys[monkeys[m]['first']] *
                                     monkeys[monkeys[m]['second']])
                elif monkeys[m]['symbol'] == '/':
                    monkeys[m] = int(monkeys[monkeys[m]['first']] /
                                     monkeys[monkeys[m]['second']])

done = datetime.now()
print("Answer to part 1:", monkeys['root'])
print("Time taken:", done - now)

testval = 3099532691300
unsolved = True

while unsolved:
    monkeys = {}
    for f in file:
        f = f.replace('\n', '')
        f = f.split(': ')
        if any(x in f[1] for x in maths_symbols):
            monkeys[f[0]] = {'first': f[1][:4],
                             'second': f[1][7:], 'symbol': f[1][5:6]}
        elif f[0] == 'humn':
            monkeys['humn'] = testval
        else:
            monkeys[f[0]] = int(f[1])

    unresolved = True
    while unresolved:
        for m in monkeys:
            if isinstance(monkeys[m], int):
                continue
            else:
                if isinstance(monkeys[monkeys[m]['first']], int) and isinstance(monkeys[monkeys[m]['second']], int):
                    if m == 'root':
                        unresolved = False
                        # print(
                        #     testval, ': ', monkeys[monkeys[m]['first']], monkeys[monkeys[m]['second']])
                        if monkeys[monkeys[m]['first']] == monkeys[monkeys[m]['second']]:
                            unsolved = False
                            # print(testval)
                    elif monkeys[m]['symbol'] == '+':
                        monkeys[m] = int(monkeys[monkeys[m]['first']] +
                                         monkeys[monkeys[m]['second']])
                    elif monkeys[m]['symbol'] == '-':
                        monkeys[m] = int(monkeys[monkeys[m]['first']] -
                                         monkeys[monkeys[m]['second']])
                    elif monkeys[m]['symbol'] == '*':
                        monkeys[m] = int(monkeys[monkeys[m]['first']] *
                                         monkeys[monkeys[m]['second']])
                    elif monkeys[m]['symbol'] == '/':
                        monkeys[m] = int(monkeys[monkeys[m]['first']] /
                                         monkeys[monkeys[m]['second']])
    testval -= 1

print("Answer to part 2:", testval + 1)
