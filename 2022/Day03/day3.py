with open('input.txt') as fid:
    data = fid.readlines()

lines = [n.strip() for n in data]
compartments = [(n[:len(n)//2],n[len(n)//2:]) for n in lines]

# Part #1
common_parts = [list(set(n[0]).intersection(set(n[1])) )[0] for n in compartments]
table = dict(zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',range(1,53)))
print(sum([table[n] for n in common_parts]))

# Part #2
result = 0
for ii in range(0,len(lines),3):
    result += table[list(set(lines[ii])
              .intersection(set(lines[ii+1])
              .intersection(set(lines[ii+2]))))[0]]
print(result)