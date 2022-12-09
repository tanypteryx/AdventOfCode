# TODO: eliminate dependency on root as initial directory
def parser(data):
    dirtree = {'/': {}}
    current_dir = dirtree['/']
    path = ['/',]
    for line in data:
        if '$' in line:
            tmp = line.split()
            if 'cd' in tmp[1]:
                if '..' in tmp[2]:
                    current_dir = dirtree
                    for key in path[:-1]:
                        current_dir = current_dir[key]
                    path = path[:-1]
                else:
                    path.append(tmp[2])
                    current_dir = current_dir[tmp[2]]
                continue
            elif 'ls' in tmp[1]:
                continue
        tmp = line.split()
        if tmp[0] == 'dir':
            current_dir[tmp[1]] = {}
        else:
            current_dir[tmp[1]] = int(tmp[0])
    return dirtree

# Part 1: find total sizes

# TODO: eliminate dependence on global
# TODO: replace list by deja-vu-dictionary
record = []
def dirsize(input):
    global record
    sum = 0
    for key in input.keys():
        if not isinstance(input[key],dict):
            sum += input[key]
        else:
            record.append((key, dirsize(input[key])))
            sum += dirsize(input[key])
    return sum

# Part 1: find total sizes
with open('input.txt') as fid:
    cmds = [x.strip() for x in fid.readlines()]

dirstruct = parser(cmds[1:])
totalsize = dirsize(dirstruct)

print(sum([x[1] for x in set(record) if x[1] <= 100_000]))

# Part 2: find candidate deletion directories
print(min([x[1] for x in set(record) if x[1] >= (totalsize-40_000_000)]))