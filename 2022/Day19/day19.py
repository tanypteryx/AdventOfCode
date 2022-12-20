# Let's MC the hell out of this one
from random import choice
import re
pattern = r'Blueprint (\d+): Each ore robot costs (\d+) ore.'+ \
             ' Each clay robot costs (\d+) ore.' + \
             ' Each obsidian robot costs (\d+) ore and (\d+) clay.' + \
             ' Each geode robot costs (\d+) ore and (\d+) obsidian.'

with open('input.txt') as fid:
    data = fid.read()
data = re.findall(pattern,data)

recipes = {}
template = {'nothing', 'ore', 'clay', 'obs', 'geode'}
for entry in data:
    nums = [int(x) for x in entry]
    template = {'nothing': [0,0,0,0], 
                'ore': [nums[1],0,0,0], 
                'clay': [nums[2],0,0,0], 
                'obs': [nums[3],nums[4],0,0], 
                'geode': [nums[5],0,nums[6],0]}
    recipes[nums[0]] = template






weights = {'nothing': 1, 'ore': 2, 'clay': 2, 'obs': 400, 'geode': 4000}
steps = 24

def check_options(resources, costs, weights):
    options = []
    for key, value in costs.items():
        if all([(x-y) >= 0 for x,y in zip(resources,value)]): 
            options += [key,] * weights[key]
    return options
result = 0
"""
for recipe in range(1,31):
    steps = 24
    costs = recipes[recipe]
    weights = {'nothing': 1, 'ore': 2, 'clay': 2, 'obs': 400, 'geode': 4000}
    max_geodes = 0
    best = []    
    for _ in range(100000):
        resources = [0,0,0,0]
        robots = [1,0,0,0]
        #tmp = []
        for _ in range(steps):
            # check available options
            action = choice(check_options(resources, costs,weights))
            newbots = [0,0,0,0]
            match action:
                case 'nothing':
                    pass
                case 'ore':
                    newbots[0] += 1
                    resources = [x-y for x, y in zip(resources, costs['ore'])]
                case 'clay':
                    newbots[1] += 1
                    resources = [x-y for x, y in zip(resources, costs['clay'])]       
                case 'obs':
                    newbots[2] += 1
                    resources = [x-y for x, y in zip(resources, costs['obs'])]
                case 'geode':
                    newbots[3] += 1
                    resources = [x-y for x, y in zip(resources, costs['geode'])]
            resources = [x + y for x,y in list(zip(resources,robots))]
            robots = [x+y for x,y in zip(robots,newbots)]
            #tmp.append(resources + robots)
        if resources[3] > max_geodes:
            #best = tmp
            max_geodes = resources[3]
    print(recipe, max_geodes)
    result += recipe*max_geodes
print(result)
"""
# You know what? DRY be damned. Let's copy+paste this crap
result = 1

for recipe in range(1,4):
    steps = 32
    costs = recipes[recipe]
    weights = {'nothing': 1, 'ore': 2, 'clay': 2, 'obs': 400, 'geode': 4000}
    max_geodes = 0
    best = []    
    for _ in range(1000000):
        resources = [0,0,0,0]
        robots = [1,0,0,0]
        #tmp = []
        for _ in range(steps):
            # check available options
            action = choice(check_options(resources, costs,weights))
            newbots = [0,0,0,0]
            match action:
                case 'nothing':
                    pass
                case 'ore':
                    newbots[0] += 1
                    resources = [x-y for x, y in zip(resources, costs['ore'])]
                case 'clay':
                    newbots[1] += 1
                    resources = [x-y for x, y in zip(resources, costs['clay'])]       
                case 'obs':
                    newbots[2] += 1
                    resources = [x-y for x, y in zip(resources, costs['obs'])]
                case 'geode':
                    newbots[3] += 1
                    resources = [x-y for x, y in zip(resources, costs['geode'])]
            resources = [x + y for x,y in list(zip(resources,robots))]
            robots = [x+y for x,y in zip(robots,newbots)]
            #tmp.append(resources + robots)
        if resources[3] > max_geodes:
            #best = tmp
            max_geodes = resources[3]
    print(recipe, max_geodes)
    result *= max_geodes
print(result)