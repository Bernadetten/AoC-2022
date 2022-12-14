import sys
import ast
import functools
test = bool(int(sys.argv[1]))
file_path = ""
data = ""
pairs = []
singles = [[[2]],[[6]]]

if test:
    file_path = "test_day_13.txt"
else:
    file_path = "input_day_13.txt"

with open(file_path, "r") as f:
    data = f.read().split('\n\n')

for line in data:
    if line != "":
        temp_data = line.split('\n')
        pairs += [(ast.literal_eval(temp_data[0]), ast.literal_eval(temp_data[1]))]
        singles += [ast.literal_eval(temp_data[0]), ast.literal_eval(temp_data[1])]

def eval_pair(first, second):
    #print('next eval', first, '  ', second)
    #print('s',second)

    if isinstance(first, int) and isinstance(second, int):
        return first <= second
    elif not isinstance(first, int) and not isinstance(second, int):
        for elem in zip(first, second):
            result = eval_pair(elem[0], elem[1])
     #       print('e',elem, '                            ', first, '   ', second)
      #      print('eval', elem,'   ', result)
            if result and elem[0] != elem[1]:
       #         print('i get her')
                return True
            elif not result: 
                return result
        
        if len(first) > len(second):
            return False
        if first == second:
            return True
        return True
    elif isinstance(second, int):
        return eval_pair(first, [second])
        #print('heredsiuhjkfkj')
    else:
        return eval_pair([first], second)
        #print('here')
count = []

for pair in pairs:
    #print('next pair', pair)
    if eval_pair(pair[0], pair[1]):
        count += [1]
     #   print('yes')
    else:
        count += [0]

#print([i for i, x in enumerate(count) if x == 1])
print(sum([i+1 for i, x in enumerate(count) if x == 1]))

singles.sort(key=functools.cmp_to_key(lambda x,y: -1 if eval_pair(x,y) else 1 if eval_pair(y,x) else 0))

index_start = singles.index([[2]])  
index_end = singles.index([[6]]) + 1

print(index_start * index_end)


