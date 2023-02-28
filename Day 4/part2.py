with open ('Day 4/input.txt') as input:
    data = input.readlines()

total = 0
for pair in data:
    pairs = pair.strip().split(',')
    pairs[0] = [int(i) for i in pairs[0].split('-')]
    pairs[1] = [int(i) for i in pairs[1].split('-')]
    if max(pairs[0][0], pairs[1][0]) <= min(pairs[0][1], pairs[1][1]):
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
range(max(19, 99), min(19,97)+1)
range(99,20)
'''