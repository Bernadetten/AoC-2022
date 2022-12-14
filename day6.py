import sys

test = bool(int(sys.argv[1]))
amount = int(sys.argv[2]) 
file_path = ""
data = ""

if test:
    file_path = "test_day_6.txt"
else:
    file_path = "input_day_6.txt"

with open(file_path, "r") as f:
    data = f.read()

for i in range(len(data)):
    if i+amount < len(data):
        set_of_char = set([])

        for j in range(amount):
            set_of_char.add(data[i+j])

        if len(set_of_char) == amount:
            print(i + amount)
            exit()
