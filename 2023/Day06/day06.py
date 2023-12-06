import re
from math import ceil, floor
with open('input.txt') as fid:
    data = fid.readlines()

# Preprocess data
times = [int(x) for x in re.findall(r'\d+',data[0])]
dists = [int(x) for x in re.findall(r'\d+',data[1])]

# Part 1: Solve t(T-t) > D
result = 1
for T, d in zip(times, dists):
    tmp = T**2-4*d
    t1, t2 = ((T - tmp**(0.5))/2), ((T+tmp**(0.5))/2)
    result *= floor(t2)-ceil(t1)+1
print(f'Part 1: {result}')

# Part 2: Solve t(T-t) > D but merge digits first
T = int(''.join([str(x) for x in times]))
d = int(''.join([str(x) for x in dists]))
result = 1
tmp = T**2-4*d
t1, t2 = ((T - tmp**(0.5))/2), ((T+tmp**(0.5))/2)
result = floor(t2)-ceil(t1)+1
print(f'Part 2: {result}')
