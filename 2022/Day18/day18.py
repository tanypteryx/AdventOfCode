# Well, I wish that wasn't necessary ...
import sys
sys.setrecursionlimit(6000)

with open('input.txt') as fid:
    data = [x.split(',') for x in fid.read().strip().split('\n')]


# dictionary for O(1) access time
cubes = [(int(x[0]), int(x[1]), int(x[2])) for x in data]

add_tuples = lambda x,y : tuple([m+n for m,n in zip(x,y)])

steps = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def count_facets(cubes, steps = steps):
    facets = 0
    for cube in cubes:
        facets += 6
        for step in steps:
            if add_tuples(cube,step) in cubes:
                facets -= 1
    return facets

def dfs(graph, node, visited=[], tmp=[]):
    visited.append(node)
    tmp.append(node)
    for edge in graph[node]:
        if edge not in visited:
            dfs(graph, edge, visited, tmp)
    return tmp


def build_graph(cubes):
    graph = dict()
    for cube in cubes:
        tmp = []
        for step in steps:
            if add_tuples(cube, step) in cubes:
                tmp.append(add_tuples(cube, step))
        graph[cube] = tmp
    return graph

def find_connected(graph):
    visited = []
    cc = []
    for cube in graph.keys():
        if cube not in visited:
            tmp = []
            cc.append(dfs(graph,cube,visited, tmp))
    return cc


# find exposed surfaces
print(count_facets(cubes))

# find connected interior spaces not having at least one cube on surface
# For this:
# Invert the space and search for connected areas
# this should give exterior and interior
inverse = set([(x,y,z) for x in range(-1,21) for y in range(-1,21) for z in range(-1,21)]).difference(set(cubes))
ig = build_graph(list(inverse))
enclosures = find_connected(ig)
# eliminate enclosures where no outside connection is contained (any value of 0 or 20 in cubes)
outside = []
for ii, enc in enumerate(enclosures):
    for x,y,z in enc:
        if x==-1 or y ==-1 or z ==-1 or x ==20 or y==20 or z == 20:
            outside.append(enc)
            break
# there seems to be only one outside volume (might not be true for all inputs)
# let's run with that
outside = outside[0]
# for all cubes, check if they touch the outside
exposed = 0
for cube in cubes:
    for step in steps:
        if add_tuples(step,cube) in outside:
            exposed += 1
print(exposed)
#cg = build_graph(cubes)
#droplets = find_connected(cg)