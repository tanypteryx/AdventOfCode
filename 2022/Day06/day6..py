with open('input.txt') as fid:
    data = fid.readline()

token_finder = lambda x, l: [len(set(x[n:n+l])) for n in range(len(x)-l)].index(l) + l
print(token_finder(data,4))
print(token_finder(data,14)) 
