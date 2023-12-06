with open('input.txt') as fid:
    data = fid.read().split('\n\n')
data = [x.split('\n') for x in data]

# preprocess data
seeds = [int(x) for x in data[0][0].split(' ')[1:]]
maps = []
for line in data[1:]:
    tmpmap = []
    for submap in line[1:]:
        if submap:
            tmp = [int(x) for x in submap.split()]
            tmpmap.append((tmp[1], tmp[1]+tmp[2], tmp[0]))
    maps.append(tmpmap)


# table lookup
def lookup(key, maps):
    for mp in maps:
        if  mp[0] <= key <= mp[1]:
            return mp[2] + (key - mp[0])
    return None

# range mapping
def range_lookup(range, maps):
    pass

# Part 1
results = []
for idx in seeds:
    for mp in maps:
        tmp = lookup(idx, mp)
        if tmp:
            idx = tmp  
    results.append(idx)
print(f'Part 1: {min(results)}')


# Part 2: range to range mapping
def interval_operations(interval, other_intervals):
    def intersect(a, b):
        return [max(a[0], b[0]), min(a[1], b[1]), b[2], b[3]]

    def is_valid_interval(i):
        return i[0] <= i[1]

    # Calculate Intersection
    intersections = []
    for other in other_intervals:
        inter = intersect(interval, other)
        if is_valid_interval(inter):
            intersections.append(inter)

    # Sort other_intervals for complement calculation
    other_intervals = sorted(other_intervals, key=lambda x: x[0])

    # Calculate Complement
    complement = []
    current_start = interval[0]

    for other in other_intervals:
        inter = intersect(interval, other)
        if is_valid_interval(inter):
            if current_start < inter[0]:
                complement.append([current_start, inter[0] - 1])
            current_start = max(current_start, inter[1] + 1)

    if current_start <= interval[1]:
        complement.append([current_start, interval[1]])

    return intersections, complement

seedranges = []
for sidx in range(0,len(seeds),2):
    seedranges.append([seeds[sidx],seeds[sidx]+seeds[sidx+1]-1])
for map_no in range(len(maps)):
    stagemaps = [[x[0],x[1],x[2],x[0]] for x in maps[map_no]]
    newranges = []
    for sr in seedranges:
        isec, comp = interval_operations(sr, stagemaps)
        newranges += [[x[2]+x[0]-x[3],x[2]+x[1]-x[3]] for x in isec]
        if len(comp) > 0:
            newranges += comp
    seedranges = newranges
print(f'Part 2: {min([x[0] for x in seedranges])}')
