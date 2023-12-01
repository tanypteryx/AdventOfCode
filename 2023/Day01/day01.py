with open('input.txt') as fid:
    input = fid.readlines()

digits = '0123456789'
spelled = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
           'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


# Part 1: Nice and easy
result = 0
for line in input:
    tmp = [x for x in line if x in digits]
    result += int(tmp[0]+tmp[-1])
print(f'Part 1: {result}')

# Part 2:
# it was not nice of the instructions to not tell you that
# the input had to be read both from left to right and
# right to left to replace the textual digits. Frankly,
# that was a BOFH move ...
result = 0
for line in input:
    # go through string from left to right and replace
    lr = line.strip()
    for location in range(len(lr)):
        for text, value in spelled.items():
            lr = lr[:location].replace(text,value)+lr[location:]
    # again, but from right to left
    rl = line.strip()
    for location in range(len(rl),0,-1):
        for text, value in spelled.items():
            rl = rl[:location]+rl[location:].replace(text,value)
    tmp_lr = [x for x in lr if x in digits]
    tmp_rl = [x for x in rl if x in digits]
    result += int(tmp_lr[0]+tmp_rl[-1])
print(f'Part 2: {result}')
