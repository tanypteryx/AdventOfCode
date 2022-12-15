import re

manhattan = lambda x: ((x[0], x[1]), abs(x[2]-x[0])+abs(x[3]-x[1]))

with open('input.txt') as fid:
    data = fid.readlines()

data = [[int(x) for x in re.findall(r'(-?\d+)',line)] for line in data]
# find field column extent (considering max sensor ranges)
beacons = dict([((x[2],x[3]), 0) for x in data])
sensors = dict([manhattan(x) for x in data]) # contains sensors plus manhattan distance

def interval_union(ivs):
    if not ivs: return []
    ivs = sorted(ivs, key=lambda x: x[0])
    result = [ivs.pop(0),]
    while ivs:
        if result[-1][1] >= ivs[0][0]:
            if ivs[0][1] >= result[-1][1]:
                result[-1][1] = ivs[0][1]
            ivs.pop(0)
        else:
            result.append(ivs.pop(0))
    return result

def find_holes(line_no, grid):
    intervals = []
    for sensor in grid.keys():
        remainder = grid[sensor]-abs(sensor[1]-line_no) 
        if remainder >= 0:
            intervals.append([sensor[0]-remainder, sensor[0]+remainder])  
    return intervals

# Part 1
line = 2_000_000
part1 = interval_union(find_holes(line, sensors))
part1 = sum([x[1]-x[0]+1 for x in part1])
# check beacons and sensors in row
corrector = sum([1 for x in sensors.keys() if x[1] == line]+[1 for x in beacons if x[1] == line])
print(part1 - corrector)

# Part 2
# there can be only one gap and it must be between exactly two intervals 
lines = 4_000_000
for ii in range(0,lines+1):
    tmp = interval_union(find_holes(ii, sensors))
    if len(tmp) == 2 and (0 <= tmp[0][1] <= lines):
        print((tmp[0][1]+1)*lines+ii)
        break
    

