with open ('Day 2/input.txt') as input:
    data = input.readlines()

'''
A for Rock, B for Paper, and C for Scissors.
X for Rock, Y for Paper, and Z for Scissors.

Scores: 6 win, 3 draw, 0 loss
'''
winning_choice = {'A': 'Y', 'B': 'Z', 'C': 'X'}
losing_choice = {'A': 'Z', 'B': 'X', 'C': 'Y'}
equivalencies = {'A': 'X', 'B': 'Y', 'C': 'Z'}
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
    round = round.strip()
    opponent, me = round.split(' ')
    if me == 'X':
        me = losing_choice[opponent]
    elif me == 'Y':
        me = equivalencies[opponent]
    elif me == 'Z':
        me = winning_choice[opponent]
    total_score += choice_score[me] + outcomes[f'{opponent} {me}']
print(total_score)



