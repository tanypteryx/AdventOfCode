with open('input.txt') as fid:
    data = [x.strip().split() for x in fid.readlines()]
col1 = [int(x[0]) for x in data]
col2 = [int(x[1]) for x in data]

# Part 1
result = 0
for x in zip(sorted(col1),sorted(col2)):
    result += abs(x[0]-x[1])
print(f'Part 1: {result}')

# Part 2
col1 = set(col1)
result = 0
for x in col1:
    result += x*col2.count(x)
print(f'Part 2: {result}')

