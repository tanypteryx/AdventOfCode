import re
with open('input.txt') as fid:
    data = [x.split('\n') for x in fid.read().split('Monkey') if x !='']


class Monkey:
    def __init__(self, description):
        self.parse(description)
        self.inspections = 0
        self.modder = 3
    
    def parse(self, indata):
        self.items = [int(x) for x in re.findall(r'(\d+)',indata[1])]
        self.test = int(re.findall(r'(\d+)', indata[3])[0])
        self.operands = re.findall( r'(\d+|old)',indata[2])
        self.operator =  re.findall(r'(\+|\*)', indata[2])[0]
        self.iftrue = int(re.findall(r'(\d+)', indata[4])[0])
        self.iffalse = int(re.findall(r'(\d+)', indata[5])[0])

    def step(self, modder):
        table = []
        for item in self.items:
            self.inspections += 1
            if self.operator == '+':
                if self.operands[-1] == "old":
                    item += item
                else:
                    item += int(self.operands[-1])
            else:
                if self.operands[-1] == "old":
                    item *= item
                else:
                    item *= int(self.operands[-1])
            if modder:
                item %= modder
            else:
                item //= 3   
            if item % self.test == 0:
                table.append((item, self.iftrue))
            else:
                table.append((item, self.iffalse))
        self.items = []
        return(table)

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def get_inspections(self):
        return self.inspections
    
    def get_test(self):
        return self.test



# Part 1:
monkeys = [Monkey(data[ii]) for ii in range(len(data))]
for i in range(20):
    for monkey in monkeys:
        transfer = monkey.step(None)
        for it, mk in transfer:
            monkeys[mk].add_item(it)
result = []
for ii, mk in enumerate(monkeys):
    result.append(mk.get_inspections())

tmp = sorted(result)[-2:]
print(tmp[0]*tmp[1])

# Part 2:
modder = 1

monkeys = [Monkey(data[ii]) for ii in range(len(data))]

for mk in monkeys:
    modder *= mk.get_test()

for i in range(10000):
    for monkey in monkeys:
        transfer = monkey.step(modder)
        for it, mk in transfer:
            monkeys[mk].add_item(it)
        

result = []
for ii, mk in enumerate(monkeys):
    result.append(mk.get_inspections())

tmp = sorted(result)[-2:]
print(tmp[0]*tmp[1])