import sys
from anytree import Node, RenderTree, Resolver

test = bool(int(sys.argv[1]))

file_path = ""
data = ""

if test:
    file_path = "test_day_7.txt"
else:
    file_path = "input_day_7.txt"

with open(file_path, "r") as f:
    data = f.read().split('\n')

root = Node('.', type = 'd', weight = -1)
parent_node = '/.'
looping = False
r = Resolver('name')

def encountered_a_command(temp_data, parent_node, looping):
    if temp_data[0] == '$':
        if temp_data[1] == 'ls':
            looping = True 
        elif temp_data[1] == 'cd' and temp_data[2] == '..':
            temp = parent_node.split('/')
            parent_node = '/'.join(temp[0:len(temp)-1])
        else:
            parent_node = parent_node + '/' + temp_data[2]
    return parent_node, looping

for line in data:
    temp_data = line.split(' ')

    if line != '':
        if looping:
            if temp_data[0] == 'dir':
                Node(temp_data[1], type ='d' , weight = -1, parent=r.get(root,parent_node))
            elif temp_data[0] == '$':
                looping = False
                parent_node, looping = encountered_a_command(temp_data, parent_node, looping)
            else:
                Node(temp_data[1], type = 'f', weight = int(temp_data[0]), parent= r.get(root,parent_node))
        else:
            parent_node, looping = encountered_a_command(temp_data, parent_node, looping)

print(root.children)

# Figure out weigths. From top to bottom.
def weigth_of_location(location):
    node = r.get(root, location)
    if node.weight < 0:
        node_children = r.get(root, location).children
        weight = 0
        for x in node_children:
            weight = weight + weigth_of_location(location + '/' + x.name)
        node.weight = weight

    return node.weight

weigth_of_location('/.')

# Sum all weigths of dirs under 100 000
def sum_weights(location, amount):
    node = r.get(root, location)
    weight = 0

    if node.type == 'd':
        if node.weight < amount:
            weight += node.weight 
        node_children = node.children
        for x in node_children:
            weight = weight + sum_weights(location + '/' + x.name, amount)
    
    return weight

print('total_weight', sum_weights('/.', 100000))

def smallest_dir(location, size, size_list):
    node = r.get(root, location)
    
    if node.type == 'd':
        size_list = size_list + [node.weight]
        node_children = node.children
        for x in node_children:
            if x.weight > size:
                size_list = smallest_dir(location + '/' + x.name, size, size_list)

    return size_list

amount_free = (70000000 - root.weight) 

sizes = smallest_dir('/.', 30000000 - amount_free, [])

sizes.sort()
print('smallest dir', sizes[0])

for pre, fill, node in RenderTree(root):
    print("%s%s%s%s" % (pre, node.name, '  -  ', node.weight))
