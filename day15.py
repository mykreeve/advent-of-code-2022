from datetime import datetime

filename = "input/day15input.txt"
file = open(filename, "r")
file = file.readlines()

now = datetime.now()

sensors = []
beacons = []

for f in file:
    f = f.replace('\n', '')
    f = f.replace('Sensor at x=', '')
    f = f.replace(', y=', ',')
    f = f.replace(': closest beacon is at x=', ',')
    nums = f.split(',')
    nums = map(int, nums)
    (senx, seny, beacx, beacy) = nums
    if (senx, seny) not in sensors:
        distx = abs(senx-beacx)
        disty = abs(seny-beacy)
        sensors.append({'loc': (senx, seny), 'dist': distx + disty})
    if (beacx, beacy) not in beacons:
        beacons.append((beacx, beacy))

minx = 999999
maxx = 0

for x in sensors:
    test = x['loc'][0] - x['dist']
    if test < minx:
        minx = test
    test = x['loc'][0] + x['dist']
    if test > maxx:
        maxx = test
for x in beacons:
    if x[0] < minx:
        minx = x[0]
    if x[0] > maxx:
        maxx = x[0]


def calcdist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


range = None
for s in sensors:
    if s['loc'][1] - s['dist'] <= 2000000 and s['loc'][1] + s['dist'] >= 2000000:
        dist = s['dist'] - calcdist(s['loc'], (s['loc'][0], 2000000))
        left = (s['loc'][0] - dist, 2000000)
        right = (s['loc'][0] + dist, 2000000)
        if not range:
            range = (left[0], right[0])
        else:
            if left[0] < range[0]:
                range = (left[0], range[1])
            if right[0] > range[1]:
                range = (range[0], right[0])

done = datetime.now()
print("Answer to part 1:", range[1] - range[0])
print("Time taken:", done - now)

now = datetime.now()
y = 0
done = False
while y < 4000000 and not done:
    x = 0
    while x < 4000000:
        curr = x
        for s in sensors:
            if s['loc'][1] - s['dist'] <= y and s['loc'][1] + s['dist'] >= y:
                dist = s['dist'] - calcdist(s['loc'], (s['loc'][0], y))
                left = s['loc'][0] - dist
                right = s['loc'][0] + dist
                if left <= x and right >= x:
                    x = right
        if x == curr:
            done = True
            # print(x)
            break
    # print(y)
    y += 1

done = datetime.now()
print("Answer to part 2:", (((x+1)*4000000) + y-1))
print("Time taken:", done - now)
