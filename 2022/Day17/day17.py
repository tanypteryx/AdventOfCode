with open('test.txt') as fid:
    data = fid.read().strip()

blows = list(map(lambda x: -1 if x == '<' else 1, data))

# This problem cries for C but let's do it in Python

# Principal idea: use bitpattern of shapes and the cave to
# find collisions quickly

# Brute forcing is impossible even with optimization or
# going to C
# Discussions indicated repeating patterns starting at
# some point --> pattern search with manageable number of
# rocks and sensible pattern lengths

def print_shape(shape):
    if not shape: return None
    str = '{:040b}'.format(shape)
    for line in [str[8*i:8*(i+1)].replace('0','.') for i in range(5)]:
        print(line)
    print('\n')

def print_cave(cave):
    if isinstance(cave, list):
        for ii, line in enumerate(cave):
            str = '{:08b}'.format(line)
            str = '|'+str[1:]+'|'
            str = str.replace('1', '#')
            if ii == len(cave)-1:
                print('+-------+')
            else:
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


### HERE BE DRAGONS
# Part 2 completely messed up the code

settled = True
no_of_rocks = 0
blowpointer = 0
rockpointer = 0
dropdepth = 0
blowpat = 0
patterns = []
heights = []
while no_of_rocks <= 100000:
    if settled:
        patterns.append((rockpointer, dropdepth, blowpat))
        rock = shapes[rockpointer]
        rockpointer = (rockpointer +1) % len(shapes)
        cavepointer = 0
        dropdepth = 0
        blowpat = 0
        settled = False
        no_of_rocks += 1
        heights.append(get_height(cave))
    cave_section = get_cave_section(cave, cavepointer)
    rock = shift(rock, blows[blowpointer], cave_section)
    blowpointer = (blowpointer + 1) % len(blows)
    if (drop(rock) & cave_section) > 0:
        settled = True
        update_cave(cave, cavepointer, cave_section | rock)
    else:
        dropdepth += 1
        cavepointer += 1
        if blows[blowpointer] == 1:
            blowpat += 2**cavepointer

print(get_height(cave))
patterns = patterns[1:]
            
def find_pattern(patterns,lmin,lmax,maxpos):
    for ii in range(maxpos):
        for slen in range(lmin,lmax):
            searcher = patterns[ii:ii+slen]
            if patterns[ii+slen:ii+2*slen] == searcher:
                # check the next 10 sequences
                patcheck = 0
                for jj in range(2,11):
                    if patterns[ii+jj*slen:ii+(jj+1)*slen] != searcher:
                        break
                    else:
                        patcheck += 1
                if patcheck == 9:
                    print(f'Pattern found! Rock: {ii}, Length: {slen}')
                    return ii, slen 

ppos, plen = find_pattern(patterns,500,5000,50000)
repeat_height = heights[ppos+plen]-heights[ppos]
repetitions = (1_000_000_000_000-ppos) // plen
leftovers = (1_000_000_000_000-ppos) % plen
leftover_height = heights[ppos+leftovers] - heights[ppos]
print(heights[ppos]+repeat_height*repetitions)
print(heights[ppos]+repeat_height*repetitions + leftover_height)


