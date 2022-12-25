with open('input.txt') as fid:
    data = fid.read().strip().split('\n')

# find the initial positions of the elves
elves = []
for yy, row in enumerate(data):
    for xx, col in enumerate(row):
        if col == '#':
            elves.append(xx+1j*yy)

table = {'N': (-1j+1, -1j-1, -1j), 'S': (1j+1, 1j-1, 1j), 'W': (-1,-1+1j, -1-1j), 'E': (1, 1+1j, 1-1j)}
cycle = ['N','S','W','E']
cycm = [-1j, 1j, -1, 1]


def visualize(elves):
    reals = [x.real for x in elves]
    imags = [x.imag for x in elves]
    rows = max(imags)-min(imags)+1
    columns = max(reals)-min(reals)+1
    tags = [elf - min(reals) - 1j*min(imags) for elf in elves]
    for r in range(int(rows)):
        row = ''
        for c in range(int(columns)):
            if c + 1j*r in tags:
                row += '#'
            else:
                row += '.'
        print(row)  
#print(elves)
#visualize(elves)
step = 0
#for step in range(10):
moved = True
while moved:
    # Propsal phase
    proposals = {}
    for ii, elf in enumerate(elves):
        tmp = []
        for direction in range(4):
            neighbours = table[cycle[(direction + step) % 4]]
            if not any([(elf + x) in elves for x in neighbours]):
                tmp.append(elf + cycm[(direction + step) % 4])
        if tmp and len(tmp) < 4:
            proposals[ii] = tmp[0]
    # Execution phase
    if not proposals: moved = False
    for ii in proposals.keys():
        if proposals[ii] not in [value for key, value in proposals.items() if key != ii]:
            elves[ii] = proposals[ii]
    print(step, len(proposals))
    step += 1
print(step)
    #print()
    #print(visualize(elves))

reals = [x.real for x in elves]
imags = [x.imag for x in elves]
print((max(reals)-min(reals)+1)*(max(imags)-min(imags)+1)-len(elves))

    

