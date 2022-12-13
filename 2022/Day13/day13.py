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

# Part 2
# make long list
llist = []
for pair in pairs:
    llist += [pair[0],] + [pair[1],]
llist += [[[2]]] + [[[6]]]
# build a merge-sort 
def merge(l, r, key):
    result = []
    while l != [] and r != []:
        if key(l[0],r[0]) == 'T':
            result.append(l[0])
            l = l[1:]
        else:
            result.append(r[0])
            r = r[1:]
    
    if l != []:
        result += l
    if r != []:
        result += r

    return result
def merge_sort(mlist, key):
    if len(mlist) <= 1:
        return mlist
    
    l = []
    r = []
    for ii, entry in enumerate(mlist):
        if ii < len(mlist)//2:
            l.append(entry)
        else:
            r.append(entry)
    
    l = merge_sort(l, key)
    r = merge_sort(r, key)

    return merge(l, r, key)

result = 1
for ii,line in enumerate(merge_sort(llist, compare_lists)):
    if line == [[2]] or line == [[6]]: result *= ii+1
print(result)