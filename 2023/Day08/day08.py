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


def find_steps(startnode, endnodes, tree, directions):
    steps = 0
    steppos = 0
    current = startnode
    while current not in endnodes:
        steps += 1
        select = directions[steppos % (len(directions))]
        steppos += 1
        current = tree[current][select]
    return steps

# Part 1:
print(f"Part 1: {find_steps('AAA',['ZZZ',],tree,directions)}")


# Part 2
startnodes = [x for x in tree.keys() if x[-1] == 'A']
endnodes = [x for x in tree.keys() if x[-1] == 'Z']
result = []
for current in startnodes:
    result.append(find_steps(current,endnodes,tree,directions))
