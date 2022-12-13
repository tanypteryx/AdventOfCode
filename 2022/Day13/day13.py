import json
from functools import cmp_to_key

def compare_lists(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        else:
            return None 
    if isinstance(left, list) and isinstance(right, list):
        if left == [] and right == []:
            return None 
        if left != [] and right == []:
            return False
        if left == [] and right != []:
            return True
        tval = compare_lists(left[0],right[0])
        if tval != None:
            return tval
        else:
            return compare_lists(left[1:],right[1:])
    if isinstance(left, int) and isinstance(right, list):
        return compare_lists([left,],right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, [right,])

# Load and prepare data

with open('input.txt') as fid:
    data = fid.read()

# pair up and convert to Python lists
pairs = [x.split('\n') for x in data.split('\n\n')]
pairs = [(json.loads(pair[0]), json.loads(pair[1])) for pair in pairs]

# Part 1
idx = []
for ii, pair in enumerate(pairs):
    if compare_lists(pair[0],pair[1]):
        idx.append(ii+1)
print(sum(idx))

# Part 2

# make long list
llist = []
for pair in pairs:
    llist += [pair[0],] + [pair[1],]
llist += [[[2]]] + [[[6]]]
result = 1
llist.sort(key=cmp_to_key(lambda x, y: -1 if compare_lists(x,y) else 1))
for ii, line in enumerate(llist):
    if line == [[2]] or line == [[6]]: result *= ii+1
print(result)