with open('input.txt') as fid:
    data = fid.read().strip().split('\n')

table = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
rev_table = {0: '0', 1: '1', 2: '2', -1: '-', -2:'='}

def snafu2dec(number):
    exp = 0
    result = 0
    for ii in range(len(number)-1,-1,-1):
        result += table[number[ii]]*5**exp
        exp += 1
    return result

def dec2snafu(number):
    # go to base 5 first
    digits = []
    while number > 0:
        digits.insert(0, number % 5)
        number = number // 5
    # translate to snafu system
    for ii in range(len(digits)-1,0,-1):
        match digits[ii]:
            case 3:
                digits[ii] = -2
                digits[ii-1] += 1
            case 4:
                digits[ii] = -1
                digits[ii-1] += 1
            case 5:
                digits[ii] = 0
                digits[ii-1] += 1
    # check the first digit
    if digits[0] > 2:
        digits.insert(0, 1)
        match digits[1]:
            case 3:
                digits[1] = -2
            case 4:
                digits[1] = -1
            case 5:
                digits[1] = 0
    # finally, translate
    result = ''.join([rev_table[x] for x in digits])
    return result


part1 = dec2snafu(sum([snafu2dec(entry) for entry in data]))
print(part1)