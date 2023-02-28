with open ('Day 3/input.txt') as input:
    data = input.readlines()

total = 0
for line in data:
    line = line.strip()
    length = len(line)
    sack1, sack2 = line[:length//2], line[length//2:]
    for item in sack1:
        if item in sack2:
            if item.isupper():
                total += ord(item) - 38
            else:
                total += ord(item) - 96
            break

print(total)