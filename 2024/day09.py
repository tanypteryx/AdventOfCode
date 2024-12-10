with open('input.txt') as fid:
    data = fid.read().strip()
files = [int(x) for x in data[::2]]
empty = [int(x) for x in data[1::2]]
files = list(zip(range(len(files)),files))
total_length = sum(empty)+sum([x[1] for x in files])
max_id = files[-1][0]
fmt = f'0{len(str(max_id))}d'
# create array total_length times digits of maxid
disk = []
# see that both lists have same length
if len(empty) < len(files):
    empty.append(0)

newdisk = []
for file, void in zip(files,empty):
    [newdisk.append(file[0]) for _ in range(file[1])]
    [newdisk.append(None) for _ in range(void)]

free = newdisk.index(None)
for ii in range(len(newdisk)-1,0,-1):
    if newdisk[ii]:
        newdisk[free] = newdisk[ii]
        newdisk[ii] = None
        free = newdisk.index(None)
    if ii <= free:
        break
result = newdisk[:free]
result = sum(list(map(lambda x: x[0]*x[1], zip(range(len(result)),result))))
print(f'Part 1: {result}')

# Part 2: Different Approach
newdisk = []
newempty = []
newfiles = []
for file, void in zip(files,empty):
    newfiles.append((len(newdisk), file[1], file[0]))
    [newdisk.append(file[0]) for _ in range(file[1])]
    newempty.append([len(newdisk), void])
    [newdisk.append(None) for _ in range(void)]

def find_fit(length, spaces):
    result = None
    for entry in spaces:
        if entry[1] >= length:
            return(entry)



for entry in newfiles[::-1]:
    tmp = find_fit(entry[1],newempty)
    if tmp and (tmp[0]<entry[0]):
        old = tmp.copy()
        for ii in range(entry[1]):
            newdisk[old[0]+ii] = entry[2]
            newdisk[entry[0]+ii] = None
            tmp[0] += 1
            tmp[1] -= 1
result = [x if x else 0 for x in newdisk]
result = sum(list(map(lambda x: x[0]*x[1], zip(range(len(result)),result))))
print(f'Part 2: {result}')


