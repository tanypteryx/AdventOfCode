import re
from itertools import combinations

pattern_letters = r'([A-Z][A-Z])'
pattern_flow = r'(\d+);'

with open('input.txt') as fid:
    data = fid.readlines()

network = {}
flowrates = {}
for entry in data:
    valves = re.findall(pattern_letters,entry)
    flow = int(re.findall(pattern_flow, entry)[0])
    network[valves[0]] = valves[1:]
    flowrates[valves[0]] = flow

critical_nodes = ['AA',] + [x for x in flowrates.keys() if flowrates[x] > 0] 

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
            path = [end,]
            while current != start:
                current = parents[current]
                path.append(current)
                count += 1
            return path, count
        for edge in nodes[v]:
            if not explored[edge]:
                explored[edge] = True
                parents[edge] = v
                queue.append(edge)
    return None, None

def find_flow(start, work_nodes, duration, pd, frs):
    wn = work_nodes.copy()
    wn.remove(start)
    flow_max = 0
    for goal in wn:
        ticktime = duration - (pd[(start,goal)] + 1)
        if ticktime >= 0:
            flow = frs[goal]*ticktime + find_flow(goal, wn, ticktime, pd, frs)
            if flow > flow_max: flow_max = flow
    return flow_max 

def find_flow_team(start0, start1, work_nodes, duration0, duration1, pd, frs):
    wn = work_nodes.copy()
    wn.remove(start0)
    if not start0 == start1: wn.remove(start1)
    flow_max = 0
    fork = list(combinations(wn,2))
    fork += [[x[1],x[0]] for x in fork]
    #print(wn)
    for goals in fork:
        ticktime0 = duration0 - (pd[(start0,goals[0])] + 1)
        ticktime1 = duration1 - (pd[(start1,goals[1])] + 1)
        if ticktime0 >= 0 and ticktime1 >= 0:
            flow = frs[goals[0]]*ticktime0 + frs[goals[1]]*ticktime1
            #if duration0 < duration1:
            flow += find_flow_team(goals[0], goals[1], wn, ticktime0, ticktime1, pd, frs)
            #else:  
            #    flow += find_flow_team(goals[1], goals[0], wn, ticktime1, ticktime0, pd, frs)
            if flow > flow_max: flow_max = flow 
        elif ticktime0 >=0:
            flow = frs[goals[0]]*ticktime0 + find_flow(goals[0], wn, ticktime0, pd, frs)
            if flow > flow_max: flow_max = flow 
        elif ticktime1 >=0:   
            flow = frs[goals[1]]*ticktime1 + find_flow(goals[1], wn, ticktime1, pd, frs)
            if flow > flow_max: flow_max = flow 
    return flow_max

# Speed-up: pre-calculate critical distances
critical_pairs = list(combinations(critical_nodes,2))
pairdist = dict([(tuple(cp),bfs(cp[0],cp[1],network)[1]) for cp in critical_pairs])
tmp = pairdist.copy()
for key, value in tmp.items():
    pairdist[(key[1],key[0])] = value 
#print(pairdist)


# Part 1: 
print(find_flow('AA', critical_nodes, 30, pairdist, flowrates)) 

# Part 2:
print(find_flow_team('AA','AA',critical_nodes, 26, 26, pairdist, flowrates))