import sys

test = bool(int(sys.argv[1]))
file_path = ""
data = ""

if test:
    file_path = "test_day_10.txt"
else:
    file_path = "input_day_10.txt"

with open(file_path, "r") as f:
    data = f.read().split('\n')

result = 1
cycle_no = 0
signal_strength = []
crt = ""

def one_cycle(cycle_no, signal_strength, result, crt):
    cycle_no = cycle_no + 1
    if (cycle_no + 20) %  40 == 0:
        signal_strength += [cycle_no * result]

    if (cycle_no - 1) % 40>= result - 1 and (cycle_no - 1 ) % 40 <= result + 1:
        crt += "#"
    else:
        crt += "."
    return cycle_no, signal_strength, result, crt

for line in data:
    if line != "":
        data_line = line.split(' ')
        match data_line[0]:
            case "noop":
                cycle_no, signal_strength, result, crt = one_cycle(cycle_no, signal_strength, result, crt)
            case "addx":
                cycle_no, signal_strength, result, crt = one_cycle(cycle_no, signal_strength, result, crt)  
                cycle_no, signal_strength, result, crt = one_cycle(cycle_no, signal_strength, result, crt) 
                result += int(data_line[1])

chunks = len(crt)
chunk_size = 40
for line in [ crt[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]:
    print(line)
print(sum(signal_strength))
