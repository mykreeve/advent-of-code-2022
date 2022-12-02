from datetime import datetime

filename = "input/day02input.txt"
file = open(filename, "r")
file = file.readlines()

# (1 for Rock, 2 for Paper, and 3 for Scissors) plus
# (0 if you lost, 3 if the round was a draw, and 6 if you won).


def get_score(a, b, rock, paper, scissors):
    score = 0
    if (a == 'A'):
        if (b == rock):
            score += 3
        if (b == paper):
            score += 6
    if (a == 'B'):
        if (b == paper):
            score += 3
        if (b == scissors):
            score += 6
    if (a == 'C'):
        if (b == scissors):
            score += 3
        if (b == rock):
            score += 6
    if (b == rock):
        score += 1
    if (b == paper):
        score += 2
    if (b == scissors):
        score += 3
    return score


now = datetime.now()
score = 0
for f in file:
    f = f.replace('\n', '').split(' ')
    [a, b] = f
    score += get_score(a, b, 'X', 'Y', 'Z')

done = datetime.now()
print("Answer to part 1:", score)
print("Time taken:", done - now)

now = datetime.now()
score = 0

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win


def optimal_strategy(a, b):
    if (a == 'A'):
        # rock - if X then lose, play scissors
        if (b == 'X'):
            return 3
        # rock - if Y then draw, play rock
        if (b == 'Y'):
            return 4
        # rock - if Z then win, play paper
        if (b == 'Z'):
            return 8
    if (a == 'B'):
        # paper - if X then lose, play rock
        if (b == 'X'):
            return 1
        # paper - if Y then draw, play paper
        if (b == 'Y'):
            return 5
        # paper - if Z then win, play scissors
        if (b == 'Z'):
            return 9
    if (a == 'C'):
        # scissors - if X then lose, play paper
        if (b == 'X'):
            return 2
        # scissors - if Y then draw, play scissors
        if (b == 'Y'):
            return 6
        # scissors - if Z then win, play rock
        if (b == 'Z'):
            return 7


for f in file:
    f = f.replace('\n', '').split(' ')
    [a, b] = f
    score += optimal_strategy(a, b)

done = datetime.now()
print("Answer to part 2:", score)
print("Time taken:", done - now)
