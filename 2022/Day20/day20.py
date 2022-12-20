# Wow. Could an example be more misleading???
# THE F***INK NUBERS IN THE GODFORSAKEN INPUT ARE NOT F***ING UNIQUE!!!!!!

with open('input.txt') as fid:
    data = fid.read().strip().split('\n')

data = [int(x) for x in data]
# translation table:
tt = dict(zip(range(len(data)),data))

def back_translate(idxarr, tt):
    return [tt[i] for i in idxarr]

def decrypt(idxarr, ttable):
    # now just operate on the index
    for idx, shift in ttable.items():
        loc = idxarr.index(idx)
        idxarr.pop(loc)
        newloc = (loc + shift) % len(idxarr)
        idxarr.insert(newloc, idx)
    return idxarr

def get_result(indata,ttable):
    orig = back_translate(indata, ttable)
    base = orig.index(0)
    sum = 0
    for ii in (1000, 2000, 3000):
        sum += orig[(base+ii) % len(orig)]
    return sum

# Part 1
inarr = list(range(len(data)))
result = decrypt(inarr, tt)
print(get_result(inarr,tt))

# Part 2
crypt = 811589153
ttnew = dict([(key, value*crypt) for key, value in tt.items()])
inarr = list(range(len(data)))
for _ in range(10):
    inarr = decrypt(inarr, ttnew)
print(get_result(inarr,ttnew))