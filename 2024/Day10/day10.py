with open('input.txt') as fid:
    data = fid.read().splitlines()

directions = ((1,0),(-1,0),(0,1),(0,-1))

check_bounds = lambda x, rmax, cmax: x[0] >= 0 and x[0] < rmax and x[1] >=0 and x[1] < cmax
traverse = lambda start, heading: (start[0]+heading[0], start[1]+heading[1])
get_entry = lambda pos, grid: grid[pos[0]][pos[1]] if check_bounds(pos, len(grid), len(grid[0])) else None


def find_goals(data,goal):
    result = []
    for ii, line in enumerate(data):
        for jj in range(len(line)):
            if line[jj] == goal:
                result.append((ii,jj))
    return result


def find_steps(heads, goal, endpoints, trails):
    result = {}
    for head in heads:
        steps = []
        for direction in directions:
            step = traverse(head, direction)
            if step:
                tmp = get_entry(step,data)  
            else: 
                continue
            if tmp == goal:
                steps.append(step)
        if goal == '9':
            result[head] = steps
            endpoints.update(steps)
            trails += steps
            continue 
        if len(steps) != 0:
            result[head] = find_steps(steps,str(int(goal)+1),endpoints,trails)
        else:
            result[head] = None
    return result

trailheads = find_goals(data,'0')
result = 0
newresult = 0
for trailhead in trailheads:
    buffer = set()
    newbuffer = list()
    tmp = find_steps([trailhead,], '1', buffer, newbuffer)
    newresult += len(newbuffer)
    result += len(buffer)
print(f'Part 1: {result}')
print(f'Part 2: {newresult}')
    
    
    

