import sys
import re
from itertools import pairwise

test = bool(int(sys.argv[1]))
file_path = ""
data = ""
prodata = []
given_y = [int(sys.argv[2])]
absent_points = []
part1 = bool(int(sys.argv[3]))
max_y = int(sys.argv[4])

if test:
    file_path = "test_day_15.txt"
else:
    file_path = "input_day_15.txt"

with open(file_path, "r") as f:
    data = f.read().split("\n")

# The anhatten distance
def md(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Processing the data.
for line in data:
    if line != "":
        m = re.match(
            r"Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)",
            line.strip(),
        )
        x_s = int(m.group("sx"))
        y_s = int(m.group("sy"))
        x_b = int(m.group("bx"))
        y_b = int(m.group("by"))

        dis = md(x_s, y_s, x_b, y_b)
        prodata += [((x_s, y_s), (x_b, y_b), dis)]

# All y-values we want to loop over if part 2
if not part1:
    given_y = [x for x in range(0, max_y + 1)]

# Merge all ranges
def mergeranges(ranges):
    super_range = ranges[0]
    ranges = ranges[1:]

    for (xl, xh) in ranges:
        #    print('super', super_range)
        #print('comparing to', xl, ' ', xh)

        if not (xl - 1 <= super_range[1] and xl >= super_range[0]): 
            return xl - 1
            
        if xh > super_range[1]:
            super_range = (super_range[0], xh)

    return None

# Now we calculate the impossible ranges
for y in given_y:
    if part1:
        beacon_on_y = [b[0] for _, b, _ in prodata if b[1] == y]

    absent_points = []
    #print(y)
    # We need to add the ranges of points that are not available.
    for source, beacon, dis in prodata:
        height_diff = abs(source[1] - y)

        remain_dist = dis - height_diff

        if remain_dist >= 0:
            #            print('Source ', source, ' y ', y, ' dis ', dis, ' diff ', height_diff) 
            lower_x = source[0] - remain_dist
            higher_x = source[0] + remain_dist

            if part1:
                absent_points += [
                    x for x in range(lower_x, higher_x + 1) if x not in beacon_on_y
                ]
            else: 
                absent_points += [(lower_x, higher_x)]

    # If we are doing part two we need to post process the output per line.
    if not part1:        
        #   print(absent_points)
        absent_points = sorted(absent_points)
        #print(absent_points)
        result = mergeranges(absent_points)
        if result != None:
            print('part2, x:', result, 'y:', y, 'output:', result *4000000 +y)
            sys.exit()

if part1:
    print('part1', len(set(absent_points)))
