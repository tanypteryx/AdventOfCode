import re
from sympy.parsing.sympy_parser import parse_expr
from sympy import solve
from sympy.abc import x
from copy import deepcopy
with open('input.txt') as fid:
    data = fid.read().strip().split('\n')

pattern = r'^([a-z]{4}): (\d+)'
pattern2 = r'([a-z]{4}): ([a-z]{4}) (\+|\-|\*|\/) ([a-z]{4})'

def calc(op,od1,od2):
    match op:
        case '+':
            return od1 + od2
        case '*':
            return od1 * od2
        case '-':
            return od1 - od2
        case '/':
            return od1 // od2

# Parse input
leaves = dict()
nodes = dict()
for line in data:
    p1 = re.findall(pattern,line)
    p2 = re.findall(pattern2, line)
    if p1:
        tmp = p1[0]
        leaves[tmp[0]] = int(tmp[1])
    elif p2:
        tmp = p2[0]
        nodes[tmp[0]] = (tmp[2],tmp[1],tmp[3])

def part1(nd, lv, target):
    nodes = deepcopy(nd)
    leaves = deepcopy(lv)
    nodelen = len(nodes)
    while nodes:
        numkeys = leaves.keys()
        blacklist = []
        for key, value in nodes.items():
            op, m1, m2 = value
            if m1 in numkeys and m2 in numkeys:
                leaves[key] = calc(op,leaves[m1],leaves[m2])
                blacklist.append(key)
        for key in blacklist:
            del nodes[key]
        if len(nodes) == nodelen:
            break
        else:
            nodelen = len(nodes) 
    if target in leaves.keys():
        return(leaves[target])
    else:
        return nodes, leaves


def build_equation(nd, lv, target):
    def get_next(nds, tgt):
        for key, value in nds.items():
            if tgt in value:
                return key
    nodes = deepcopy(nd)
    leaves = deepcopy(lv)
    leaves['humn'] = 'x'
    equation = ''
    startnode = 'humn'
    while startnode != target:
        startnode = get_next(nodes,startnode)
        val = nodes[startnode]
        equation = '('+str(leaves[val[1]])+val[0]+str(leaves[val[2]])+')'
        leaves[startnode] = equation
    return(equation)

# Part 1: iterate through monkeys
print(part1(nodes, leaves, 'root'))

# Part 2: Build two equations
root1 = nodes['root'][1]
root2 = nodes['root'][2]
del nodes['root']
del leaves['humn']
# Try to reduce both trees
a = part1(nodes, leaves, root1)
b = part1(nodes, leaves, root2)
if isinstance(a,int):
    result = a
else:
    equation = build_equation(a[0], a[1], root1)
if isinstance(b, int):
    result = b
else:
    equation = build_equation(b[0], b[1], root2)    
print(solve(parse_expr(equation+str(-result)),x)[0])
