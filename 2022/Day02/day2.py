with open('input.txt') as fid:
    data = fid.readlines()

# Part 1
table = {'AX': 4, 'AY': 8, 'AZ': 3,
         'BX': 1, 'BY': 5, 'BZ': 9,
         'CX': 7, 'CY': 2, 'CZ': 6 }
print(sum([table[''.join(n.split())] for n in data]))

# Part 2
table_win = {'X': 0, 'Y': 3, 'Z': 6}
table = {'AX': 3, 'AY': 1, 'AZ': 2,
         'BX': 1, 'BY': 2, 'BZ': 3,
         'CX': 2, 'CY': 3, 'CZ': 1 }
print(sum([table[''.join(n.split())] for n in data])+sum([table_win[n.split()[1]]for n in data]))