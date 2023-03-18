with open ('Day 4/input.txt') as input:
    data = input.readlines()

total = 0
for pair in data:
    pairs = pair.strip().split(',')
    pairs[0] = [int(i) for i in pairs[0].split('-')]
    pairs[1] = [int(i) for i in pairs[1].split('-')]
    # if real code this if should probably be a helper function for clarity (it basically reads is pair 1 a subset of pair 2 or is pair 2 a subset of pair 1)
    if (pairs[0][1] <= pairs[1][1] and pairs[0][0] >= pairs[1][0]) or \
        (pairs[1][1] <= pairs[0][1] and pairs[1][0] >= pairs[0][0]):
        total += 1

print(total)

'''
[['5', '94'], ['2', '95']] - complete overlap
range(max(5, 2), min(94,95)+1)
range(5,95)
if the range is not empty, there's overlap

[['24', '73'], ['74', '92']] - no overlap
range(max(24, 74), min(73,92)+1)

[['19', '99'], ['19', '97']] - complete overlap
range(max(19, 19), min(99,97)+1)
range(99,20)

['2', '95']] [['5', '94']
'''