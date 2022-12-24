from datetime import datetime
import heapq

filename = "input/day19input.txt"
file = open(filename, "r")
file = file.readlines()

blueprints = []

now = datetime.now()

for f in file:
    f = f.replace('\n', '')
    f = f.replace('Blueprint ', '')
    f = f.replace(': Each ore robot costs ', ',')
    f = f.replace(' ore. Each clay robot costs ', ',')
    f = f.replace(' ore. Each obsidian robot costs ', ',')
    f = f.replace(' ore and ', ',')
    f = f.replace(' clay. Each geode robot costs ', ',')
    f = f.replace(' ore and ', ',')
    f = f.replace(' obsidian.', '')
    [number, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost,
        geode_robot_ore_cost, geode_robot_obsidian_cost] = [int(val) for val in f.split(',')]

    blueprint = {
        'ore_robot_ore_cost': ore_robot_ore_cost,
        'clay_robot_ore_cost': clay_robot_ore_cost,
        'obsidian_robot_ore_cost': obsidian_robot_ore_cost,
        'obsidian_robot_clay_cost': obsidian_robot_clay_cost,
        'geode_robot_ore_cost': geode_robot_ore_cost,
        'geode_robot_obsidian_cost': geode_robot_obsidian_cost
    }
    blueprints.append(blueprint)


def get_options(geodes, obsidian, clay, ore, geode_robots,
                obsidian_robots, clay_robots, ore_robots, turn, blueprint, max_turns):
    options = []
    if turn == max_turns:
        return options
    # can build geode robot
    if ore >= blueprint['geode_robot_ore_cost'] and obsidian >= blueprint['geode_robot_obsidian_cost']:
        return ['geode']
    ore_cost = max([blueprint['ore_robot_ore_cost'],
                    blueprint['clay_robot_ore_cost'], blueprint['obsidian_robot_ore_cost'], blueprint['geode_robot_ore_cost']])
    # can build obsidian robot
    if ore >= blueprint['obsidian_robot_ore_cost'] and clay >= blueprint['obsidian_robot_clay_cost'] and obsidian_robots < blueprint['geode_robot_obsidian_cost']:
        options.append('obsidian')
    # can build clay robot
    if ore >= blueprint['clay_robot_ore_cost'] and clay_robots < blueprint['obsidian_robot_clay_cost']:
        options.append('clay')
    # can build ore robot
    if ore >= blueprint['ore_robot_ore_cost'] and ore_robots < ore_cost:
        options.append('ore')
    options.append('none')
    return options


max_turns = 24

tot = 0

for index, blueprint in enumerate(blueprints):
    turn = 1
    queue = []
    seen = []
    best = 0
    heapq.heappush(queue, (turn, 0, 0, 0, 1, 0, 0, 0, 1, []))

    while len(queue) > 0:
        pos = heapq.heappop(queue)
        (turn, geodes, obsidian, clay, ore, geode_robots,
         obsidian_robots, clay_robots, ore_robots, prev) = pos
        # if turn == 9:
        #     print(turn, geodes, obsidian, clay, ore, geode_robots,
        #           obsidian_robots, clay_robots, ore_robots)

        if turn == max_turns:
            if geodes > best:
                best = geodes
        options = get_options(geodes, obsidian, clay, ore, geode_robots,
                              obsidian_robots, clay_robots, ore_robots, turn, blueprint, max_turns)

        # print(options)
        for o in options:
            if o == 'none':
                heapq.heappush(queue, (turn + 1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots, ore + ore_robots, geode_robots,
                                       obsidian_robots, clay_robots, ore_robots, options))
            elif o in prev:
                continue
            elif o == 'geode':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots - blueprint['geode_robot_obsidian_cost'], clay + clay_robots, ore + ore_robots -
                                       blueprint['geode_robot_ore_cost'], geode_robots + 1, obsidian_robots, clay_robots, ore_robots, []))
            elif o == 'obsidian':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots - blueprint['obsidian_robot_clay_cost'], ore + ore_robots -
                                       blueprint['obsidian_robot_ore_cost'], geode_robots, obsidian_robots + 1, clay_robots, ore_robots, []))
            elif o == 'clay':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots, ore + ore_robots -
                                       blueprint['clay_robot_ore_cost'], geode_robots, obsidian_robots, clay_robots + 1, ore_robots, []))
            elif o == 'ore':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots, ore + ore_robots -
                                       blueprint['ore_robot_ore_cost'], geode_robots, obsidian_robots, clay_robots, ore_robots + 1, []))

    tot += (best * (index + 1))
    # print((index + 1), ')', best, ' => ', tot)

done = datetime.now()
print("Answer to part 1:", tot)
print("Time taken:", done - now)


now = datetime.now()

max_turns = 32
tot = 1

for index, blueprint in enumerate([blueprints[0], blueprints[1], blueprints[2]]):
    turn = 1
    queue = []
    seen = []
    best = 0
    heapq.heappush(queue, (turn, 0, 0, 0, 1, 0, 0, 0, 1, []))

    while len(queue) > 0:
        pos = heapq.heappop(queue)
        (turn, geodes, obsidian, clay, ore, geode_robots,
         obsidian_robots, clay_robots, ore_robots, prev) = pos

        if turn == max_turns:
            if geodes > best:
                best = geodes
        options = get_options(geodes, obsidian, clay, ore, geode_robots,
                              obsidian_robots, clay_robots, ore_robots, turn, blueprint, max_turns)

        for o in options:
            if o == 'none':
                heapq.heappush(queue, (turn + 1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots, ore + ore_robots, geode_robots,
                                       obsidian_robots, clay_robots, ore_robots, options))
            elif o in prev:
                continue
            elif o == 'geode':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots - blueprint['geode_robot_obsidian_cost'], clay + clay_robots, ore + ore_robots -
                                       blueprint['geode_robot_ore_cost'], geode_robots + 1, obsidian_robots, clay_robots, ore_robots, []))
            elif o == 'obsidian':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots - blueprint['obsidian_robot_clay_cost'], ore + ore_robots -
                                       blueprint['obsidian_robot_ore_cost'], geode_robots, obsidian_robots + 1, clay_robots, ore_robots, []))
            elif o == 'clay':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots, ore + ore_robots -
                                       blueprint['clay_robot_ore_cost'], geode_robots, obsidian_robots, clay_robots + 1, ore_robots, []))
            elif o == 'ore':
                heapq.heappush(queue, (turn+1, geodes + geode_robots, obsidian + obsidian_robots, clay + clay_robots, ore + ore_robots -
                                       blueprint['ore_robot_ore_cost'], geode_robots, obsidian_robots, clay_robots, ore_robots + 1, []))

    tot *= best
    # print((index + 1), ')', best, ' => ', tot)

done = datetime.now()
print("Answer to part 2:", tot)
print("Time taken:", done - now)
