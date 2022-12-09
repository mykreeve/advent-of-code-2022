from datetime import datetime

filename = "input/day06input.txt"
file = open(filename, "r")
file = file.readlines()


now = datetime.now()
data = file[0].replace('\n', '')

pos = 3
found = False

while pos < len(data) and found == False:
    pos += 1
    message = data[pos-4:pos]
    if len(message) == len(set(message)):
        found = True

done = datetime.now()
print("Answer to part 1:", pos)
print("Time taken:", done - now)

now = datetime.now()
pos = 13
found = False

while pos < len(data) and found == False:
    pos += 1
    message = data[pos-14:pos]
    if len(message) == len(set(message)):
        found = True

done = datetime.now()
print("Answer to part 2:", pos)
print("Time taken:", done - now)
