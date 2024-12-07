from math import log10, ceil
with open('input.txt') as fid:
    data = fid.readlines()
    data = [x.strip().split(':') for x in data]
    data = [(int(x[0]), list(map(lambda n: int(n),x[1].strip().split(' ')))) for x in data]


def solution_found(numbers, target, operators):
    memo = {}

    def dfs(index, current_result):
        if (index, current_result) in memo:
            return memo[(index, current_result)]
        if current_result == target and index == len(numbers):
            return True
        if index == len(numbers) or current_result > target:
            return False
        memo[(index, current_result)] = False 
        for ops in operators:
            tmp = dfs(index + 1, ops(current_result, numbers[index]))
            memo[(index, current_result)] = memo[(index, current_result)] or tmp
            if tmp: 
                break
        return memo[(index, current_result)]

    return dfs(1, numbers[0])

# Part 1
result = 0
operators = [int.__add__,int.__mul__]
for target, ops in data:
    if solution_found(ops, target, operators):
        result += target

print(f'Part 1: {result}')

# Part 2
result = 0
operators = [int.__add__,int.__mul__, lambda m,n: int(f'{m}{n}')]
for target, ops in data:
    if solution_found(ops, target, operators):
        result += target

print(f'Part 2: {result}')
