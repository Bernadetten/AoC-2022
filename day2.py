## Column 1
# A - Rock
# B - Paper
# C - Scissors

## Column 2
# X - Rock
# Y - Paper
# Z - Scissors

# Score of a round is x + y, where x is 1:2:3 for rock:paper:scissors and y is 0:3:6 for lost:draw:win
# Total score determines if you win

# Would map the following to a dictonary matrix if it were a bigger solution space than 9
outcomes = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5, 
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6
}

data = []
score = 0

with open("input_day_2.txt", "r") as f:
    data = f.read().split('\n')

for line in data:
    if line != "":
        score += outcomes[line]

print(score)
score = 0

## Column 2
# X - Need to lose
# Y - Need draw
# Z - Need to win

needToLose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

needToDraw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

needToWin = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

for line in data:
    if line != "":
        line_data = line.split(' ')
        situation = line_data[0] + ' '
        match line_data[1]:
            case 'X':
                situation += needToLose[line_data[0]]
            case 'Y':
                situation += needToDraw[line_data[0]]
            case 'Z':
                situation += needToWin[line_data[0]]
        score += outcomes[situation]

print(score)
