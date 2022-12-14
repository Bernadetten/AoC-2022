import sys

test = bool(int(sys.argv[1]))
file_path = ""
data = ""

if test:
    file_path = "test_day_8.txt"
else:
    file_path = "input_day_8.txt"

with open(file_path, "r") as f:
    data = f.read().split('\n')

matrix = []
visible = []
scenic = []

for line in data:
    if line != "":
        row = []
        row_v = []
        row_s = []
        for char in line:
            row = row + [int(char)]
            row_v = row_v + [0]
            row_s = row_s + [0]
        matrix = matrix + [row]
        visible = visible + [row_v]
        scenic = scenic + [row_s]

# All trees on the edge are visible:
for i, line in enumerate(visible):
    for j, elem in enumerate(line):
        if i == 0 or (i == len(visible)-1) or j==0 or j==len(line)-1:
            visible[i][j] = 1

# From the top
for i in range(len(matrix[0])): 
    to_the_top = 0
    for j in range(len(matrix)):
        if to_the_top < matrix[j][i]:
            visible[j][i] = 1
            to_the_top = matrix[j][i]

# From the bottom
for i in range(len(matrix[0])): 
    to_the_bottom = 0
    for j in range(len(matrix)):
        if to_the_bottom < matrix[len(matrix[0])-1-j][i]:
            visible[len(matrix[0])-1-j][i] = 1
            to_the_bottom = matrix[len(matrix[0])-1-j][i]

# From the right
for i, row in enumerate(matrix): 
    to_the_right = 0
    for j, elem in enumerate(reversed(row)):
        if to_the_right < elem:
            visible[i][len(row)-1-j] = 1
            to_the_right = elem

# From the left
for i, row in enumerate(matrix): 
    to_the_left = 0
    for j, elem in enumerate(row):
        if to_the_left < elem:
            visible[i][j] = 1
            to_the_left = elem

# Sum over the visible array
count = 0
for row in visible:
    for elem in row:
        count = count + elem

# Print result
print(count)

def calc_scenic(i,j,matrix):
    count = 0
    result = 1
    # Down
    if i != len(matrix[0])-1:
        high = matrix[i+1][j]
        count = count + 1
        if high < matrix[i][j]: 
            for k in range(i+2, len(matrix[0])):
                count = count + 1
                high = matrix[k][j]
                if matrix[k][j] >= matrix[i][j]:
                    break

    result = result * count

    count = 0
    # Up
    if i != 0:
        high = matrix[i-1][j]
        count = count + 1
        if high < matrix[i][j]:
            for k in reversed(range(0, i-1)):
                count = count + 1
                high = matrix[k][j]
                if matrix[k][j] >= matrix[i][j]:
                    break
    result = result * count

    count = 0
    # Left
    if j != 0:
        high = matrix[i][j-1]
        count = count + 1
        if high < matrix[i][j]:
            for k in reversed(range(0, j-1)):
                count = count + 1
                high = matrix[i][k]
                if matrix[i][k] >= matrix[i][j]:
                    break
    result = result * count

    count = 0
    # Right
    if j != len(matrix)-1:
        high = matrix[i][j+1]
        count = count + 1
        if high < matrix[i][j]:
            for k in range(j+2, len(matrix)):
                count = count + 1
                high = matrix[i][k]
                if matrix[i][k] >= matrix[i][j]:
                    break

    result = result * count
    return result
# 
max_scenic = 0
for i, line in enumerate(matrix):
    for j, elem in enumerate(line):
        scenic[i][j] = calc_scenic(i,j,matrix)
        if scenic[i][j] > max_scenic:
            max_scenic = scenic[i][j]

print(max_scenic)

