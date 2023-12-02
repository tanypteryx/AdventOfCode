from re import findall

with open('input.txt') as fid:
    data = fid.readlines()

# regular expression to get information
game_pattern = r'Game (\d+):'
color_pattern = r"(\d+)\s*(red|green|blue)"
result = {}
for line in data:
    tmp = {'red': [], 'green': [], 'blue': []}
    game_no = findall(game_pattern, line)[0]
    colors = findall(color_pattern,line)
    for color in colors:
        tmp[color[1]].append(int(color[0]))
    result[game_no] = tmp

# Part 1:
max_red = 12
max_green = 13
max_blue = 14
possible = 0
for key, val in result.items():
    if (max(val['red']) <= max_red) and (max(val['green']) <= max_green) and (max(val['blue']) <= max_blue):
        possible += int(key)
print(f'Part 1: {possible}')

# Part 2:
powers = 0
for _, val in result.items():
    powers += max(val['red'])*max(val['green'])*max(val['blue'])
print(f'Part 2: {powers}')
