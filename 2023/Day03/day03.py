import re

# load and clean data
with open('input.txt') as fid:
    data = fid.readlines()
data = [x.strip() for x in data]

# identify all possible symbols that are 
# neither digits nor periods
symbols = set()
for line in data:
    symbols |= set(line)
symbols = symbols-set('0123456789.')

# cols and rows of the grid
rows,cols = len(data), len(data[0])

# find all grid postions of symbol and part numbers
sym_pos = []
num_pos = []
for row in range(rows):
    for match in re.finditer(r'\d+',data[row]):
        num_pos.append(((row, match.start()),match.group()))
    for col in range(cols):
        if data[row][col] in symbols:
            sym_pos.append(((row,col),data[row][col]))

def candidates(indata):
    # generate set of candidate symbol positions
    extent = len(indata[1])
    dcol = range(-1,extent+1)
    drow = [-1,0,1]
    result = set()
    for row in drow:
        for col in dcol:
            result.add((indata[0][0]+row,indata[0][1]+col))
    return result

# Part 1: Check if a symbol is found in search area around number
sum = 0
sym_set = set([x[0] for x in sym_pos])
for num in num_pos:
    if len(candidates(num).intersection(sym_set)) > 0:
        sum += int(num[1])
print(f'Part 1: {sum}')

# Part 2: Filter "*" symbols, find adjacent parts and filter again
aster_set = set([x[0] for x in sym_pos if x[1] == '*'])
gears = {x: [] for x in list(aster_set)}
for num in num_pos:
    tmp = candidates(num).intersection(aster_set)
    for part in tmp:
        gears[part].append(int(num[1]))
sum = 0
for _, val in gears.items():
    if len(val) == 2:
        sum += val[0]*val[1]
print(f'Part 2: {sum}')
