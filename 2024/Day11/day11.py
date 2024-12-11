with open('input.txt') as fid:
    data = fid.read().strip().split()
    data = [int(x) for x in data]

# after the complete f*** - up that was the first implementation (> 10 mins runtime)   
# a new recursive implementation with look-up table

def mutate(stone, steps, lut):
    if steps == 0:
        return 1
    elif (stone, steps) in lut:
        return lut[(stone,steps)]
    elif stone == 0:
        fragments = mutate(1, steps-1, lut)
    elif len(str(stone)) % 2 == 0:
        idx = len(str(stone))//2
        left = int(str(stone)[:idx])
        right = int(str(stone)[idx:])
        fragments = mutate(left, steps-1, lut) + mutate(right, steps-1, lut)
    else:
        fragments = mutate(stone*2024, steps-1, lut)
    lut[(stone, steps)] = fragments
    return fragments
    

lut = {}
result = [mutate(x,25,lut) for x in data]
print(f'Part 1: {sum(result)}')
result = [mutate(x,75,lut) for x in data]
print(f'Part 2: {sum(result)}')

