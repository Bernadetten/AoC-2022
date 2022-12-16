from collections import defaultdict

# We need the flow rates, vertices and the distance matrix.
flow_rates = {} 
distance_matrix = defaultdict(lambda: 1337)
vertices = []

# Input
with open("input_day_16.txt", "r") as f:
    data = f.read().split("\n")

# Preprocessing/Populating the variables
for i, line in enumerate(data):
    if line != "":
        temp = line.split(" ")
        node = temp[1]
        vertices += [node]

        flow = int(temp[4].split(";")[0].split("=")[1])
        if flow != 0:
            flow_rates[node] = flow
        
        for j in range(9, len(temp)):
            dest = temp[j][0:2]
            distance_matrix[node, dest] = 1
            distance_matrix[dest, node] = 1

# We use Floyd-Warshall as that allows us to immediately calculate the distance between any pair of points.
# https://www.geeksforgeeks.org/python-construct-cartesian-product-tuple-list/
all_combinations_for_floyd_warshall = [(i, j, k) for k in vertices for i in vertices for j in vertices]
for i,j,k in all_combinations_for_floyd_warshall:  
    distance_matrix[i, j] = min(distance_matrix[i, j], distance_matrix[i, k] + distance_matrix[k, j])

# We solve the dynamic programming problem. We it is actually more of a graph problem, but how do you programme graph problems...
# With a lot of pain.

# No but the gist in this case is we have a limited amount of time, say x, now what we do is consider all next steps. These next
# steps have a different source and less time. And again these subproblems are solved by dividing them until you get to a base case..
# Here it is mathematically speaking:
#
# rev ( time , vertices , source ) = max_{v in vertices} rev( time - time_v - 1 , vertices - {v}, v ) + ( time - time_v - 1 ) * flow_v 
# rev ( 0 , _ , _ ) = 0
# rev ( _ , {} , _ ) = 0
# where 
#       time_v is the time it takes to go from the source to the vertice v
#       
# However, I first wanted to emulate this as a graph, but how even do you program that. 
def solve_1(time, sub_vertices, source):

    results = []
    
    for vertice in sub_vertices:
        
        if distance_matrix[source, vertice] < time:

            revenue = flow_rates[vertice] * (time - distance_matrix[source, vertice] - 1)
            sub_problem = solve_1(time - distance_matrix[source, vertice] - 1, [v for v in sub_vertices if v != vertice], vertice)
            results += [revenue + sub_problem]

    if results != []:
        return max(results)
    return 0

# In this case we do something similar but now we need to keep track of both positions.

def solve_2(time_me, time_el, sub_vertices, source_me, source_el):

    results = []
    
    for vertice_me in sub_vertices:
        for vertice_el in sub_vertices:
            if vertice_me != vertice_el and distance_matrix[source_me, vertice_me] < time_me and distance_matrix[source_el, vertice_el] < time_el:
                
                # Me
                revenue_me = flow_rates[vertice_me] * (time_me - distance_matrix[source_me, vertice_me] - 1)
                revenue_el = flow_rates[vertice_el] * (time_el - distance_matrix[source_el, vertice_el] - 1)

                sub_problem = solve_2(time_me - distance_matrix[source_me, vertice_me] - 1, time_el - distance_matrix[source_el, vertice_el] - 1, [v for v in sub_vertices if v != vertice_me and v != vertice_el], vertice_me, vertice_el)
                
                
                

                results += [revenue_me + revenue_el + sub_problem]

    if results != []:
        return max(results)
    return 0

print(solve_1(30, flow_rates, 'AA'))
print(solve_2(26, 26, flow_rates, 'AA', 'AA'))
