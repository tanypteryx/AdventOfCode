def range_to_string(input, string=True):
    limits = input.strip().split('-')
    if string:
        return ' '+' '.join([str(x) for x in list(range(int(limits[0]),int(limits[1])+1))])+' '
    else:
        return list(range(int(limits[0]),int(limits[1])+1))

with open('input.txt') as fid:
    data = fid.readlines()

# Part 1
result = 0
for line in [n.strip().split(',') for n in data]:
    x1 = range_to_string(line[0])
    x2 = range_to_string(line[1])
    if ((x1 in x2) or (x2 in x1)):
        result += 1
print(result)

# Part 2
result = 0
for line in [n.strip().split(',') for n in data]:
    x1 = set(range_to_string(line[0],string=False))
    x2 = set(range_to_string(line[1], string=False))
    if len(x1 & x2) > 0:
        result += 1
print(result)