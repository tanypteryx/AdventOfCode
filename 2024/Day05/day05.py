with open('input.txt') as fid:
    data = fid.readlines()
    rules = [x.strip().split('|') for x in data if '|' in x]
    pages = [x.strip().split(',')  for x in data if ',' in x]

# build ruleset 
ruleset = {}
for rule in rules:
    if rule[0] in ruleset:
        ruleset[rule[0]].append(rule[1])
    else:
        ruleset[rule[0]] = [rule[1],]

# check if rules fulfilled
invalid = 0
result = 0
invalids = []
for page in pages:
    invalid = False
    for ii in range(len(page)):
        if page[ii] in ruleset:
            if len(set(ruleset[page[ii]]).intersection(set(page[:ii]))) > 0:
                invalid = True
                invalids.append(page)
                break
    if not invalid:
        result += int(page[len(page)//2])
print(result)

finished = False
while not finished:
    finished = True
    for page in invalids:
        for ii in range(len(page)):
            if page[ii] in ruleset:
                isec = list(set(ruleset[page[ii]]).intersection(set(page[:ii])))
                if len(isec) > 0:
                    finished = False
                    idx = page.index(isec[0])
                    buffer = page[ii]
                    page[ii] = page[idx]
                    page[idx] = buffer

result = 0
for page in invalids:
    result += int(page[len(page)//2])
print(result)


