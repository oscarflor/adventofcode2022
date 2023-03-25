from pprint import pprint
with open ('Day 8/input.txt') as input:
    data = input.readlines()

trees = [[] for i in range(len(data[0])-1)] #empty lists for trees (2d array basically)

# creates trees list
for row, line in enumerate(data):
    line = line.rstrip()
    for ch in line:
        trees[row].append((int(ch), False))

# loops through all trees and checks for visibility
total_visible = 0
for i, row in enumerate(trees):
    tallest_tree = -1
    for j, tree in enumerate(row):
        if tree[0] > tallest_tree:
            tallest_tree = tree[0]
            if not tree[1]:
                # is visible from left side
                total_visible += 1
                trees[i][j] = (tree[0], True)
                

for i, row in enumerate(trees):
    tallest_tree = -1
    for j, tree in enumerate(reversed(row)):
        print('checking', tree, tallest_tree)
        if tree[0] > tallest_tree:
            tallest_tree = tree[0]
            if not tree[1]:
                # is visible from right side
                total_visible += 1
                trees[i][-j-1] = (tree[0], True)


for i, col in enumerate(zip(*trees)):
    tallest_tree = -1
    for j, tree in enumerate(col):
        if tree[0] > tallest_tree:
            tallest_tree = tree[0]
            if not tree[1]:
                # is visible from top side
                total_visible += 1
                trees[j][i] = (tree[0], True)


for i, col in enumerate(reversed(list(zip(*trees)))):
    tallest_tree = -1
    for j, tree in enumerate(reversed(col)):
        if tree[0] > tallest_tree:
            tallest_tree = tree[0]
            if not tree[1]:
            # is visible from bottom side
                total_visible += 1
                trees[-j-1][-i-1] = (tree[0], True)

print(total_visible)
