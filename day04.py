from datetime import datetime

filename = "input/day04input.txt"
file = open(filename, "r")
file = file.readlines()


now = datetime.now()
count = 0
for f in file:
    f = f.replace('\n', '').split(',')
    first = f[0].split('-')
    first_start = int(first[0])
    first_end = int(first[1])
    second = f[1].split('-')
    second_start = int(second[0])
    second_end = int(second[1])
    if (first_start <= second_start and first_end >= second_end):
        count += 1
    elif (second_start <= first_start and second_end >= first_end):
        count += 1

done = datetime.now()
print("Answer to part 1:", count)
print("Time taken:", done - now)

now = datetime.now()
count = 0
for f in file:
    f = f.replace('\n', '').split(',')
    first = f[0].split('-')
    first_start = int(first[0])
    first_end = int(first[1])
    second = f[1].split('-')
    second_start = int(second[0])
    second_end = int(second[1])
    if (first_start <= second_start and first_end >= second_start):
        # print(first_start, first_end, second_start, second_end, '---', second_start, 'to', first_end)
        count += 1
    elif (second_start <= first_start and second_end >= first_start):
        # print(first_start, first_end, second_start, second_end, '---', first_start, 'to', second_end)
        count += 1
    # else:
        # print(first_start, first_end, second_start, second_end)
        # input('.')


done = datetime.now()
print("Answer to part 2:", count)
print("Time taken:", done - now)
