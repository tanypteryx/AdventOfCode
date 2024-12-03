import re

with open('input.txt') as fid:
    data = fid.read()

mac = lambda ops: sum([int(x[0])*int(x[1]) for x in ops])

pattern = r'mul\((\d+),(\d+)\)'

# Part 1
instr = re.findall(pattern, data)
print(f'Part 1: {mac(instr)}')

# Part 2
data = "do()"+data+"don't()"
instr = [x.split("don't()")[0] for x in data.split("do()")]
instr = re.findall(pattern, ''.join(instr))
print(f'Part 2: {mac(instr)}')
