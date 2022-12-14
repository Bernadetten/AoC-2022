import sys

test = bool(int(sys.argv[1]))
print(test)
file_path = ""
data = []

if test:
    file_path = "test_day_4.txt"
else:
    file_path = "input_day_4.txt"

with open(file_path, "r") as f: 
    data = f.read().split('\n')

count = 0
second_count = 0

for line in data:
    if line != "":
        sections = line.split(',')
        first_pair = sections[0].split('-')
        second_pair = sections[1].split('-')
        first_pair = [int(first_pair[0]), int(first_pair[1])]
        second_pair = [int(second_pair[0]), int(second_pair[1])]

        if first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]:
            count += 1
        elif first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]:
            count += 1
        
        if first_pair[1] >= second_pair[0] and first_pair[0] <= second_pair[0]: 
            second_count += 1
        elif second_pair[1] >= first_pair[0] and second_pair[0] <= first_pair[0]:
            second_count += 1

print(count)
print(second_count)

