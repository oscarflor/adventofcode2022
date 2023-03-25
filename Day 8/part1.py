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
total_visible = 0
for i, row in enumerate(trees):
    for j, tree in enumerate(row):
        # checks if on an edge (first or last row or col)
        if i == 0 or j == 0 or i == len(trees)-1 or j == len(trees[0])-1:
            total_visible += 1
        # check entire row and entire col
        else:
            is_visible_above = True
            is_visible_below = True
            is_visible_right = True
            is_visible_left = True

            # checks to right of tree
            for c in range(j+1, len(row)):
                if trees[i][c] >= tree:
                    is_visible_right = False
                    break
            # checks to left of tree
            for c in range(j-1, -1, -1):
                if trees[i][c] >= tree:
                    is_visible_left = False
                    break
            # checks below tree
            for r in range(i+1, len(trees)):
                if trees[r][j] >= tree:
                    is_visible_below = False
                    break
            # checks above tree
            for r in range(i-1, -1, -1):
                if trees[r][j] >= tree:
                    is_visible_above = False
                    break
            if is_visible_above or is_visible_below or is_visible_left or is_visible_right:
                total_visible += 1

print(total_visible)