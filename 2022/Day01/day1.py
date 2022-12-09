with open('input.txt') as fid:
    data = fid.read()

data = [sum(map(lambda x: 0 if x =='' else int(x), n.split('\n'))) for n in data.split('\n\n')]

# Part 1
print(max(data))

# Part 2
print(sum(sorted(data)[-3:]))