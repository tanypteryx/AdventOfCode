with open('input.txt') as fid:
    data = [x.strip().split() for x in fid.readlines()]

# helper function for hand classification
max_count = lambda xs: max([xs.count(x) for x in set(xs)])



def valuate(data, trans):
    result = []
    for hand in data:
        tmp = ''.join([trans[x] for x in hand[0]])
        result.append(hand.copy()+[int(tmp,16),])
    return result
       

def categorize(data):
    ordered = {str(x): [] for x in range(1,8)}
    for hand in data:
        hand = hand.copy()
        category = len(set(hand[0]))
        if category == 1:
            # 5 of a kind
            ordered['1'].append(hand)
        elif category == 2:
            # 4 of a kind or full house
            if max_count(hand[0]) == 4:
                ordered['2'].append(hand)
            else:
                ordered['3'].append(hand)
        elif category == 3:
            # three of a kind or two pairs
            if max_count(hand[0]) == 3:
                ordered['4'].append(hand)
            else:
                ordered['5'].append(hand)
        elif category == 4:
            # one pair
            ordered['6'].append(hand)
        elif category == 5:
            # none
            ordered['7'].append(hand)
    return ordered


def count_value(ordered):
    rank = 1
    sum = 0
    for ii in range(7,0,-1):
        val = ordered[str(ii)]
        tmp = sorted(val,key = lambda x: x[2])
        for x in tmp:
            sum += rank*int(x[1])
            rank += 1
    return(sum)

def jokerize(data):
    # WATCH OUT: SIDE EFFECTS
    # original data will be altered
    highest = dict(zip('J23456789TQKA',range(14)))
    #ordered = {str(x): [] for x in range(1,8)}
    for hand in data:
        # Joker Present?
        if 'J' in set(hand[0]):
            # How many?
            jokers = hand[0].count('J')
            if jokers == 5:
                hand[0] == 'AAAAA'
            else:
                others = list(set(hand[0]).difference('J'))
                others = [(x, highest[x]) for x in others]
                others = [x[0] for x in sorted(others)]
                other_count = [hand[0].count(x) for x in others]
                high_card = others[max(enumerate(other_count),key=lambda x: x[1])[0]]
                hand[0] = hand[0].replace('J', high_card)
    return data


# Part 1
trans = dict(zip('23456789TJQKA','0123456789abcd'))
print(f'Part 1: {count_value(categorize(valuate(data,trans)))}')
# Part 2:
trans = dict(zip('J23456789TQKA','0123456789abcd'))
print(f'Part 2: {count_value(categorize(jokerize(valuate(data,trans))))}')

