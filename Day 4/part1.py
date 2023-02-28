with open ('Day 4/input.txt') as input:
    data = input.readlines()

total = 0
for pair in data:
    pairs = pair.strip().split(',')
    pairs[0] = [int(i) for i in pairs[0].split('-')]
    pairs[1] = [int(i) for i in pairs[1].split('-')]
    pair1_set = set(range(pairs[0][0], pairs[0][1]+1))
    pair2_set = set(range(pairs[1][0], pairs[1][1]+1))
    if pair1_set.issubset(pair2_set) or pair2_set.issubset(pair1_set):
        total += 1
print(total)