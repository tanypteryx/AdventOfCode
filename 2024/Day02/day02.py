with open("input.txt") as fid:
    data = fid.readlines()
data = [list(map(int,x.strip().split())) for x in data]

# Part 1
result = 0
for line in data:
    tmp = [x[0]-x[1] for x in zip(line[:-1],line[1:])]
    if (sum([x > 0 for x in tmp])) == len(line)-1 or  (sum([x < 0 for x in tmp])) == len(line)-1:
        if sum([(abs(x) > 0) and (abs(x) < 4) for x in tmp]) == len(line)-1:
            result += 1
print(f'Part 1: {result}')

# Part 2
result = 0
for line in data:
    for pos in range(len(line)):
        removed = line.copy()
        removed.pop(pos)
        tmp = [x[0]-x[1] for x in zip(removed[:-1],removed[1:])]
        if (sum([x > 0 for x in tmp])) == len(line)-2 or  (sum([x < 0 for x in tmp])) == len(line)-2:
            if sum([(abs(x) > 0) and (abs(x) < 4) for x in tmp]) == len(line)-2:
                result += 1
                break
print(f'Part 2: {result}')
