def dijkstra(start, end, nodes):
    unvisited = list(nodes.keys())
    prev = dict([(key,[]) for key in nodes.keys()])
    distances = {x: 1e20 for x in nodes.keys()}
    distances[start] = 0
    while len(unvisited) > 0:
        print(len(unvisited))
        dist_candidates = dict([(key,value) for key, value in distances.items() if key in unvisited])
        u = sorted(dist_candidates.items(), key=lambda item: item[1])[0][0]
        if u == end:
            break
        unvisited.remove(u)
        #print(u, sorted(dist_candidates.items(), key=lambda item: item[1])[0][0])
        for v in nodes[u]:
            if v in unvisited:
                alt = distances[u] + 1
                #print(distances[u],alt)
                if alt < distances[v]:
                    distances[v] = alt
                    prev[v].append(u)

    return distances, prev


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
        if data[ii][jj] == "E":
            end = (ii,jj)


# Part 1
dists, prevs = dijkstra(start, end ,nodes)
print(dists[end])


# Part 2
#for ii in range(rdim):
#    for jj in range(cdim):
#        if data[ii][jj] =='a':
#            print((ii,jj),dists[(ii,jj)])
