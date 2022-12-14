mkcomplex = lambda x: x[0] + x[1]*1j
indexer = lambda x: range(int(x)+1) if x > 0 else range(int(x),1)

def flow_sand(blocked, bottom, infinite = False):
    rocks = blocked.copy()
    count = 0
    overflow = False
    while not(overflow):
        if infinite and 500 in rocks:
            return count
        settled = False
        start = 500
        while not settled:
            if start + 1j not in rocks:
                start += 1j
            elif start + (-1 + 1j) not in rocks:
                start += -1 + 1j
            elif start + (1 + 1j) not in rocks:
                start += 1 + 1j
            else:
                settled = True
                rocks.add(start)
                count += 1
            if start.imag == bottom + 2:
                if not infinite: 
                    overflow = True 
                else: 
                    settled = True
                    rocks.add(start)
                break
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