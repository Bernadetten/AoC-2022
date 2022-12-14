data = []
temp_cal = 0
top_three = [0,0,0]

with open("input_day_1.txt", "r") as f:
    data = f.read().split('\n')

for line in data:
    if line == "":
        top_three = sorted(top_three + [temp_cal], reverse=True)[0:3] 
        temp_cal = 0
    else:
        temp_cal += int(line)

print('Max amount of calories: ' + str(top_three[0]))
print('Summation of the top three: ' + str(sum(top_three)))
