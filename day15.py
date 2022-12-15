import sys
from multiprocessing import Pool

test = bool(int(sys.argv[1]))
file_path = ""
data = ""
prodata = []
part1 = bool(int(sys.argv[2]))
given_y = int(sys.argv[3])

if test:
    file_path = "test_day_15.txt"
else:
    file_path = "input_day_15_PIM.txt"

with open(file_path, "r") as f:
    data = f.read().split("\n")

# The manhatten distance
def md(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# Steps: read in data to be (S, B, distance)
for line in data:
    if line != "":
        temp = line.split(" ")
        x_s = int(temp[2].split(",")[0].split("=")[1])
        y_s = int(temp[3].split(":")[0].split("=")[1])
        x_b = int(temp[8].split(",")[0].split("=")[1])
        y_b = int(temp[9].split("=")[1])

        dis = md(x_s, y_s, x_b, y_b)
        prodata += [((x_s, y_s), (x_b, y_b), dis)]

print("processed input")

y_max = int(sys.argv[4])
if part1:
    given_y = [given_y]
else:
    given_y = [x for x in range(0, y_max + 1)]

beacon_on_y = []
for _, beacon, _ in prodata:
    if beacon[1] in given_y:
        beacon_on_y += [beacon[0]]

beacon_list = [x[1] for x in prodata]
print("gedfasdf")
# or y in range(0, y_max+1):


def dosth(y):
    for x in range(0, y_max + 1):
        found_it = True
        for s, b, d in prodata:
            found_it = (
                found_it and (x, y) != s and (x, y) != b and md(x, y, s[0], s[1]) > d
            )

        if found_it:
            return x, y

    # with Pool() as pool:
    # for result in pool.map(dosth, range(y_max + 1)):
    # print(result)


print("preprocessed data")

unreachable_points = []
# Then loop over prodata and add all points that cannot be a beacon at height given_y to a list
for y in given_y:
    for source, beacon, dis in prodata:
        height_diff = abs(source[1] - y)

        remain_dist = dis - height_diff

        lower_x = source[0] - remain_dist
        higher_x = source[0] + remain_dist

        if part1:
            unreachable_points += [
                x for x in range(lower_x, higher_x + 1) if x not in beacon_on_y
            ]
        else:
            unreachable_points += [
                (x, y)
                for x in range(lower_x, higher_x + 1)
                if (x, y) not in beacon_list and x >= 0 and x <= y_max
            ]
            print("we are at", y / y_max)
# print("determined unreachable nodes")

# source_list = [x[0] for x in prodata]
# reachable_points = []
# output = []
# for y in range(0, y_max + 1):
#    output_line = ""
#    for x in range(0, y_max + 1):
#
#        if (x,y) in [x[0] for x in prodata]:
#            output_line += "S"
#        elif (x,y) in [x[1] for x in prodata]:
## #           output_line += "B"
#        if (
#            (x, y) not in unreachable_points
#            and (x, y) not in beacon_list
#            and (x, y) not in source_list
#        ):
#            reachable_points += [(x, y)]
#         output_line += "."
##      else:
#           output_line += "#"
#    output += [output_line]
#    print("we are at:", y / (y_max + 1))
# print(unreachable_points)

# for line in output:
#   y print(line)
# print("r", reachable_points)
print(len(set(unreachable_points)))
