with open ('Day 3/input.txt') as input:
    data = input.readlines()

total = 0
for i in range(0, len(data), 3):
    elf1, elf2, elf3 = data[i].strip(), data[i+1].strip(), data[i+2].strip()
    intersection = set(elf1) & set(elf2) & set(elf3)
    item = intersection.pop()
    if item.isupper():
        total += ord(item) - 38
    else:
        total += ord(item) - 96

print(total)