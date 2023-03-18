from collections import deque
from pprint import pprint

with open ('Day 5/input.txt') as input:
    data = input.readlines()


# construct stacks
stacks_list = []
instructions_begin_index = 0
for index, line in enumerate(data):
    if line.startswith(' 1'):
        instructions_begin_index = index+2
        break
    line = line.rstrip() # strips new lines (\n) from end of string
    line = [line[i:i+4].strip() for i in range(0, len(line), 4)]
    # print(line)
    for stack, crate in enumerate(line, 1):
        if len(stacks_list) < stack:
            stacks_list.append(deque())
        if crate != '':
            stacks_list[stack-1].insert(0, crate)

# pprint(stacks_list)

# move crates around
for instruction in data[instructions_begin_index:]:
    instruction = instruction.strip().split(' ')
    num_moves = int(instruction[1])
    move_from = int(instruction[3])
    move_to = int(instruction[5])
    # print(instruction)
    # print(num_moves, move_from, move_to)
    for i in range(num_moves):
        stacks_list[move_to-1].append(stacks_list[move_from-1].pop())

# pprint(stacks_list)

top_crate = ''
for stack in stacks_list:
    top_crate += stack.pop()[1]

print(top_crate)
