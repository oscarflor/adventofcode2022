from pprint import pprint
with open ('Day 8/input.txt') as input:
    data = input.readlines()

trees = [[] for i in range(len(data[0])-1)] #empty lists for trees (2d array basically)

# creates trees list
for row, line in enumerate(data):
    line = line.rstrip()
    for ch in line:
        trees[row].append((int(ch), {'left':0,'right':0,'up':0,'down':0}))

# loops through all trees and checks for visibility
for i, row in enumerate(trees):
    heights_seen = {}
    for j, tree in enumerate(row):
        if not heights_seen:
            # on left edge
            heights_seen[tree[0]] = j
        elif tree[0] <= trees[i][j-1][0]:
            tree[1]['left'] = 1
        else:
            keys = set(range(tree[0], 10)) & set(heights_seen.keys())
            if keys:
                closest_blocker = -1
                for key in keys:
                    if heights_seen[key] > closest_blocker:
                        closest_blocker = heights_seen[key]
                tree[1]['left'] = j - closest_blocker
            else:
                # no blockers
                tree[1]['left'] = j
        heights_seen[tree[0]] = j
                

for i, row in enumerate(trees):
    heights_seen = {}
    for j, tree in enumerate(reversed(row)):
        if not heights_seen:
            # on right edge
            heights_seen[tree[0]] = j
        elif tree[0] <= trees[i][-j][0]:
            tree[1]['right'] = 1
        else:
            keys = set(range(tree[0], 10)) & set(heights_seen.keys())
            if keys:
                closest_blocker = -1
                for key in keys:
                    if heights_seen[key] > closest_blocker:
                        closest_blocker = heights_seen[key]               
                tree[1]['right'] = j - closest_blocker
            else:
                # no blockers
                tree[1]['right'] = j
        heights_seen[tree[0]] = j


for i, col in enumerate(zip(*trees)):
    heights_seen = {}
    for j, tree in enumerate(col):
        if not heights_seen:
            # on top edge
            heights_seen[tree[0]] = j
        elif tree[0] <= trees[j-1][i][0]:
            tree[1]['up'] = 1
        else:
            keys = set(range(tree[0], 10)) & set(heights_seen.keys())
            if keys:
                closest_blocker = -1
                for key in keys:
                    if heights_seen[key] > closest_blocker:
                        closest_blocker = heights_seen[key]
                tree[1]['up'] = j - closest_blocker 
            else:
                # no blockers
                tree[1]['up'] = j
        heights_seen[tree[0]] = j


for i, col in enumerate(reversed(list(zip(*trees)))):
    heights_seen = {}
    for j, tree in enumerate(reversed(col)):
        if not heights_seen:
            # on top edge
            heights_seen[tree[0]] = j
        elif tree[0] <= trees[-j][-i][0]:
            tree[1]['down'] = 1
        else:
            keys = set(range(tree[0], 10)) & set(heights_seen.keys())
            if keys:
                closest_blocker = -1
                for key in keys:
                    if heights_seen[key] > closest_blocker:
                        closest_blocker = heights_seen[key]
                tree[1]['down'] = j - closest_blocker
            else:
                # no blockers
                tree[1]['down'] = j
        heights_seen[tree[0]] = j

highest_score = 0
for row in trees:
    for tree in row:
        score = tree[1]['left'] * tree[1]['right'] * tree[1]['up'] * tree[1]['down']
        if score > highest_score:
            highest_score = score

print(highest_score)