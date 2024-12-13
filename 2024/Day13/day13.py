import re

with open('input.txt') as fid:
    data = fid.read()

# prepare data
pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X\=(\d+), Y\=(\d+)'
configs = [list(map(int, x)) for x in re.findall(pattern,data)]

# Let's not use any non-built-in libraries
def inv(mtrx):
    det = mtrx[0][0]*mtrx[1][1]-mtrx[0][1]*mtrx[1][0]
    return [[mtrx[1][1],-mtrx[0][1]],[-mtrx[1][0],mtrx[0][0]]], det

def matmul(mtrx, vctr):
    return [mtrx[0][0]*vctr[0]+mtrx[0][1]*vctr[1],mtrx[1][0]*vctr[0]+mtrx[1][1]*vctr[1]]

# Refactored after part 2
def get_tokens(machines, offset):
    tokens = 0
    for config in machines:
        imat, det = inv([[config[0],config[2]],[config[1],config[3]]])
        result = matmul(imat,[config[4]+offset,config[5]+offset])
        if (result[0]/det == result[0]//det) and (result[1]/det == result[1]//det):
            tokens += 3*result[0]//det+result[1]//det
    return(tokens)

print(f'Part 1: {get_tokens(configs,0)}')
print(f'Part 2: {get_tokens(configs,10_000_000_000_000)}')
