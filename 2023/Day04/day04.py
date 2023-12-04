import re
with open('input.txt') as fid:
    data = fid.readlines()


result = {}
for line in data:
    game = re.findall(r'Card\s+(\d+)',line)[0]
    tmp = line.split('|')
    wins = [int(x) for x in tmp[0].split(':')[1].split()]
    mine = [int(x) for x in tmp[1].strip().split()]
    result[game] = (wins, mine)

# Part 1: (including preparation for part 2)
total = 0
hitlist = {}
for game, nums in result.items():
    hits = len(set(nums[0]).intersection(set(nums[1])))
    hitlist[game] = [hits, 1]
    if hits > 0:
        total += 2**(hits-1)
print(f'Part 1: {total}')

# Part 2: (this relies on correct ordering of the dict which is dangerous...)
total = 0
max_game = max([int(x) for x in hitlist.keys()])
for game, nums in hitlist.items():
    for ii in range(nums[0]):
        tmp = int(game)+ii+1
        if tmp <= max_game:
            hitlist[str(tmp)][1] += nums[1]
for _, nums in hitlist.items():
    total += nums[1]
print(f'Part 2: {total}')
