with open('input.txt') as fid:
    data = [x.strip().split() for x in fid.readlines()]

valX = [1]
buffer = None
for instruction in data:
    if instruction[0] == 'noop':
        if buffer is None:
            valX.append(valX[-1])
        else:
            valX.append(valX[-1]+buffer)
            buffer = None
    if instruction[0] == 'addx':
        if buffer is None:
            valX += [valX[-1]] *2
        else:
            valX += [valX[-1]+buffer]*2
        buffer = int(instruction[1])

# Part 1
print(sum([valX[idx]*idx for idx in range(20,221,40)]))
# Part 2
valX = valX[1:]
rows = [valX[ri*40:(ri+1)*40] for ri in range(6)]
for row in rows:
    img = ''
    for ii,cyc in enumerate(row):
        if abs(cyc-ii) <= 1:
            img += '#'
        else:
            img += '.'
    print(img)
