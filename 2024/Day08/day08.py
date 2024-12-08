with open('input.txt') as fid:
    data = fid.read().splitlines()


# helper functions
vecadd = lambda x,y: (x[0]+y[0],x[1]+y[1])
vecneg = lambda x: (-x[0],-x[1])
vecdiff = lambda x,y: vecadd(x,vecneg(y))
scalar = lambda a, x: (a*x[0],a*x[1])

check_boundary = lambda ll, rr, cc: (ll[0] >= 0) and (ll[1] >= 0) and (ll[0] < rr) and (ll[1] < cc)


# Part 1
def find_antinodes(locs):
    result = []
    for ii, loc in enumerate(locs[:-1]):
        for loc2 in locs[ii+1:]:
            tmp = vecdiff(loc,loc2)
            result.append(vecadd(loc,tmp))
            result.append(vecadd(loc2,vecneg(tmp)))
    return(result)

# Part 2 - could be generalized to include Part 1, but why bother?
def find_extended_antinodes(locs, rows, cols):
    result = []
    for ii, loc in enumerate(locs[:-1]):
        for loc2 in locs[ii+1:]:
            tmp = vecdiff(loc,loc2)
            multi = 0
            while check_boundary(vecadd(loc,scalar(multi,tmp)),rows,cols):
                result.append(vecadd(loc,scalar(multi,tmp)))
                multi += 1
            multi = 0
            while check_boundary(vecadd(loc2,scalar(multi,vecneg(tmp))),rows,cols):
                result.append(vecadd(loc2,scalar(multi,vecneg(tmp))))
                multi += 1
    return(result)


def mapfilter(data,rows,cols):
    result = data.copy()
    for entry in data:
        if not check_boundary(entry, rows, cols):
            result.remove(entry)
    return result

# prepare data and identify attena locations
rows = len(data)
cols = len(data[0])
data = ''.join(data)
antennas = set(data)
antennas.remove('.')
findpos = lambda ltr, text: [(i // rows, i % rows) for i, ch in enumerate(text) if ch==ltr]
locations = {x: findpos(x,data) for x in antennas}

# Part 1
result = []
for antenna in antennas:
    result += find_antinodes(locations[antenna])
print(f'Part 1: {len(mapfilter(set(result),rows,cols))}')

# Part 2
result = [] 
for antenna in antennas:
    result += find_extended_antinodes(locations[antenna],rows,cols)
print(f'Part 2: {len(set(result))}')

