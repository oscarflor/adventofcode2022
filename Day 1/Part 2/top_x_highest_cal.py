import heapq

with open ('Day 1/Part 1/input.txt') as input:
    data = input.readlines()

data.append('\n')
#returns sum of calories carried by the top num(default 1) elves
def get_top_num_calories(num=1):
    highest_totals = [0] * num
    heapq.heapify(highest_totals)
    current_cal = 0
    for line in data:
        if line == '\n':
            if current_cal > highest_totals[0]:
                heapq.heapreplace(highest_totals, current_cal)
            current_cal = 0
            continue
        current_cal += int(line)
    print(highest_totals)
    return sum(highest_totals)

print(get_top_num_calories(3))