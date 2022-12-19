from datetime import datetime
import heapq

filename = "input/day16input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()

valves = {}

for f in file:
    f = f.replace('\n', '')
    f = f.replace('Valve ', '')
    f = f.replace(' has flow rate=', ',')
    f = f.replace('; tunnel leads to valve ', ',')
    f = f.replace('; tunnels lead to valves ', ',')
    f = f.replace(', ', ',')
    f = f.split(',')
    name = f.pop(0)
    rate = int(f.pop(0))
    tunnels = f
    valves[name] = {'rate': rate, 'tunnels': tunnels}

options = []
heapq.heappush(options, (0, 1, [], 'AA'))


def get_flow_from_valves(t):
    tot = 0
    for v in t:
        tot += valves[v]['rate']
    return tot


def get_new_options(cum_flow, time, open_valves, location):
    ops = []
    if time == 30:
        return []
    if location not in open_valves and valves[location]['rate'] != 0:
        ops.append((cum_flow, time+1, open_valves+[location], location))
    for dest in valves[location]['tunnels']:
        ops.append((cum_flow, time+1, open_valves, dest))
    return ops


best_at_loc = {}

best = 0
while len(options) > 0:
    (cum_flow, time, open_valves, location) = heapq.heappop(options)
    cum_flow = cum_flow - get_flow_from_valves(open_valves)
    if time == 30:
        if abs(cum_flow) > best:
            print(abs(cum_flow), open_valves)
            best = abs(cum_flow)
    next = get_new_options(cum_flow, time, open_valves, location)
    for n in next:
        if n not in options:
            l = ','.join(n[2])
            if (l, n[3]) not in best_at_loc:
                best_at_loc[(l, n[3])] = {'cum': abs(cum_flow), 'time': time}
                heapq.heappush(options, n)
            if best_at_loc[(l, n[3])]['time'] > time or (best_at_loc[(l, n[3])]['time'] >= time and best_at_loc[(l, n[3])]['cum'] < abs(cum_flow)):
                best_at_loc[(l, n[3])] = {'cum': abs(cum_flow), 'time': time}
                heapq.heappush(options, n)
            # if (l, n[3]) not in best_at_loc:
            #     best_at_loc[(l, n[3])] = abs(cum_flow)
            # if best_at_loc[(l, n[3])] >= abs(cum_flow):
            #     best_at_loc[(l, n[3])] = abs(cum_flow)
            #     heapq.heappush(options, n)

done = datetime.now()
print("Answer to part 1:", best)
print("Time taken:", done - now)

now = datetime.now()
options = []
heapq.heappush(options, (0, 1, [], ['AA', 'AA']))

full_valves = []
for v in valves:
    if valves[v]['rate'] > 0:
        full_valves.append(v)
full_valves.sort()


def get_options_for_two(cum_flow, time, open_valves, locations):
    ops = []
    if time == 26:
        return []
    if open_valves == full_valves:
        return [(cum_flow, time+1, open_valves, locations)]
    # first player can open valve?
    if locations[0] not in open_valves and valves[locations[0]]['rate'] != 0:
        # both players can open valve?
        if locations[1] != locations[0] and locations[1] not in open_valves and valves[locations[1]]['rate'] != 0:
            ops.append((cum_flow, time+1, open_valves+locations, locations))
        for d in valves[locations[1]]['tunnels']:
            ops.append((cum_flow, time+1, open_valves +
                       [locations[0]], [locations[0], d]))
    # second player can open valve
    if locations[1] != locations[0] and locations[1] not in open_valves and valves[locations[1]]['rate'] != 0:
        for d in valves[locations[0]]['tunnels']:
            ops.append((cum_flow, time+1, open_valves +
                       [locations[1]], [d, locations[1]]))
    # neither player can open valve
    for d1 in valves[locations[1]]['tunnels']:
        for d2 in valves[locations[0]]['tunnels']:
            ops.append((cum_flow, time+1, open_valves, [d1, d2]))
    return ops


best_at_loc = {}

best = 0
while len(options) > 0:
    (cum_flow, time, open_valves, location) = heapq.heappop(options)
    cum_flow = cum_flow - get_flow_from_valves(open_valves)
    open_valves.sort()
    location.sort()
    if time == 26:
        if abs(cum_flow) > best:
            print(abs(cum_flow), open_valves, len(options))
            best = abs(cum_flow)
    next = get_options_for_two(cum_flow, time, open_valves, location)
    # print('---')
    # print(cum_flow, time, open_valves, location)
    # print('---')
    # print(next)
    # input('.')
    for n in next:
        if n[2] == full_valves:
            heapq.heappush(options, n)
        if n not in options:
            l = ','.join(n[2])
            m = ','.join(n[3])
            if (l, m) not in best_at_loc:
                best_at_loc[(l, m)] = {'cum': abs(cum_flow), 'time': time}
                heapq.heappush(options, n)
            if best_at_loc[(l, m)]['time'] > time or (best_at_loc[(l, m)]['time'] >= time and best_at_loc[(l, m)]['cum'] < abs(cum_flow)):
                best_at_loc[(l, m)] = {'cum': abs(cum_flow), 'time': time}
                heapq.heappush(options, n)

done = datetime.now()
print("Answer to part 2:", best)
print("Time taken:", done - now)
