import sys

test = bool(int(sys.argv[1]))
file_path = ""
data = ""

if test:
    file_path = "test_day_9.txt"
else:
    file_path = "input_day_9.txt"

with open(file_path, "r") as f:
    data = f.read().split('\n')

instructions = []

for line in data:
    line_data = line.split(' ')
    if line != "":
        for i in range(int(line_data[1])):
            instructions += [line_data[0]]

#(x,y) = (column, row)
location_head = (0,0)
location_ropes = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
visited_set = set([(0,0)])

def update_location_head(location_head, instruction):
    match instruction:
        case 'R':
            return (location_head[0]+1, location_head[1])
        case 'U':
            return (location_head[0], location_head[1]-1)
        case 'L':
             return (location_head[0]-1, location_head[1])
        case 'D':
            return (location_head[0], location_head[1]+1)

def update_location_tail(location_head, location_tail):
    # Straight moves
    if location_head[0] == location_tail[0]: #Same column
        # The head is underneath the tail, by more than one step
        if location_head[1] - location_tail[1] > 1:  
            return (location_tail[0], location_tail[1] + 1)
        elif location_head[1] - location_tail[1] < -1:
            return (location_tail[0], location_tail[1] - 1)
        else:
            return location_tail
    elif location_head[1] == location_tail[1]: #Same row
        # The head is further to the right
        if location_head[0] - location_tail[0] > 1: 
            return (location_tail[0] + 1, location_tail[1])
        elif location_head[0] - location_tail[0] < -1:
            return (location_tail[0] - 1, location_tail[1])
        else:
            return location_tail

    # Diagonal moves
    possible_moves = [(1,1), (-1,-1), (1,-1), (-1,1)]
    # If it is far enough away to warrent a diagonal move
    if abs(location_head[0] - location_tail[0]) > 1 or abs(location_head[1] - location_tail[1]) > 1: 
        best_move = (0,0)
        best_distance = 100
        for move in possible_moves:
            distance = abs(location_head[0] - (location_tail[0] + move[0])) + abs(location_head[1] - (location_tail[1] + move[1]))
            if distance < best_distance:
                best_move = move
                best_distance = distance
            
        # Doing the best move
        return (location_tail[0] + best_move[0], location_tail[1] + best_move[1])
    
    # Else diagonal move to keep up
    # Close enough -> we dont do anything
    return location_tail


for instruction in instructions:
    location_head = update_location_head(location_head, instruction)
    location_ropes[0] = update_location_tail(location_head, location_ropes[0]) 
    #visited_set.add(location_ropes[0])
    for i, knot in enumerate(location_ropes):
        if i != 0:

            location_ropes[i] = update_location_tail(location_ropes[i-1], location_ropes[i])
            if i == len(location_ropes)-1:
                visited_set.add(location_ropes[-1])

print(len(visited_set))
