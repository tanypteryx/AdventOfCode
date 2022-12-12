def bfs(start, end, nodes):
    queue = []
    explored = dict([(key, False) for key in nodes.keys()])
    explored[start] = True
    queue.append(start)
    parents = dict([(key, None) for key in nodes.keys()])
    while len(queue) > 0:
        v = queue.pop(0)
        if v == end:
            count = 0
            current = end
            while current != start:
                current = parents[current]
                count += 1
            return v, count
        for edge in nodes[v]:
            if not explored[edge]:
                explored[edge] = True
                parents[edge] = v
                queue.append(edge)
    return None, None



with open('input.txt') as fid:
    data = [x.strip() for x in fid.readlines()]

heights_alpha = dict(zip('abcdefghijklmnopqrstuvwxyz',range(26)))
heights_alpha['S'] = 0
heights_alpha['E'] = 25

heights = [[heights_alpha[h] for h in x] for x in data]
rdim = len(heights)
cdim = len(heights[0])
# Convert to graph
nodes = {}
start = None
end = None
for ii in range(rdim):
    for jj in range(cdim):
        tmp = []
        base = heights[ii][jj]
        if ii < rdim-1 and  heights[ii+1][jj]-base <= 1:
            tmp.append((ii+1,jj))
        if ii > 0 and (heights[ii-1][jj]-base) <= 1:
            tmp.append((ii-1,jj))
        if jj < cdim-1 and (heights[ii][jj+1]-base) <= 1:
            tmp.append((ii,jj+1))
        if jj > 0 and (heights[ii][jj-1]-base) <= 1:
            tmp.append((ii,jj-1))
        nodes[(ii,jj)] = tmp
        if data[ii][jj] == 'S':
            start = (ii,jj)
        if data[ii][jj] == 'E':
            end = (ii,jj)


# Part 1
print(bfs(start, end ,nodes))

# Part 2
pls = []
for ii in range(rdim):
    for jj in range(cdim):
        if data[ii][jj] =='a' or data[ii][jj] == 'S':
            tmp = bfs((ii,jj),end,nodes)
            if tmp[0] is not None: pls.append(tmp[1])
print(min(pls))
            
