mkcomplex = lambda x: x[0] + x[1]*1j
indexer = lambda x: range(int(x)+1) if x > 0 else range(int(x),1)

def flow_sand(blocked, bottom, infinite = False):
    rocks = blocked.copy()
    count = 0
    overflow = False
    while not(overflow):
        settled = False
        start = 500
        while not settled and start.imag < bottom + 1:
            settled = True
            for flow in 1j, -1+1j, 1+1j:
                if start + flow not in rocks:
                    start += flow
                    settled = False
                    break
        count += 1
        rocks.add(start)
        if start.imag == bottom + 1:
            if infinite:
                rocks.add(start) 
            else:
                 overflow = True
                 count -= 1 # Overcount on last sand (slips away)
        if 500 in rocks:
            return count
    return count

with open('input.txt') as fid:
    data = [x.strip().split('->') for x in fid.readlines()]

data = [[mkcomplex(list(map(int, x.split(',')))) for x in row] for row in data]

# find blocked grid-tiles
rocks = []
for row in data:
    for ii in range(len(row)-1):
        diff = row[ii+1]-row[ii]
        if abs(diff.imag) > 0:
            rocks += [row[ii]+inc*1j for inc in indexer(diff.imag)] 
        else:
            rocks += [row[ii]+inc for inc in indexer(diff.real)]  
rocks = set(rocks)
# find the bottom
bottom = max([int(x.imag) for x in rocks])

# Part 1
print(flow_sand(rocks,bottom))

# Part 2
print(flow_sand(rocks,bottom,infinite=True))