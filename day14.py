# The code for day 14 of the AoC 2022

# Input expected:
#   - Whether to use the real data or the test data (where 1 is the real data)
#   - Whether to output the results of the second part of the puzzle or the first (where 1 is the second)
#   - Whether to print the results to the screen (after every sand grain has fallen; where 1 is print the results)
#   - The amount to remove from the left side (useful for small inputs)
#   - The amount to add to the right side (useful for big inputs)

import sys

# Processing the input
use_test_input = bool(int(sys.argv[1]))
if use_test_input:
    data = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]
else:
    with open("input_day_14.txt", "r") as f:
        data = f.read().split("\n")

# User input variables
second_part = bool(
    int(sys.argv[2])
)  # Do we compute the answer to part 2 of the puzzle?
print_output = bool(int(sys.argv[3]))  # Do we print the intermediate results?
less_width_left = int(sys.argv[4])  # How much do we take away from the left side?
more_width_right = int(sys.argv[5])  # How much do we add to the right side?

# Variables
sand_is_falling = True  # Whether or not sand is still falling.
start_position = (0, 500 - less_width_left)
lowest_rock = 0  # Lowest rock in the input.
highest_y_coordinate = 0
highest_x_coordinate = 0
count_sand = 0

# We preprocess the data into polylines and also ensure we know the size of the grid.
pairs = []
for line in data:
    coordinates = line.split("->")
    temp_pairs = []
    for i, x in enumerate(coordinates):
        if i > 0:
            # Add next line segment of the polyline
            first = coordinates[i - 1].split(",")
            first_x = int(first[0]) - less_width_left
            first_y = int(first[1])
            second = coordinates[i].split(",")
            second_x = int(second[0]) - less_width_left
            second_y = int(second[1])
            temp_pairs += [((first_x, first_y), (second_x, second_y))]

            # Update the size of the input
            if first_x > highest_x_coordinate:
                highest_x_coordinate = first_x
            if first_y > highest_y_coordinate:
                highest_y_coordinate = first_y
            if second_x > highest_x_coordinate:
                highest_x_coordinate = second_x
            if second_y > highest_y_coordinate:
                highest_y_coordinate = second_y

    # Add polyline
    pairs += [temp_pairs]

# Set up empty grid
data = [
    ["." for _ in range(highest_x_coordinate + more_width_right)]
    for _ in range(highest_y_coordinate + 1)
]

# Compute the lowest rock
for i, line in enumerate(data):
    if "#" in line:
        lowest_rock = i
    data[i] = [*line]

# Add a floor beneath the lowest rock.
if second_part:
    data += [["." for _ in range(highest_x_coordinate + more_width_right)]] + [
        ["#" for _ in range(highest_x_coordinate + more_width_right)] for _ in range(5)
    ]

# Process the polylines into rocks in the grid
for pair_list in pairs:
    for pair in pair_list:
        direction = (0, 0)
        if pair[0][0] > pair[1][0]:
            direction = (-1, 0)
        elif pair[0][1] > pair[1][1]:
            direction = (0, -1)
        elif pair[0][0] < pair[1][0]:
            direction = (1, 0)
        elif pair[0][1] < pair[1][1]:
            direction = (0, 1)

        pointer = pair[0]
        while pointer != pair[1]:
            data[pointer[1]][pointer[0]] = "#"
            pointer = (pointer[0] + direction[0], pointer[1] + direction[1])

        data[pair[1][1]][pair[1][0]] = "#"

# Compute the final position for a given sand grain.
def calc_final_position(x, y, data):
    data_not_at_rest = True
    while data_not_at_rest:
        # Compute next position
        if data[x + 1][y] == ".":
            x = x + 1
        elif data[x + 1][y - 1] == ".":
            x = x + 1
            y = y - 1
        elif data[x + 1][y + 1] == ".":
            x = x + 1
            y = y + 1
        else:
            return x, y, False

        # Compute whether we are done with part 1.
        if x + 1 > lowest_rock and not second_part:
            return x, y, True


# Computation of sand coming from the source per grain.
while sand_is_falling:
    # Calculate the position of sand
    y, x, moving = calc_final_position(start_position[0], start_position[1], data)

    # Check whether we are done, if it comes back moving we are done, else we need to continue.
    sand_is_falling = not moving

    # If the sand is stationary at the source, that means we are done in part 2.
    if y == 0 and x == 500 - less_width_left:
        sand_is_falling = False

    # Print every sand grain falling
    if print_output:
        for line in data:
            print("".join(line))

    # Update data set
    data[y][x] = "o"
    count_sand += 1

print(count_sand)
