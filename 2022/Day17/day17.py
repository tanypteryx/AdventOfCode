with open('input.txt') as fid:
    data = fid.read().strip()

blows = list(map(lambda x: -1 if x == '<' else 1, data))

# This problem cries for C but let's do it in Python

# Principal idea: use bitpattern of shapes and the cave to
# find collisions quickly

# TODO: Major overhaul for Part 2
# TODO: Bottleneck is the cave list
# TODO: Replace cave list with number, similar to shapes
# TODO: NO STRING OPS WHATSOEVER ALLOWED

def print_shape(shape):
    if not shape: return None
    str = '{:040b}'.format(shape)
    for line in [str[8*i:8*(i+1)].replace('0','.') for i in range(5)]:
        print(line)
    print('\n')

def print_cave(cave):
    if isinstance(cave, list):
        for line in cave:
            str = '{:08b}'.format(line)
            print(str.replace('0','.'))
    else:    
        print_shape(cave)
    print('\n')

def shift(shape, direction, section):
    result = shape >> direction if direction > 0 else shape << -direction
    return shape if ((section & result) > 0) else result
    
def drop(shape):
    return shape // 0x100

def get_cave_section(cave, cavepointer):
    # in principle, everything is already here...
    return sum(cave[ii]*2**(8*(cavepointer-ii+4)) for ii in range(cavepointer,cavepointer+5))

def update_cave(cave, cavepointer, section_update):
    # this is inefficient as hell...
    str = '{:010X}'.format(section_update) 
    update = [int(str[2*ii:2*(ii+1)],16) for ii in range(5)]
    for ii, value in enumerate(update):
        cave[cavepointer+ii] = value
    # necessary, add new inital lines
    count = 0
    while cave[count] == 0x80:
        count += 1
    add_lines = 7 - count
    for _ in range(add_lines):
        cave.insert(0,0x80)

def get_height(cave):
    count = 0
    while cave[count] == 0x80:
        count += 1
    return len(cave)-count-1

def prune_cave(cave):
    # HAHAHAH - does nothing for Part 2
    # ETA came down from several years to "just" 180 days
    # Success, I guess?
    count = 0 
    while (cave[count] | cave[count+1]) != 0xFF:
        count += 1
    return cave[:count+2]

rotate = lambda x: x[1:]+ x[:1] 

shapes = [0x1e00, 0x81C0800, 0x4041C00, 0x1010101000, 0x181800]
# This needs to become a number for Part 2
cave = [0x80 for _ in range(7)] + [0xFF] # inital

settled = True
import time
s = time.time()
no_of_rocks = 0
blowpointer = 0
rockpointer = 0
while no_of_rocks <= 2022:
    if settled:
        rock = shapes[rockpointer]
        rockpointer = (rockpointer +1) % len(shapes)
        cavepointer = 0
        settled = False
        no_of_rocks += 1
        #if no_of_rocks % 100 == 0:
        #    cave = prune_cave(cave)
    # get relevant cave section
    cave_section = get_cave_section(cave, cavepointer)
    # try to shift
    rock = shift(rock, blows[blowpointer], cave_section)
    blowpointer = (blowpointer + 1) % len(blows)
    if (drop(rock) & cave_section) > 0:
        settled = True
        update_cave(cave, cavepointer, cave_section | rock)
    else:
        cavepointer += 1
print(time.time()-s)
print(get_height(cave))
    

  



