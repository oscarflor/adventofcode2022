with open ('Day 2/input.txt') as input:
    data = input.readlines()

'''
A for Rock, B for Paper, and C for Scissors.
X for Rock, Y for Paper, and Z for Scissors.

Scores: 6 win, 3 draw, 0 loss
'''
choice_score = {'X': 1, 'Y': 2, 'Z': 3}
outcomes = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}
total_score = 0
for round in data:
    opponent, me = round.split(' ')
    total_score += choice_score[me.strip()] + outcomes[round.strip()]
print(total_score)



