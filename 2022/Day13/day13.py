import json
from copy import deepcopy

def compare_lists(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return "T"
        if left > right:
            return "F"
        else:
            return "U"
    if isinstance(left, list) and isinstance(right, list):
        if left == [] and right == []:
            return "U"
        if left != [] and right == []:
            return "F"
        if left == [] and right != []:
            return "T"
        tval = compare_lists(left[0],right[0])
        if tval != 'U':
            return tval
        else:
            return compare_lists(left[1:],right[1:])
    if isinstance(left, int) and isinstance(right, list):
        return compare_lists([left,],right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, [right,])


with open('input.txt') as fid:
    data = fid.read()

# pair up and convert to Python lists
pairs = [x.split('\n') for x in data.split('\n\n')]
pairs = [(json.loads(pair[0]), json.loads(pair[1])) for pair in pairs]
idx = []

# Part 1
for ii, pair in enumerate(pairs):
    if compare_lists(pair[0],pair[1]) == 'T':
        idx.append(ii+1)

print(sum(idx))