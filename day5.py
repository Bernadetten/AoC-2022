import sys

test = bool(int(sys.argv[1]))
part1 = bool(int(sys.argv[2]))
file_path = ""
data = []

if test:
    file_path = "test_day_5.txt"
else:
    file_path = "input_day_5.txt"

with open(file_path, "r") as f:
    data = f.read().split("\n")

# Need a list of stacks
stacks_test = [["Z", "N"], ["M", "C", "D"], ["P"]]

stacks_input = [
    ["D", "T", "W", "F", "J", "S", "H", "N"],
    ["H", "R", "P", "Q", "T", "N", "B", "G"],
    ["L", "Q", "V"],
    ["N", "B", "S", "W", "R", "Q"],
    ["N", "D", "F", "T", "V", "M", "B"],
    ["M", "D", "B", "V", "H", "T", "R"],
    ["D", "B", "Q", "J"],
    ["D", "N", "J", "V", "R", "Z", "H", "Q"],
    ["B", "N", "H", "M", "S"],
]

# Loop over the instructions
def process(stacks, p1):
    for line in data:
        if line != "":
            instructions = line.split(" ")

            if p1:
                for i in range(int(instructions[1])):
                    elem = stacks[int(instructions[3]) - 1].pop()
                    stacks[int(instructions[5]) - 1].append(elem)
            else:
                temp_stack = []
                for i in range(int(instructions[1])):
                    elem = stacks[int(instructions[3]) - 1].pop()
                    temp_stack.append(elem)

                for i in range(int(instructions[1])):
                    elem = temp_stack.pop()
                    stacks[int(instructions[5]) - 1].append(elem)
    return stacks


# Pop the top one and print
if test:
    for x in process(stacks_test, part1):
        print(x.pop(), end="")
else:
    for x in process(stacks_input, part1):
        print(x.pop(), end="")
