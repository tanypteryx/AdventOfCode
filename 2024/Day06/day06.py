with open('input.txt') as fid:
    data = fid.readlines()
    data = [x.strip() for x in data]

for x in zip(range(len(data)),data):
        xpos = x[1].find('^')
        if xpos != -1:
            ypos = x[0]
            pos = [ypos, xpos]
            data[ypos] = data[ypos].replace('^','.')
            break

origpos = [ypos, xpos]
directions = [
        (0,-1),
        (1,0),
        (0,1),
        (-1,0),
        ]

xmax, ymax = len(data[0]), len(data)
fields = set([tuple(pos +[0,])])
diridx = 0
while True:
    nextpos = [pos[0]+directions[diridx][1],
               pos[1]+directions[diridx][0]]
    if nextpos[0] >= 0 and nextpos[0]<ymax and nextpos[1] >=0 and nextpos[1] < xmax:
        if data[nextpos[0]][nextpos[1]] == '.':
            pos = nextpos
            if tuple(pos+[diridx,]) in fields:
                options += 1
                break
            fields.add(tuple(pos+[diridx,]))
        else:
            diridx = (diridx+1) % 4
    else:
        break
print(len(fields))
options = 0
for yy in range(ymax):
    print(yy)
    for xx in range(xmax):
        if yy == origpos[0] and xx == origpos[1]:
            continue
        pos = origpos
        diridx = 0
        fields = set([tuple(pos +[0,])])
        buffer = data[yy]
        data[yy] = data[yy][:xx] + '#' + data[yy][xx+1:]
        while True:
            nextpos = [pos[0]+directions[diridx][1],
                       pos[1]+directions[diridx][0]]
            #print(pos, directions[diridx],nextpos)
            if nextpos[0] >= 0 and nextpos[0]<ymax and nextpos[1] >=0 and nextpos[1] < xmax:
                if data[nextpos[0]][nextpos[1]] == '.':
                    pos = nextpos
                    if tuple(pos+[diridx,]) in fields:
                        options += 1
                        break
                    fields.add(tuple(pos+[diridx,]))
                else:
                    diridx = (diridx+1) % 4
            else:
                break
        data[yy] = buffer
print(options)


