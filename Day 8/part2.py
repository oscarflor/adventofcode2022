from pprint import pprint
with open ('Day 8/input.txt') as input:
    data = input.readlines()

trees = [[] for i in range(len(data[0])-1)] #empty lists for trees (2d array basically)

# creates trees list
for row, line in enumerate(data):
    line = line.rstrip()
    for ch in line:
        trees[row].append(int(ch))

# loops through all trees and checks for visibility
highest_score = 0
for i, row in enumerate(trees):
    for j, tree in enumerate(row):
        # check entire row and entire col
        score_above = 0
        score_below = 0
        score_right = 0
        score_left = 0
        

        # checks to right of tree
        for c in range(j+1, len(row)):
            score_right += 1
            if trees[i][c] >= tree:
                break
        # checks to left of tree
        for c in range(j-1, -1, -1):
            score_left += 1
            if trees[i][c] >= tree:
                break
        # checks below tree
        for r in range(i+1, len(trees)):
            score_below += 1
            if trees[r][j] >= tree:
                break
        # checks above tree
        for r in range(i-1, -1, -1):
            score_above += 1
            if trees[r][j] >= tree:
                break
        
        tree_score = score_above * score_below * score_left * score_right

        if tree_score > highest_score:
            highest_score = tree_score

            
print(highest_score)