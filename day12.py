# ord(c) - 96
import queue
import sys

test = bool(int(sys.argv[1]))
file_path = ""
data = ""
grid = []
part1 = bool(int(sys.argv[2]))

if test:
    file_path = "test_day_12.txt"
else:
    file_path = "input_day_12.txt"

with open(file_path, "r") as f:
    data = f.read().split('\n')

start1 = (0,0)
final = (0,0)
visited = set([])
parent = {}

for i, line in enumerate(data):
    if line != "":
        row = []
        for j, char in enumerate(line):
            match char:
                case 'S':
                    row += [1]
                    start1 = (i,j)
                case 'E':
                    row += [26]
                    final = (i,j)
                case _:
                    row += [ord(char)-96]
        grid += [row]

def left(location, grid):
    if location[0] >= 1:
        if grid[location[0]-1][location[1]] - grid[location[0]][location[1]] <= 1:
            return True, (location[0]-1, location[1])
    return False, location 

def right(location, grid):
    if location[0] <= len(grid) - 2:
        if grid[location[0]+1][location[1]] - grid[location[0]][location[1]] <= 1:
            return True, (location[0]+1, location[1])
    return False, location 

def up(location, grid):
    if location[1] >= 1:
        if grid[location[0]][location[1]-1] - grid[location[0]][location[1]] <= 1:
            return True, (location[0], location[1]-1)
    return False, location 

def down(location, grid):
    if location[1] <= len(grid[0]) - 2:
        if grid[location[0]][location[1]+1] - grid[location[0]][location[1]] <= 1:
            return True, (location[0], location[1]+1)
    return False, location 

if part1:
    list_of_start = [start1]
else:
    list_of_start = [(x,0) for x in range(len(grid))] # Not future proof
list_of_lengths = []

for start in list_of_start:
    visited = set([])
    parent = {}
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        move = q.get()

        if move not in visited: 
            r = right(move, grid)
            if r[0]:
                if r[1] not in visited:
                    q.put(r[1])
                    parent[r[1]] = move 
    
            d = down(move, grid )
            if d[0]:
                if d[1] not in visited:
                    q.put(d[1])
                    parent[d[1]] = move        

            l = left(move, grid)
            if l[0]:
                if l[1] not in visited:
                    q.put(l[1])
                    parent[l[1]] = move

            u = up(move, grid)
            if u[0]:
                if u[1] not in visited:
                    q.put(u[1])
                    parent[u[1]] = move 
    
            visited.add(move)

    temp = parent[final]
    length = 1
    while temp != start:
        temp = parent[temp]
        length += 1

    list_of_lengths += [length]

print(min(list_of_lengths))
