
with open ('Day 1/Part 1/input.txt') as input:
    data = input.readlines()

highest_cal = 0
current_cal = 0
for line in data:
    if line == '\n':
        highest_cal = current_cal if current_cal > highest_cal else highest_cal
        current_cal = 0
        continue
    current_cal += int(line)

print(highest_cal)
