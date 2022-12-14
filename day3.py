data = []

with open("input_day_3.txt", "r") as f:
    data = f.read().split('\n')

def calc_prio(c):
    if ord(c) < 91:
        return ord(c) - 64 + 26
    else:
        return erd(c) - 96

total_prio = 0

for line in data:
    if line != "":
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        commoncharacter = ''.join(sorted(set(firstpart) & set(secondpart), key = firstpart.index))
        total_prio += calc_prio(commoncharacter)

print(total_prio)

total_prio = 0

for i in range(0, len(data), 3):
    if data[i] != "":
        commoncharacter = ''.join(sorted(set(data[i]) & set(data[i+1]), key = data[i].index))
        commoncharacter = ''.join(sorted(set(commoncharacter) & set(data[i+2]), key = data[i+2].index))
        total_prio += calc_prio(commoncharacter)

print(total_prio)
