import re
from math import lcm
with open('input.txt') as fid:
    data = fid.readlines()

# read directions and make them numeric
directions = data[0].strip()
tmp = []
for x in directions:
    if x == 'L':
        tmp.append(0)
    else:
        tmp.append(1)
directions = tmp

# read in tree
tree = {}
pattern = r'([A-Z]+)\s=\s\(([A-Z]+), ([A-Z]+)\)'
for line in data[2:]:
    tmp = re.findall(pattern,line)[0]
    tree[tmp[0]] = tmp[1:]


# Part 1
steps = 0
steppos = 0
current = 'AAA'
while current != 'ZZZ':
    steps += 1
    select = directions[steppos % (len(directions))]
    steppos += 1
    current = tree[current][select]
print(f'Part 1: {steps}')


# Part 2
currentnodes = [x for x in tree.keys() if x[-1] == 'A']
# do for each starting node, then find least common multiple
nodesteps = []
for current in currentnodes:
    steps = 0
    steppos = 0
    while current[-1] != 'Z':
        steps += 1
        select = directions[steppos % (len(directions))]
        current = tree[current][select]
        steppos += 1
    nodesteps.append(steps)
print(f'Part 2: {lcm(*nodesteps)}')


