## Data preparation
with open('input.txt') as fid:
    data = fid.readlines()
    data = [x.strip() for x in data]
rows = len(data)
cols = len(data[0])


## Refactored after Part 2:
def stencilsearch(grid, scsize, ptrnsize, stencils):
    rows = len(grid)
    cols = len(grid[0])
    result = 0
    for rr in range(0,rows-scsize+1):
        for cc in range(0,cols-scsize+1):
            tmp = ''.join([x[cc:cc+scsize] for x in data[rr:rr+scsize]])
            for sc in stencils:
                if sum(map(lambda x: x[0] == x[1], zip(sc, tmp))) == ptrnsize:
                    result += 1
    return(result)


## Part 1:
result = 0
# horizontal
result += sum([x.count('XMAS')+x.count('SAMX') for x in data])
# vertical
transposed = [''.join(x) for x in zip(*data)]
result += sum([x.count('XMAS')+x.count('SAMX') for x in transposed])
# diagonal
stencils = ['X....M....A....S','S....A....M....X','...X..M..A..S...','...S..A..M..X...']
print(f'Part 1: {result + stencilsearch(data,4,4,stencils)}')


## Part 2:
stencils = ['S.M.A.S.M','S.S.A.M.M','M.S.A.M.S','M.M.A.S.S']
print(f'Part 2: {stencilsearch(data,3,5,stencils)}')
