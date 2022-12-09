import re
from copy import deepcopy
from visualizer import *

with open('input.txt') as fid:
    stacks = [fid.readline() for _ in range(10)]
    instructions = fid.readlines()

# fill stacks
display = init_screen()



stacks = stacks[::-1]
result = [[],[],[],[],[],[],[],[],[]]
for line in range(2,10):
    idx = range(1,len(stacks[line])+1,4)
    packs = [stacks[line][n] for n in idx]
    for ii in range(9):
        if packs[ii] != ' ':
            result[ii].append(packs[ii])
buffer = deepcopy(result)


# Part 1
update_screen(display, result)
for ins in instructions:
    rex = r'move (\d+) from (\d+) to (\d+)'
    mt = re.findall(rex,ins)[0]
    origin = int(mt[1])-1
    target = int(mt[2])-1
    for _ in range(int(mt[0])):
        result[target].append(result[origin].pop(-1))
    update_screen(display, result)
end_screen()
print(''.join([n[-1] for n in result]))

# Part 2
result = buffer
for ins in instructions:
    rex = r'move (\d+) from (\d+) to (\d+)'
    mt = re.findall(rex,ins)[0]
    origin = int(mt[1])-1
    target = int(mt[2])-1
    size = int(mt[0])
    result[target] = result[target] + result[origin][-size:]
    result[origin] = result[origin][:-size]
print(''.join([n[-1] for n in result]))