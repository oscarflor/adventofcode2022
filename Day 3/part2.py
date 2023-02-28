with open ('Day 3/input.txt') as input:
    data = input.readlines()

total = 0
for i in range(0, len(data), 3):
    elf1, elf2, elf3 = data[i], data[i+1], data[i+2]
    for item in elf1:
        if item in elf2 and item in elf3:
            if item.isupper():
                total += ord(item) - 38
            else:
                total += ord(item) - 96
            break

print(total)