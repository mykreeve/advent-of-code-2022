from datetime import datetime
import math

filename = "input/day17input.txt"
file = open(filename, "r")
file = file.readlines()

winds = file[0].replace('\n', '')

now = datetime.now()

pieces = [
    [['@', '@', '@', '@']],
    [['.', '@', '.'], ['@', '@', '@'], ['.', '@', '.']],
    [['.', '.', '@'], ['.', '.', '@'], ['@', '@', '@']],
    [['@'], ['@'], ['@'], ['@']],
    [['@', '@'], ['@', '@']]
]

playspace = {}

for y in range(10):
    for x in range(9):
        if y == 0:
            playspace[(x, y)] = '-'
        elif x == 0 or x == 8:
            playspace[(x, y)] = '|'
        else:
            playspace[(x, y)] = '.'


def print_playspace(space):
    miny = 99999999
    maxy = 0
    for s in space:
        if s[1] > maxy:
            maxy = s[1]
        if s[1] < miny:
            miny = s[1]
    for y in range(maxy, miny-1, -1):
        for x in range(9):
            print(space[(x, y)], end='')
        print('')
    print('')


def highest_point(space):
    maxy = 0
    for s in space:
        if space[s] == '#':
            if s[1] > maxy:
                maxy = s[1]
    return maxy


def can_move(space, dir):
    for s in space:
        if space[s] == '@':
            if space[(s[0] + dir, s[1])] not in ['.', '@']:
                return False
    return True


def can_drop(space):
    for s in space:
        if space[s] == '@':
            if space[(s[0], s[1]-1)] not in ['.', '@']:
                return False
    return True


def get_pieces(space):
    p = []
    for s in space:
        if space[s] == '@':
            p.append(s)
    return p


def take_second(elem):
    return elem[1]


def move_parts(space, parts, dir):
    if dir == 1:
        parts = parts[::-1]
    for p in parts:
        space[p] = '.'
        space[(p[0] + dir, p[1])] = '@'
    return space


def drop_parts(space, parts):
    for p in parts:
        space[p] = '.'
        space[(p[0], p[1]-1)] = '@'
    return space


def lock_parts(space, parts):
    for p in parts:
        space[p] = '#'
    return space


def build_space(space, needed):
    maxy = 0
    for s in space:
        if s[1] > maxy:
            maxy = s[1]
    for y in range(maxy+1, needed+5):
        for x in range(9):
            if y == 0:
                space[(x, y)] = '-'
            elif x == 0 or x == 8:
                space[(x, y)] = '|'
            else:
                space[(x, y)] = '.'
    return space


def clear_out_of_play(space):
    vals = [0, 0, 0, 0, 0, 0, 0]
    for s in space:
        if space[s] == '#':
            if vals[s[0] - 1] < s[1]:
                vals[s[0] - 1] = s[1]
    miny = min(vals)
    new = {}
    for s in space:
        if s[1] >= miny:
            new[s] = space[s]
    return new


def get_tops(space):
    vals = [0, 0, 0, 0, 0, 0, 0]
    for s in space:
        if space[s] == '#':
            if vals[s[0] - 1] < s[1]:
                vals[s[0] - 1] = s[1]
    miny = min(vals)
    new_vals = [l - miny for l in vals]
    return new_vals


wind = 0
wind_length = len(winds)
piece = 0
piece_length = len(pieces)

while piece < 2022:

    curr_piece = pieces[piece % piece_length]

    # find start location
    starty = highest_point(playspace) + 4
    startx = 3

    if (startx, starty+4) not in playspace:
        playspace = build_space(playspace, starty)

    # put piece in place
    posy = starty
    piece_height = len(curr_piece)
    for piecey in range(piece_height-1, -1, -1):
        posx = startx
        for piecex in range(len(curr_piece[0])):
            playspace[(posx, posy)] = curr_piece[piecey][piecex]
            posx += 1
        posy += 1

    can_fall = True
    while can_fall:
        # wind move
        curr_wind = winds[wind % wind_length]
        if curr_wind == '<':
            curr_wind = -1
        else:
            curr_wind = 1
        if can_move(playspace, curr_wind):
            parts = get_pieces(playspace)
            parts.sort()
            playspace = move_parts(playspace, parts, curr_wind)
        wind += 1

        # drop
        can_fall = can_drop(playspace)
        if can_fall:
            parts = get_pieces(playspace)
            parts = sorted(parts, key=take_second)
            playspace = drop_parts(playspace, parts)

    parts = get_pieces(playspace)
    playspace = lock_parts(playspace, parts)

    if (piece > 0 and piece % 10 == 0):
        playspace = clear_out_of_play(playspace)

    piece += 1


done = datetime.now()
print("Answer to part 1:", highest_point(playspace))
print("Time taken:", done - now)


now = datetime.now()

wind = 0
wind_length = len(winds)
piece = 0
piece_length = len(pieces)
playspace = {}
seen = {}
last = None
found = False
add_this_many_to_height = None

for y in range(10):
    for x in range(9):
        if y == 0:
            playspace[(x, y)] = '-'
        elif x == 0 or x == 8:
            playspace[(x, y)] = '|'
        else:
            playspace[(x, y)] = '.'

while piece < 1000000000000:

    curr_piece = pieces[piece % piece_length]

    # find start location
    starty = highest_point(playspace) + 4
    startx = 3

    if (startx, starty+4) not in playspace:
        playspace = build_space(playspace, starty)

    # put piece in place
    posy = starty
    piece_height = len(curr_piece)
    for piecey in range(piece_height-1, -1, -1):
        posx = startx
        for piecex in range(len(curr_piece[0])):
            playspace[(posx, posy)] = curr_piece[piecey][piecex]
            posx += 1
        posy += 1

    can_fall = True
    while can_fall:
        # wind move
        curr_wind = winds[wind % wind_length]
        if curr_wind == '<':
            curr_wind = -1
        else:
            curr_wind = 1
        if can_move(playspace, curr_wind):
            parts = get_pieces(playspace)
            parts.sort()
            playspace = move_parts(playspace, parts, curr_wind)
        wind += 1

        # drop
        can_fall = can_drop(playspace)
        if can_fall:
            parts = get_pieces(playspace)
            parts = sorted(parts, key=take_second)
            playspace = drop_parts(playspace, parts)

    parts = get_pieces(playspace)
    playspace = lock_parts(playspace, parts)

    if (piece > 0 and piece % 10 == 0):
        playspace = clear_out_of_play(playspace)

    if piece > 0 and not found:
        new = str(get_tops(playspace) + [curr_piece])
        if new in seen:
            if last != piece - 1:
                count = 0
                loop_starter = new
                loop_start_piece = piece
                height_at_start = highest_point(playspace)
            else:
                count += 1
                if new == loop_starter:
                    print("Loop starts at", loop_start_piece, "with height", height_at_start,
                          "and continues every", piece - loop_start_piece, "adding", highest_point(playspace) - height_at_start, "each loop")
                    found = True
                    loops_left = math.floor(
                        (1000000000000 - piece) / (piece - loop_start_piece))
                    piece += (loops_left * (piece - loop_start_piece))
                    add_this_many_to_height = (
                        loops_left * (highest_point(playspace) - height_at_start))
            seen[new] = seen[new] + [piece]
            last = piece
        else:
            seen[new] = [piece]

    piece += 1

done = datetime.now()
print("Answer to part 2:", highest_point(playspace) + add_this_many_to_height)
print("Time taken:", done - now)
