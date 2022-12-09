def select_rc(pos, grid):
    row = grid[pos[0]]
    col = [ x[pos[1]] for x in grid]
    return row[:pos[1]][::-1], row[::-1][:-pos[1]-1][::-1], col[:pos[0]][::-1], col[::-1][:-pos[0]-1][::-1]

with open('input.txt') as fid:
    data = [list(map(int, list(x.strip()))) for x in fid.readlines()] 



searchgrid = [(i,j) for i in range(1,len(data)-1) for j in range(1,len(data[0])-1)]

# Part 1:
total = 0
for x in searchgrid:
    #print(([max(n) for n in select_rc(x, data)]) , data[x[0]][x[1]])
    if min([max(n) for n in select_rc(x, data)]) < data[x[0]][x[1]]: total += 1

print(total + 2*len(data) + 2*(len(data[0])-2))

# Part 2:

maxscore = 0
for x in searchgrid:
    my_height = data[x[0]][x[1]]
    viewlines = select_rc(x, data)
    score = 1
    for v in viewlines:
        tmp = [h >= my_height for h in v]
        vd = 0
        #print(tmp)
        for t in tmp:
            vd += 1
            if t: break
        score = score*vd
    if score > maxscore: maxscore = score

print(maxscore)